$ErrorActionPreference = "Stop"

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName Microsoft.VisualBasic

Add-Type @"
using System;
using System.Runtime.InteropServices;

public static class NativeWindow {
    [DllImport("user32.dll")]
    public static extern bool SetForegroundWindow(IntPtr hWnd);

    [DllImport("user32.dll")]
    public static extern bool ShowWindowAsync(IntPtr hWnd, int nCmdShow);
}
"@

$workspaceRoot = "E:\over-300k-journey"
$notesRoot = Join-Path $workspaceRoot "testing\python_notes"
$codeCmd = "E:\Microsoft VS Code\bin\code.cmd"

function Save-ScaledScreenshot {
    param(
        [string]$Path
    )

    $bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
    $source = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height
    $graphics = [System.Drawing.Graphics]::FromImage($source)
    $graphics.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size)

    $targetWidth = 1920
    $targetHeight = 1080
    $target = New-Object System.Drawing.Bitmap $targetWidth, $targetHeight
    $targetGraphics = [System.Drawing.Graphics]::FromImage($target)
    $targetGraphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $targetGraphics.DrawImage($source, 0, 0, $targetWidth, $targetHeight)

    $directory = Split-Path -Parent $Path
    New-Item -ItemType Directory -Force -Path $directory | Out-Null
    $target.Save($Path, [System.Drawing.Imaging.ImageFormat]::Png)

    $targetGraphics.Dispose()
    $target.Dispose()
    $graphics.Dispose()
    $source.Dispose()
}

function Capture-CodeFile {
    param(
        [string]$TargetFile,
        [int]$LineNumber,
        [string]$OutputPath
    )

    $argumentList = @(
        "--new-window"
        "--disable-extensions"
        "--goto"
        "${TargetFile}:$LineNumber"
    )

    $before = @(Get-Process Code -ErrorAction SilentlyContinue | Where-Object { $_.MainWindowHandle -ne 0 } | Select-Object -ExpandProperty Id)
    $process = Start-Process -FilePath $codeCmd -ArgumentList $argumentList -PassThru

    $codeProcess = $null
    for ($index = 0; $index -lt 30; $index++) {
        Start-Sleep -Milliseconds 500
        $candidates = Get-Process Code -ErrorAction SilentlyContinue |
            Where-Object { $_.MainWindowHandle -ne 0 -and $_.Id -notin $before } |
            Sort-Object StartTime -Descending
        if ($candidates) {
            $codeProcess = $candidates | Select-Object -First 1
            break
        }
    }

    if (-not $codeProcess) {
        if ($process -and -not $process.HasExited) {
            Stop-Process -Id $process.Id -Force
        }
        throw "Unable to find VS Code window for $TargetFile"
    }

    [NativeWindow]::ShowWindowAsync($codeProcess.MainWindowHandle, 3) | Out-Null
    [NativeWindow]::SetForegroundWindow($codeProcess.MainWindowHandle) | Out-Null
    Start-Sleep -Milliseconds 1200

    Save-ScaledScreenshot -Path $OutputPath

    Stop-Process -Id $codeProcess.Id -Force
    Start-Sleep -Milliseconds 700
}

$tasks = @(
    @{ file = '01_environment\python_version_management.md'; line = 36; output = '01_environment\images\python_version_management_01.png' },
    @{ file = '01_environment\python_version_management.md'; line = 54; output = '01_environment\images\python_version_management_02.png' },
    @{ file = '01_environment\python_version_management.md'; line = 74; output = '01_environment\images\python_version_management_03.png' },
    @{ file = '01_environment\dependency_management.md'; line = 36; output = '01_environment\images\dependency_management_01.png' },
    @{ file = '01_environment\dependency_management.md'; line = 54; output = '01_environment\images\dependency_management_02.png' },
    @{ file = '01_environment\dependency_management.md'; line = 88; output = '01_environment\images\dependency_management_03.png' },
    @{ file = '01_environment\ide_setup.md'; line = 35; output = '01_environment\images\ide_setup_01.png' },
    @{ file = '01_environment\ide_setup.md'; line = 43; output = '01_environment\images\ide_setup_02.png' },
    @{ file = '01_environment\ide_setup.md'; line = 89; output = '01_environment\images\ide_setup_03.png' },
    @{ file = '02_basic_syntax\variables_and_types.md'; line = 34; output = '02_basic_syntax\images\variables_and_types_01.png' },
    @{ file = '02_basic_syntax\operators_and_expressions.md'; line = 34; output = '02_basic_syntax\images\operators_and_expressions_01.png' },
    @{ file = '02_basic_syntax\control_flow.md'; line = 34; output = '02_basic_syntax\images\control_flow_01.png' },
    @{ file = '02_basic_syntax\strings_and_methods.md'; line = 34; output = '02_basic_syntax\images\strings_and_methods_01.png' },
    @{ file = '02_basic_syntax\collections.md'; line = 34; output = '02_basic_syntax\images\collections_01.png' },
    @{ file = '02_basic_syntax\function_basics.md'; line = 34; output = '02_basic_syntax\images\function_basics_01.png' },
    @{ file = '03_advanced_syntax\iterators_and_generators.md'; line = 34; output = '03_advanced_syntax\images\iterators_and_generators_01.png' },
    @{ file = '03_advanced_syntax\decorators.md'; line = 34; output = '03_advanced_syntax\images\decorators_01.png' },
    @{ file = '03_advanced_syntax\context_managers.md'; line = 34; output = '03_advanced_syntax\images\context_managers_01.png' },
    @{ file = '03_advanced_syntax\object_oriented_programming.md'; line = 34; output = '03_advanced_syntax\images\object_oriented_programming_01.png' },
    @{ file = '03_advanced_syntax\exceptions.md'; line = 34; output = '03_advanced_syntax\images\exceptions_01.png' },
    @{ file = '03_advanced_syntax\modules_and_packages.md'; line = 34; output = '03_advanced_syntax\images\modules_and_packages_01.png' },
    @{ file = '04_progressive_topics\python_re.md'; line = 33; output = '04_progressive_topics\images\python_re_01.png' },
    @{ file = '04_progressive_topics\python_keywords.md'; line = 33; output = '04_progressive_topics\images\python_keywords_01.png' },
    @{ file = '04_progressive_topics\python_concurrency.md'; line = 33; output = '04_progressive_topics\images\python_concurrency_01.png' },
    @{ file = '04_progressive_topics\python_profiling.md'; line = 33; output = '04_progressive_topics\images\python_profiling_01.png' },
    @{ file = '04_progressive_topics\type_hints_and_static_checking.md'; line = 33; output = '04_progressive_topics\images\type_hints_and_static_checking_01.png' },
    @{ file = '04_progressive_topics\testing_pyramid_and_pytest.md'; line = 33; output = '04_progressive_topics\images\testing_pyramid_and_pytest_01.png' },
    @{ file = '04_progressive_topics\packaging_and_publishing.md'; line = 33; output = '04_progressive_topics\images\packaging_and_publishing_01.png' }
)

foreach ($task in $tasks) {
    $targetFile = Join-Path $notesRoot $task.file
    $outputPath = Join-Path $notesRoot $task.output
    Capture-CodeFile -TargetFile $targetFile -LineNumber $task.line -OutputPath $outputPath
}
