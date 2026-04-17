import importlib.metadata
from typing import List, Tuple, Optional

# --- 示例 1: 自动化依赖审计脚本 (Modern importlib.metadata) ---

def check_package_status(package_name: str, min_version: Optional[str] = None) -> Tuple[str, str, bool]:
    """
    检查指定包是否已安装且版本符合最低要求。
    """
    try:
        version = importlib.metadata.version(package_name)
        if min_version:
            # 简单字符串比较，实际生产环境建议用 packaging.version
            is_ok = version >= min_version
        else:
            is_ok = True
        return package_name, version, is_ok
    except importlib.metadata.PackageNotFoundError:
        return package_name, "NOT_INSTALLED", False

# --- 示例 2: 解析 requirements.txt 文件 ---

def parse_requirements(content: str) -> List[str]:
    """
    解析 requirements.txt 内容，过滤注释和空行。
    """
    return [
        line.split('#')[0].strip() 
        for line in content.splitlines() 
        if line.strip() and not line.strip().startswith('#')
    ]

# --- 示例 3: 生成 pyproject.toml 依赖块内容 ---

def generate_poetry_dependency_line(package: str, version: str) -> str:
    """
    生成 Poetry 风格的依赖行。
    """
    return f'{package} = "^{version}"'

if __name__ == "__main__":
    # 验证环境中的关键依赖
    packages = ["pytest", "requests", "non_existent_pkg"]
    for pkg in packages:
        name, ver, ok = check_package_status(pkg)
        print(f"Package: {name:<15} | Version: {ver:<10} | Status: {'[OK]' if ok else '[FAIL]'}")

    # 验证解析器
    reqs = "pytest>=8.0\n# comment\nrequests==2.31.0"
    print(f"Parsed: {parse_requirements(reqs)}")
