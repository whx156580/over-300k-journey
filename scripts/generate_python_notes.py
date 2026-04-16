from __future__ import annotations

from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parent.parent / "testing" / "python_notes"
UPDATED = "2026-04-16"


def md(text: str) -> str:
    cleaned = dedent(text).splitlines()
    normalized = [line[12:] if line.startswith("            ") else line for line in cleaned]
    return "\n".join(normalized).strip() + "\n"


def write(relative_path: str, content: str) -> None:
    path = ROOT / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def front_matter(title: str, level: str, tags: list[str]) -> str:
    tags_text = ", ".join(tags)
    return md(
        f"""
        ---
        title: {title}
        module: testing
        area: python_notes
        stack: python
        level: {level}
        status: active
        tags: [{tags_text}]
        updated: {UPDATED}
        ---
        """
    )


def toc(items: list[str]) -> str:
    lines = ["## 目录"]
    for item in items:
        lines.append(f"- [{item}](#{item})")
    return "\n".join(lines) + "\n"


def code_block(language: str, code: str, info_suffix: str = "") -> str:
    suffix = f" {info_suffix}".rstrip()
    return f"```{language}{suffix}\n{dedent(code).strip()}\n```\n"


def section(title: str, body: str) -> str:
    return f"## {title}\n{body.strip()}\n"


def bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) + "\n"


def numbered_list(items: list[str]) -> str:
    return "\n".join(f"{index}. {item}" for index, item in enumerate(items, start=1)) + "\n"


def render_self_check(items: list[dict[str, str]]) -> str:
    groups = [
        ("概念题", "concept"),
        ("编程题", "coding"),
        ("实战场景", "scenario"),
    ]
    lines: list[str] = ["## Self-Check"]
    for heading, item_type in groups:
        lines.append(f"### {heading}")
        group_items = [item for item in items if item["type"] == item_type]
        for index, item in enumerate(group_items, start=1):
            lines.append(f"{index}. {item['question']}")
        lines.append("")
    lines.append("先独立作答，再对照下方的“参考答案”和对应章节复盘。")
    return "\n".join(lines).rstrip() + "\n"


def render_answers(items: list[dict[str, str]]) -> str:
    lines = ["## 参考答案"]
    counters = {"concept": 0, "coding": 0, "scenario": 0}
    labels = {"concept": "概念题", "coding": "编程题", "scenario": "实战场景"}
    for item in items:
        counters[item["type"]] += 1
        label = labels[item["type"]]
        number = counters[item["type"]]
        lines.append(f"### {label} {number}")
        lines.append(item["answer"])
        lines.append(f"讲解回看: [{item['link_text']}](#{item['link_anchor']})")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def footer() -> str:
    return "---\n[返回 Python 学习总览](../README.md)\n"


def compose_note(
    *,
    title: str,
    level: str,
    tags: list[str],
    toc_items: list[str],
    sections: list[tuple[str, str]],
    checks: list[dict[str, str]],
) -> str:
    parts = [front_matter(title, level, tags), toc(toc_items)]
    for heading, body in sections:
        parts.append(section(heading, body))
    parts.append(render_self_check(checks))
    parts.append(render_answers(checks))
    parts.append(section("参考链接", bullet_list(["[Python 官方文档](https://docs.python.org/3/)", "[本仓库知识模板](../../common/docs/template.md)"])))
    parts.append(section("版本记录", bullet_list([f"{UPDATED}: 初版整理，补齐示例、自测题与落地建议。"])))
    parts.append(footer())
    return "\n".join(parts)


def environment_note(
    *,
    title: str,
    tags: list[str],
    overview: list[str],
    comparison: list[str],
    implementation: str,
    validation: list[str],
    pitfalls: list[str],
    image_inventory: list[str],
    checks: list[dict[str, str]],
) -> str:
    sections = [
        ("为什么要学", bullet_list(overview)),
        ("工具对比", bullet_list(comparison)),
        ("实战步骤", implementation),
        ("验证清单", bullet_list(validation)),
        ("截图清单", bullet_list(image_inventory)),
        ("易错点", bullet_list(pitfalls)),
    ]
    return compose_note(
        title=title,
        level="basics",
        tags=tags,
        toc_items=["为什么要学", "工具对比", "实战步骤", "验证清单", "截图清单", "易错点", "Self-Check", "参考答案", "参考链接", "版本记录"],
        sections=sections,
        checks=checks,
    )


def basic_note(
    *,
    title: str,
    tags: list[str],
    concept: list[str],
    rules: list[str],
    examples: str,
    pitfalls: list[str],
    practice: list[str],
    checks: list[dict[str, str]],
) -> str:
    sections = [
        ("概念", bullet_list(concept)),
        ("语法规则", bullet_list(rules)),
        ("代码示例", examples),
        ("易错点", bullet_list(pitfalls)),
        ("小练习", numbered_list(practice) + "\n完成后再对照“参考答案”和“Self-Check”复盘。"),
    ]
    return compose_note(
        title=title,
        level="basics",
        tags=tags,
        toc_items=["概念", "语法规则", "代码示例", "易错点", "小练习", "Self-Check", "参考答案", "参考链接", "版本记录"],
        sections=sections,
        checks=checks,
    )


def advanced_note(
    *,
    title: str,
    tags: list[str],
    concept: list[str],
    mechanism: list[str],
    examples: str,
    pitfalls: list[str],
    practice: list[str],
    checks: list[dict[str, str]],
) -> str:
    sections = [
        ("概念", bullet_list(concept)),
        ("核心机制", bullet_list(mechanism)),
        ("代码示例", examples),
        ("易错点", bullet_list(pitfalls)),
        ("小练习", numbered_list(practice) + "\n\n建议先手写一遍，再对照“参考答案”检查抽象边界是否清晰。"),
    ]
    return compose_note(
        title=title,
        level="advanced",
        tags=tags,
        toc_items=["概念", "核心机制", "代码示例", "易错点", "小练习", "Self-Check", "参考答案", "参考链接", "版本记录"],
        sections=sections,
        checks=checks,
    )


def progressive_note(
    *,
    title: str,
    tags: list[str],
    why: list[str],
    what: list[str],
    how: str,
    cases: list[str],
    extra_reading: list[str],
    checks: list[dict[str, str]],
) -> str:
    sections = [
        ("为什么学", bullet_list(why)),
        ("学什么", bullet_list(what)),
        ("怎么用", how),
        ("业界案例", bullet_list(cases)),
        ("延伸阅读", bullet_list(extra_reading)),
    ]
    return compose_note(
        title=title,
        level="advanced",
        tags=tags,
        toc_items=["为什么学", "学什么", "怎么用", "业界案例", "延伸阅读", "Self-Check", "参考答案", "参考链接", "版本记录"],
        sections=sections,
        checks=checks,
    )


def build_environment_notes() -> None:
    pyenv_win_cmd = code_block("powershell", r'''
            pip install pyenv-win --user
            setx PYENV "%USERPROFILE%\.pyenv\pyenv-win"
            setx PATH "%USERPROFILE%\.pyenv\pyenv-win\bin;%USERPROFILE%\.pyenv\pyenv-win\shims;%PATH%"
            pyenv install 3.11.9
            pyenv global 3.11.9
            python --version
            '''.strip())
    pyenv_macos_cmd = code_block("bash", r'''
            brew update
            brew install pyenv
            echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
            echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
            echo 'eval "$(pyenv init -)"' >> ~/.zshrc
            exec "$SHELL"
            pyenv install 3.10.14
            pyenv local 3.10.14
            python --version
            '''.strip())
    pyenv_linux_cmd = code_block("bash", r'''
            sudo apt update
            sudo apt install -y build-essential libssl-dev zlib1g-dev \
                libbz2-dev libreadline-dev libsqlite3-dev curl git
            curl https://pyenv.run | bash
            echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
            echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
            echo 'eval "$(pyenv init -)"' >> ~/.bashrc
            source ~/.bashrc
            pyenv install 3.9.19
            pyenv shell 3.9.19
            python --version
            '''.strip())
    venv_cmd = code_block("bash", r'''
            python -m venv .venv
            source .venv/bin/activate
            python -m pip install --upgrade pip
            python -c "import sys; print(sys.prefix)"
            '''.strip())
    env_check_cmd = code_block("python", '''
            import sys
            from pathlib import Path


            def in_virtualenv() -> bool:
                return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


            executable = Path(sys.executable).name
            print(sys.version.split()[0], executable, in_virtualenv())
            '''.strip(), 'hl_lines="5 9"')
    python_version_management = environment_note(
        title="Python 多版本管理：pyenv、venv、conda",
        tags=["python", "environment", "pyenv", "venv", "conda"],
        overview=[
            "测试工程常同时维护老系统和新项目，Python 版本隔离做不好就会出现解释器冲突、依赖污染和脚本不可复现。",
            "掌握 pyenv、venv、conda 的组合关系后，可以做到“全局选版本、项目做隔离、数据科学场景管系统库”。",
            "本节的目标不是背命令，而是建立“版本管理”和“环境隔离”这两层能力的分工意识。",
        ],
        comparison=[
            "`pyenv` 负责安装多个 Python 解释器并按目录切换版本，适合开发机统一管理。",
            "`venv` 是标准库方案，轻量、稳定、对纯 Python 项目足够好。",
            "`conda` 除了装 Python 还能装二进制依赖，更适合数据分析、AI、本地 C/C++ 扩展较多的场景。",
            "常见组合是 `pyenv + venv`；如果团队已经统一到 Anaconda/Miniconda，则优先遵循团队习惯。",
        ],
        implementation=md(
            """
            ### 1. Windows：使用 pyenv-win 管理解释器

            {pyenv_win_cmd}
            逐行说明:
            - 第 1 行安装 `pyenv-win`。
            - 第 2 至 3 行把执行目录和 shim 目录加入环境变量。
            - 第 4 行安装指定版本。
            - 第 5 行设置全局版本。
            - 第 6 行回显当前解释器版本，确认切换生效。

            ### 2. macOS：使用 Homebrew 安装 pyenv

            {pyenv_macos_cmd}
            逐行说明:
            - 第 1 至 2 行安装 pyenv。
            - 第 3 至 5 行把初始化逻辑写入 shell 配置。
            - 第 6 行重新加载 shell。
            - 第 7 至 9 行安装解释器、绑定当前目录版本并验证结果。

            ### 3. Linux：系统依赖 + pyenv

            {pyenv_linux_cmd}
            逐行说明:
            - 第 1 至 2 行安装编译 Python 所需的系统依赖。
            - 第 3 行执行官方安装脚本。
            - 第 4 至 7 行把 pyenv 注入当前 shell。
            - 第 8 至 10 行安装解释器、在当前终端切换版本并验证。

            ### 4. 项目级隔离：venv

            {venv_cmd}
            逐行说明:
            - 第 1 行创建虚拟环境。
            - 第 2 行激活环境；Windows 对应命令是 `.\.venv\\Scripts\\activate`。
            - 第 3 行升级 pip，避免旧版解析器导致安装异常。
            - 第 4 行输出当前环境前缀，用于确认已进入项目环境。

            ### 5. 用 Python 自检当前解释器和虚拟环境

            {env_check_cmd}
            关键行说明:
            - 第 5 行通过 `sys.prefix` 和 `sys.base_prefix` 判断是否处于虚拟环境。
            - 第 9 行输出版本、解释器文件名和布尔结果，适合放到排障脚本里。
            """.format(
                pyenv_win_cmd=pyenv_win_cmd,
                pyenv_macos_cmd=pyenv_macos_cmd,
                pyenv_linux_cmd=pyenv_linux_cmd,
                venv_cmd=venv_cmd,
                env_check_cmd=env_check_cmd,
            )
        ),
        validation=[
            "执行 `python --version`，确认输出与 `pyenv global/local/shell` 设定一致。",
            "执行 `which python` 或 `where python`，检查路径是否落在期望的解释器目录或 `.venv` 目录。",
            "在项目目录执行 `python -c \"import sys; print(sys.prefix)\"`，确认 `venv` 已隔离。",
        ],
        image_inventory=[
            "`images/python_version_management_01.png`: Windows 上配置 pyenv-win 与 PATH 的终端截图。",
            "`images/python_version_management_02.png`: macOS 上使用 `pyenv local` 绑定目录版本的截图。",
            "`images/python_version_management_03.png`: Linux 上编译依赖与切换版本的截图。",
        ],
        pitfalls=[
            "Windows 上只装了 `pyenv-win` 但没有重新打开终端，`pyenv` 命令会提示找不到。",
            "Linux 缺少 `libssl-dev`、`zlib1g-dev` 等系统库时，`pyenv install` 通常会在编译阶段失败。",
            "很多人把 `pyenv` 当成虚拟环境工具使用，结果同一版本的第三方依赖被项目间污染；记住它只负责解释器层。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "`pyenv`、`venv`、`conda` 分别解决哪一层问题？",
                "answer": "`pyenv` 解决解释器版本切换，`venv` 解决项目级纯 Python 依赖隔离，`conda` 额外解决二进制依赖与跨语言包管理。遇到混合场景时先看团队基线，再决定组合方式。",
                "link_text": "工具对比",
                "link_anchor": "工具对比",
            },
            {
                "type": "concept",
                "question": "为什么团队里常推荐 `pyenv + venv` 这组搭配？",
                "answer": "因为它把“安装多个解释器”和“给项目做隔离”拆成两层，职责清晰、迁移成本低，而且完全基于 Python 生态自身能力。",
                "link_text": "为什么要学",
                "link_anchor": "为什么要学",
            },
            {
                "type": "concept",
                "question": "`pyenv local` 和 `pyenv global` 的作用域有什么区别？",
                "answer": "`pyenv global` 设置全局默认版本，影响所有目录；`pyenv local` 只在当前项目目录写入 `.python-version`，更适合仓库级配置。",
                "link_text": "实战步骤",
                "link_anchor": "实战步骤",
            },
            {
                "type": "coding",
                "question": "写一个脚本打印当前 Python 主版本号、可执行文件路径以及是否处于虚拟环境。",
                "answer": "可以直接复用“用 Python 自检当前解释器和虚拟环境”里的示例：`sys.version.split()[0]` 取版本，`sys.executable` 取路径，`sys.prefix != sys.base_prefix` 判断是否处于虚拟环境。",
                "link_text": "实战步骤",
                "link_anchor": "实战步骤",
            },
            {
                "type": "coding",
                "question": "如何让 Windows 下的项目固定使用 Python 3.11，并为仓库创建独立虚拟环境？",
                "answer": "先用 `pyenv install 3.11.x` 安装解释器，再在仓库目录执行 `pyenv local 3.11.x`，随后执行 `python -m venv .venv` 并激活。这样版本和依赖都被项目固定住了。",
                "link_text": "验证清单",
                "link_anchor": "验证清单",
            },
            {
                "type": "scenario",
                "question": "你的 UI 自动化仓库需要在本机同时维护 Python 3.8 和 Python 3.12，应该怎样设计开发机环境？",
                "answer": "优先用 `pyenv` 安装两个解释器，每个仓库用 `pyenv local` 绑定到目标版本，再在项目里各自创建 `.venv`。这样升级某个项目时不会连带影响另一个项目。",
                "link_text": "为什么要学",
                "link_anchor": "为什么要学",
            },
        ],
    )

    pip_init_cmd = code_block("bash", r'''
            python -m venv .venv
            source .venv/bin/activate
            python -m pip install --upgrade pip
            pip install requests pytest
            pip freeze > requirements.txt
            pip install -r requirements.txt
            '''.strip())
    poetry_init_cmd = code_block("bash", r'''
            curl -sSL https://install.python-poetry.org | python3 -
            poetry new demo_project
            cd demo_project
            poetry add requests
            poetry add --group dev pytest black
            poetry install
            poetry run pytest
            '''.strip())
    convert_cmd = code_block("bash", r'''
            poetry export -f requirements.txt --output requirements.txt --without-hashes
            pip install pip-tools
            pip-compile pyproject.toml --output-file requirements.txt
            pip install -r requirements.txt
            '''.strip())
    mirror_cmd = code_block("bash", r'''
            pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
            pip config set install.trusted-host pypi.tuna.tsinghua.edu.cn
            poetry config virtualenvs.in-project true
            poetry config repositories.company https://pypi.example.com/simple/
            '''.strip())
    requirements_check_cmd = code_block("python", '''
            requirements_text = """
            pytest==8.3.2
            requests>=2.32,<3.0
            black==24.8.0
            """.strip()

            parsed = [line for line in requirements_text.splitlines() if line and not line.startswith("#")]
            print(parsed)
            assert "pytest==8.3.2" in parsed
            '''.strip(), 'hl_lines="7 8"')
    dependency_management = environment_note(
        title="pip 与 Poetry 依赖管理",
        tags=["python", "dependency", "pip", "poetry", "packaging"],
        overview=[
            "测试仓库通常既有运行时依赖，也有格式化、静态检查和调试依赖，依赖管理混乱时最先坏掉的往往是 CI。",
            "理解 `requirements.txt`、`constraints.txt`、`pyproject.toml` 与锁文件的分工，能让环境初始化更稳定，也更方便团队协作。",
            "本节重点不是二选一，而是学会在不同项目成熟度下选择 `pip` 或 `Poetry` 的维护方式。",
        ],
        comparison=[
            "`pip` 是默认安装器，简单、兼容性广，适合脚本仓库或已有传统 `requirements.txt` 的项目。",
            "`Poetry` 把依赖声明、版本约束、构建配置统一到 `pyproject.toml`，更适合新项目或需要清晰锁文件的场景。",
            "`requirements.txt` 适合作为部署清单，`pyproject.toml` 更适合作为项目声明文件。",
            "如果团队已经在 CI、部署平台和内部模板里统一使用某一种方案，优先跟随团队基线，减少维护分叉。",
        ],
        implementation=md(
            """
            ### 1. `pip` 初始化与常用命令

            {pip_init_cmd}
            逐行说明:
            - 第 1 至 2 行准备隔离环境。
            - 第 3 行升级 pip。
            - 第 4 行安装业务与测试依赖。
            - 第 5 行冻结当前环境，生成可复现清单。
            - 第 6 行验证清单可被重新安装。

            ### 2. `Poetry` 初始化与常用命令

            {poetry_init_cmd}
            逐行说明:
            - 第 1 行安装 Poetry。
            - 第 2 至 3 行创建项目并进入目录。
            - 第 4 行安装运行时依赖。
            - 第 5 行安装开发依赖。
            - 第 6 行根据锁文件装齐依赖。
            - 第 7 行通过 `poetry run` 在项目环境里执行命令。

            ### 3. `requirements.txt` 与 `pyproject.toml` 的互转

            {convert_cmd}
            逐行说明:
            - 第 1 行把 Poetry 依赖导出为传统清单，便于部署平台复用。
            - 第 2 至 3 行使用 `pip-tools` 从项目声明生成固定依赖。
            - 第 4 行用生成结果恢复环境。

            ### 4. 版本锁定与镜像配置

            {mirror_cmd}
            逐行说明:
            - 前两行给 pip 设置镜像和可信主机，适合网络较慢时提速。
            - 第 3 行让 Poetry 把虚拟环境放在项目目录，降低排障成本。
            - 第 4 行演示如何注册私有源。

            ### 5. 用 Python 解析 requirements 内容

            {requirements_check_cmd}
            关键行说明:
            - 第 7 行过滤空行和注释，适合写依赖检查脚本。
            - 第 8 行用断言保证关键依赖没有丢失。
            """.format(
                pip_init_cmd=pip_init_cmd,
                poetry_init_cmd=poetry_init_cmd,
                convert_cmd=convert_cmd,
                mirror_cmd=mirror_cmd,
                requirements_check_cmd=requirements_check_cmd,
            )
        ),
        validation=[
            "在空目录里执行 `pip install -r requirements.txt`，确认可以一次性装齐依赖。",
            "执行 `poetry lock --no-update` 或 `poetry install`，确认锁文件和依赖声明一致。",
            "在 CI 中固定使用 `requirements.txt` 或 `poetry.lock`，避免开发机和流水线使用不同来源。",
        ],
        image_inventory=[
            "`images/dependency_management_01.png`: `pip freeze` 与 `requirements.txt` 生成过程截图。",
            "`images/dependency_management_02.png`: Poetry 初始化、添加依赖与锁文件变化截图。",
            "`images/dependency_management_03.png`: 镜像配置和私有源配置示意图。",
        ],
        pitfalls=[
            "只提交 `pyproject.toml` 不提交 `poetry.lock`，会导致不同机器解析出不同依赖树。",
            "把 `pip freeze` 的结果直接当成长期维护清单，容易把临时工具和无关依赖一起固化进去。",
            "镜像配置后忘了同步到 CI，结果本地能装、流水线超时失败。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "`requirements.txt`、`pyproject.toml`、锁文件三者的职责分别是什么？",
                "answer": "`requirements.txt` 更像可安装清单，`pyproject.toml` 是项目声明，锁文件记录被解析后的精确依赖树。三者一起用时，声明文件描述意图，锁文件保证复现，部署清单方便执行。",
                "link_text": "工具对比",
                "link_anchor": "工具对比",
            },
            {
                "type": "concept",
                "question": "为什么新项目常更推荐 Poetry，而不是只靠 `pip freeze`？",
                "answer": "因为 Poetry 把依赖声明、分组、构建元数据和锁文件管理统一起来，更适合长期维护；`pip freeze` 更像当前环境快照，表达能力弱。",
                "link_text": "为什么要学",
                "link_anchor": "为什么要学",
            },
            {
                "type": "concept",
                "question": "什么情况下 `pip` 仍然是更合适的选择？",
                "answer": "脚本仓库、历史项目、部署平台只认 `requirements.txt`，或团队已有完整 `pip + constraints` 规范时，继续使用 `pip` 往往成本更低。",
                "link_text": "工具对比",
                "link_anchor": "工具对比",
            },
            {
                "type": "coding",
                "question": "如何从 Poetry 项目导出部署用 `requirements.txt`？",
                "answer": "执行 `poetry export -f requirements.txt --output requirements.txt --without-hashes`。如果部署平台不理解 Poetry，这一步非常常见。",
                "link_text": "实战步骤",
                "link_anchor": "实战步骤",
            },
            {
                "type": "coding",
                "question": "如何快速检查一个 `requirements.txt` 文本里是否包含 `pytest`？",
                "answer": "可以像本节示例一样按行切分、过滤空行，再用 `any(line.startswith(\"pytest\"))` 或 `\"pytest==...\" in parsed` 做断言。",
                "link_text": "实战步骤",
                "link_anchor": "实战步骤",
            },
            {
                "type": "scenario",
                "question": "团队里既有老仓库，也准备启动一个新的 Python 自动化项目，该如何选择依赖管理策略？",
                "answer": "老仓库优先延续现有 `requirements.txt`，减少迁移风险；新仓库可直接使用 Poetry 或 `pip-tools + pyproject.toml`，同时在 CI 里统一锁文件与导出策略。",
                "link_text": "验证清单",
                "link_anchor": "验证清单",
            },
        ],
    )

    ide_setup = environment_note(
        title="VS Code + Pylance + Black + isort + flake8 一体化配置",
        tags=["python", "vscode", "pylance", "black", "flake8"],
        overview=[
            "写测试代码时，问题往往不是“不会写”，而是跳转、提示、格式化、调试和静态检查没有串起来。",
            "把 VS Code 调整成“保存即格式化、写代码就有类型提示、点调试就能进断点”的状态，能显著降低学习成本。",
            "本节的目标是形成一套仓库可复制的 `.vscode` 模板，而不是只在个人电脑里临时点选配置。",
        ],
        comparison=[
            "`Pylance` 提供类型推断、跳转与补全，是 VS Code 里 Python 开发体验的核心。",
            "`Black` 负责无争议格式化，`isort` 负责导入排序，`flake8` 负责最基础的规范和语法风险检查。",
            "调试配置最好和仓库一起提交，这样新成员拉下代码就能直接复用。",
        ],
        implementation=md(
            f"""
            ### 1. 安装扩展

            - Python
            - Pylance
            - Black Formatter
            - isort
            - Flake8

            ### 2. 推荐的 `.vscode/settings.json`

            {code_block("json", '''
            {
              "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
              "editor.formatOnSave": true,
              "editor.codeActionsOnSave": {
                "source.organizeImports": "explicit"
              },
              "python.analysis.typeCheckingMode": "basic",
              "python.analysis.autoImportCompletions": true,
              "editor.defaultFormatter": "ms-python.black-formatter",
              "flake8.args": ["--max-line-length=88"],
              "isort.args": ["--profile", "black"]
            }
            ''')}
            关键字段说明:
            - `python.defaultInterpreterPath`: 固定工作区解释器。
            - `editor.formatOnSave`: 保存时自动格式化。
            - `source.organizeImports`: 保存时触发 import 排序。
            - `python.analysis.typeCheckingMode`: 推荐从 `basic` 起步，再逐步切到 `strict`。

            ### 3. 推荐的 `.vscode/launch.json`

            {code_block("json", '''
            {
              "version": "0.2.0",
              "configurations": [
                {
                  "name": "Python: Current File",
                  "type": "python",
                  "request": "launch",
                  "program": "${file}",
                  "console": "integratedTerminal",
                  "justMyCode": true
                }
              ]
            }
            ''')}
            字段说明:
            - `program`: 当前打开的文件。
            - `console`: 在集成终端执行，便于观察标准输出。
            - `justMyCode`: 默认只调试业务代码，先降低干扰。

            ### 4. 断点调试示范

            {code_block("python", '''
            def divide(total: int, count: int) -> float:
                if count == 0:
                    raise ValueError("count must not be zero")
                return total / count


            if __name__ == "__main__":
                result = divide(42, 6)
                print(result)
            '''.strip(), 'hl_lines="2 4 8"')}
            调试建议:
            - 在第 2 行与第 8 行打断点，观察参数、返回值和异常分支。
            - 如果你要调试 Pytest，用 `module: pytest` 的配置比直接跑脚本更方便。

            ### 5. 用 Python 生成一份 settings 模板

            {code_block("python", '''
            import json

            settings = {
                "editor.formatOnSave": True,
                "python.analysis.typeCheckingMode": "basic",
                "editor.defaultFormatter": "ms-python.black-formatter",
            }

            print(json.dumps(settings, ensure_ascii=False, indent=2))
            assert settings["editor.formatOnSave"] is True
            '''.strip(), 'hl_lines="3 9"')}
            关键行说明:
            - 第 3 至 7 行演示如何在脚本里生成配置片段。
            - 第 9 行可作为初始化脚本的最小验收断言。
            """
        ),
        validation=[
            "打开任意 Python 文件，保存时确认 Black 和 isort 自动生效。",
            "故意写一个未使用变量或语法错误，确认 Flake8/Pylance 能在编辑器里直接提示。",
            "按 `F5` 启动当前文件调试，确认断点命中、变量面板可查看局部变量。",
        ],
        image_inventory=[
            "`images/ide_setup_01.png`: VS Code 扩展安装与解释器选择界面截图。",
            "`images/ide_setup_02.png`: `.vscode/settings.json` 配置与保存即格式化效果截图。",
            "`images/ide_setup_03.png`: `launch.json` 断点调试过程截图。",
        ],
        pitfalls=[
            "解释器路径写死为类 Unix 路径后，Windows 成员打开仓库会提示找不到 Python；需要按团队平台选择模板或使用变量。",
            "同时启用多个 Formatter 会导致保存时格式来回抖动，最后很难定位是谁在改文件。",
            "`flake8`、`black`、`isort` 版本不一致时，常出现“格式化通过但 lint 失败”的现象，最好在仓库里锁版本。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "为什么推荐把 `.vscode/settings.json` 和 `launch.json` 一起提交到仓库？",
                "answer": "因为它们属于团队开发体验的一部分。把它们跟代码一起版本化，能让新成员拉库后立刻获得统一的格式化、提示和调试行为。",
                "link_text": "为什么要学",
                "link_anchor": "为什么要学",
            },
            {
                "type": "concept",
                "question": "`Pylance`、`Black`、`flake8` 各自解决什么问题？",
                "answer": "`Pylance` 负责智能提示与类型分析，`Black` 负责代码格式统一，`flake8` 负责基础规范和语法风险检查。它们互补而不是互相替代。",
                "link_text": "工具对比",
                "link_anchor": "工具对比",
            },
            {
                "type": "concept",
                "question": "`basic` 类型检查模式为什么适合作为起点？",
                "answer": "因为它能先暴露明显类型问题，又不会像 `strict` 那样一下子引入过多告警，适合学习阶段和存量项目渐进接入。",
                "link_text": "实战步骤",
                "link_anchor": "实战步骤",
            },
            {
                "type": "coding",
                "question": "如何让保存文件时自动排序 import 并运行 Black？",
                "answer": "在 `settings.json` 中开启 `editor.formatOnSave`，并在 `editor.codeActionsOnSave` 里设置 `source.organizeImports`，同时把默认格式化器指向 `ms-python.black-formatter`。",
                "link_text": "实战步骤",
                "link_anchor": "实战步骤",
            },
            {
                "type": "coding",
                "question": "如何验证当前工作区是否真的在使用 `.venv` 里的解释器？",
                "answer": "可以在终端运行 `python -c \"import sys; print(sys.executable)\"`，也可以直接在 VS Code 右下角查看当前解释器路径是否落在 `.venv` 中。",
                "link_text": "验证清单",
                "link_anchor": "验证清单",
            },
            {
                "type": "scenario",
                "question": "团队里有人保存代码会自动格式化，有人不会，最终 PR 里全是无意义 diff，怎么收敛？",
                "answer": "把 `.vscode` 模板、`requirements.txt` 和 CI 检查一起提交。开发机靠格式化器降低成本，CI 用 `black --check` 和 `flake8` 执行兜底，形成统一闭环。",
                "link_text": "验证清单",
                "link_anchor": "验证清单",
            },
        ],
    )

    write("01_environment/python_version_management.md", python_version_management)
    write("01_environment/dependency_management.md", dependency_management)
    write("01_environment/ide_setup.md", ide_setup)


def build_basic_notes() -> None:
    variables_and_types = basic_note(
        title="变量与数据类型",
        tags=["python", "variables", "types", "identity", "annotations"],
        concept=[
            "Python 是动态类型语言，变量名绑定的是对象引用，不是提前声明好的内存槽位。",
            "“强类型”表示不会在运行时偷偷把 `\"1\"` 当作数字 `1` 用；类型不匹配时会明确抛错。",
            "类型标注主要服务于阅读、补全和静态检查，不会在运行时自动替你做类型转换。",
        ],
        rules=[
            "给变量赋值时，左边是名字，右边是对象；重新赋值本质上是让名字指向另一个对象。",
            "`==` 比较值是否相等，`is` 比较是否是同一个对象，判断 `None` 时优先使用 `is None`。",
            "常见内置类型包括 `int`、`float`、`bool`、`str`、`list`、`tuple`、`dict`、`set`。",
            "类型标注写法常见为 `name: str = \"alice\"`，函数签名可写成 `def add(a: int, b: int) -> int:`。",
        ],
        examples=md(
            f"""
            ### 示例 1：动态类型与类型标注

            {code_block("python", '''
            age: int = 28
            nickname = "qa_runner"
            is_active = True

            print(type(age).__name__, type(nickname).__name__, type(is_active).__name__)
            '''.strip(), 'hl_lines="1 4"')}
            示例要点:
            - 第 1 行展示变量注解。
            - 第 4 行验证运行时真实类型。

            ### 示例 2：`is` 与 `==`

            {code_block("python", '''
            left = [1, 2, 3]
            right = [1, 2, 3]
            alias = left

            print(left == right)
            print(left is right)
            print(left is alias)
            '''.strip(), 'hl_lines="5 6 7"')}
            示例要点:
            - 第 5 行比较值。
            - 第 6 至 7 行比较对象身份。

            ### 示例 3：`None` 判断

            {code_block("python", '''
            def format_user(name: str | None) -> str:
                if name is None:
                    return "anonymous"
                return name.strip().lower()


            print(format_user(None))
            print(format_user("  Alice  "))
            '''.strip(), 'hl_lines="2 3"')}
            """
        ),
        pitfalls=[
            "把 `is` 当作通用相等比较符，结果在列表、字典、长字符串上得到错误结论。",
            "误以为类型标注会自动帮你转换类型；实际上传入字符串仍然会在业务逻辑里爆错。",
            "在调试时只看变量名、不看 `type()` 和 `id()`，很容易把“值相同”和“对象相同”混为一谈。",
        ],
        practice=[
            "定义一个函数，接收 `str | None`，输入 `None` 时返回默认用户名，其他情况返回去除空白后的结果。",
            "创建两个值相同但不是同一对象的列表，分别打印 `==` 和 `is` 的结果。",
            "用类型标注定义一个 `dict[str, int]`，统计测试结果中 `passed` 与 `failed` 的数量。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "为什么说 Python 既是动态类型语言，又是强类型语言？",
                "answer": "动态类型指变量不需要预先声明类型，运行时再绑定对象；强类型指类型不兼容时不会悄悄转换，而是显式报错。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
            {
                "type": "concept",
                "question": "`is` 与 `==` 应该分别在什么场景下使用？",
                "answer": "`==` 用于比较值是否相等，`is` 用于判断是否是同一个对象。判断 `None`、单例对象时优先使用 `is`。",
                "link_text": "语法规则",
                "link_anchor": "语法规则",
            },
            {
                "type": "concept",
                "question": "类型标注在团队协作中最大的价值是什么？",
                "answer": "它提升可读性、补全质量和静态检查能力，让函数边界更清楚，尤其适合多人维护的测试代码和工具脚本。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
            {
                "type": "coding",
                "question": "写一个函数，传入 `None` 返回 `\"guest\"`，否则返回小写用户名。",
                "answer": "可以参考示例 3：在函数入口用 `if name is None` 处理空值，其他情况对字符串做 `strip().lower()` 再返回。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "coding",
                "question": "怎样打印两个变量是否指向同一个对象？",
                "answer": "直接打印 `a is b`。如果还要进一步排查，可配合 `id(a)` 和 `id(b)` 观察内存身份标识。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "scenario",
                "question": "接口测试里从 JSON 里取到的 `id` 有时是字符串、有时是整数，应该如何处理？",
                "answer": "不要依赖隐式转换。应在解析边界统一做类型归一化，例如通过显式转换、类型校验或 Pydantic 模型约束，再把内部使用类型固定下来。",
                "link_text": "易错点",
                "link_anchor": "易错点",
            },
        ],
    )

    operators_and_expressions = basic_note(
        title="运算符与表达式",
        tags=["python", "operators", "expressions", "comparison", "bitwise"],
        concept=[
            "表达式是会产生值的代码片段，运算符决定这些值如何组合与计算。",
            "理解优先级、结合性和短路逻辑，比记忆所有符号本身更重要。",
            "位运算在权限标记、状态位、二进制协议解析中很常见，测试工程里也会遇到。",
        ],
        rules=[
            "算术、比较、逻辑和位运算都能出现在同一个表达式中，但复杂表达式建议加括号增强可读性。",
            "链式比较 `a < b < c` 会按数学语义求值，中间值只求一次。",
            "`and`、`or` 具有短路特性，左侧已经足够决定结果时，右侧不会执行。",
            "`&`、`|`、`^`、`~`、`<<`、`>>` 作用于整数的二进制位，不要与 `and`、`or` 混用。",
        ],
        examples=md(
            f"""
            ### 示例 1：链式比较

            {code_block("python", '''
            score = 85
            result = 60 <= score < 90
            print(result)
            '''.strip(), 'hl_lines="2"')}

            ### 示例 2：短路逻辑

            {code_block("python", '''
            def expensive_check() -> bool:
                print("expensive_check called")
                return True


            print(False and expensive_check())
            print(True or expensive_check())
            '''.strip(), 'hl_lines="6 7"')}
            观察结果:
            - 这段代码不会打印 `expensive_check called`，因为两次都被短路了。

            ### 示例 3：位运算

            {code_block("python", '''
            READ = 0b001
            WRITE = 0b010
            EXECUTE = 0b100

            permission = READ | WRITE
            print(permission)
            print(permission & WRITE == WRITE)
            print(permission & EXECUTE == EXECUTE)
            '''.strip(), 'hl_lines="5 7 8"')}
            """
        ),
        pitfalls=[
            "把 `&` 当成逻辑与使用，尤其在布尔表达式里会让代码读起来非常危险。",
            "链式比较里夹带副作用函数虽然能运行，但会降低可读性，排查起来也困难。",
            "依赖 `and/or` 返回布尔值时容易踩坑，因为它们返回的是“最后一个被求值的对象”，不一定是 `True/False`。",
        ],
        practice=[
            "写一个表达式，判断温度是否处于 `[18, 26)` 区间。",
            "定义 `ADMIN = 0b1000`、`EDITOR = 0b0100`，计算同时拥有两个权限的结果。",
            "写一个函数，只有当 `debug` 为 `True` 时才调用代价较高的诊断函数。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "什么是链式比较，它和 `a < b and b < c` 有什么差异？",
                "answer": "链式比较写成 `a < b < c`，语义更接近数学表达式，而且中间值只求一次，可读性通常也更好。",
                "link_text": "语法规则",
                "link_anchor": "语法规则",
            },
            {
                "type": "concept",
                "question": "`and`、`or` 的短路机制有什么价值？",
                "answer": "它可以避免不必要的计算，也常用于“前置条件通过后再执行昂贵逻辑”的场景，比如对象判空和延迟调用。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "concept",
                "question": "位运算最典型的工程用途是什么？",
                "answer": "它常用于权限标记、状态位组合、协议解析、硬件寄存器控制等需要紧凑表达多个开关状态的场景。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
            {
                "type": "coding",
                "question": "如何判断一个整数权限集中是否包含 `WRITE` 位？",
                "answer": "使用按位与：`permission & WRITE == WRITE`。先取交集，再判断目标位是否完整保留。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "coding",
                "question": "怎样写一个不会触发昂贵函数调用的布尔判断？",
                "answer": "把廉价条件写在左侧，例如 `debug and expensive_check()`。当 `debug` 为 `False` 时，右侧不会执行。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "scenario",
                "question": "日志分析脚本里有一个 `parse()` 很慢，只在文件存在时才需要调用，表达式该怎么写？",
                "answer": "可写成 `path.exists() and parse(path)`。这样文件不存在时就不会进入解析逻辑，同时表达式仍然保持简洁。",
                "link_text": "易错点",
                "link_anchor": "易错点",
            },
        ],
    )

    control_flow = basic_note(
        title="流程控制",
        tags=["python", "flow-control", "if", "while", "for"],
        concept=[
            "流程控制决定代码按什么条件执行、重复执行以及何时提前退出。",
            "写流程控制时，关键不是“语法会不会写”，而是条件边界是否清晰、循环是否可终止。",
            "`for-else` 与 `while-else` 是 Python 里常被忽略但非常实用的结构。",
        ],
        rules=[
            "`if/elif/else` 按顺序匹配第一个满足条件的分支。",
            "`while` 适合“满足条件就继续”的场景，循环变量必须能趋近结束条件。",
            "`for` 适合遍历可迭代对象，配合 `range()` 能完成绝大多数计数循环。",
            "`break` 会提前结束循环，`continue` 会跳过本轮剩余逻辑，`else` 只会在循环未被 `break` 打断时执行。",
        ],
        examples=md(
            f"""
            ### 示例 1：条件分支

            {code_block("python", '''
            response_time = 320

            if response_time < 200:
                level = "fast"
            elif response_time < 500:
                level = "acceptable"
            else:
                level = "slow"

            print(level)
            '''.strip(), 'hl_lines="3 5 7"')}

            ### 示例 2：`for` + `range`

            {code_block("python", '''
            total = 0
            for number in range(1, 6):
                total += number
            print(total)
            '''.strip(), 'hl_lines="2 3"')}

            ### 示例 3：`for-else`

            {code_block("python", '''
            users = ["alice", "bob", "charlie"]

            for user in users:
                if user == "dora":
                    print("found")
                    break
            else:
                print("not found")
            '''.strip(), 'hl_lines="3 6 8"')}
            """
        ),
        pitfalls=[
            "`while True` 写得很顺手，但如果没有清晰退出条件，就很容易写出死循环。",
            "在遍历列表时直接删除元素，会改变索引和长度，常导致漏处理数据。",
            "很多人把 `for-else` 误解成“循环结束后总会执行 else”，其实只有没有被 `break` 打断时才会进 else。",
        ],
        practice=[
            "遍历 1 到 20，打印所有能被 3 整除但不能被 2 整除的数字。",
            "写一个 `while` 循环，把字符串列表中长度小于 3 的元素过滤掉。",
            "使用 `for-else` 判断某个用户名是否存在于用户列表里。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "`for` 和 `while` 的选择标准是什么？",
                "answer": "当你知道要遍历一个集合或固定次数时优先用 `for`；当循环是否继续取决于动态条件时用 `while` 更自然。",
                "link_text": "语法规则",
                "link_anchor": "语法规则",
            },
            {
                "type": "concept",
                "question": "`for-else` 的 `else` 到底在什么时候执行？",
                "answer": "只有循环正常结束且没有触发 `break` 时才执行；如果提前 `break`，`else` 不会运行。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "concept",
                "question": "为什么流程控制里要特别关注“终止条件”？",
                "answer": "因为边界不清晰时最常见的问题就是死循环、漏处理和分支覆盖不完整，这些都会直接影响测试脚本稳定性。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
            {
                "type": "coding",
                "question": "怎样用 `range()` 遍历 0 到 8 的偶数？",
                "answer": "使用 `range(0, 10, 2)`。起点是 0，终点不包含 10，步长为 2。",
                "link_text": "语法规则",
                "link_anchor": "语法规则",
            },
            {
                "type": "coding",
                "question": "如何在遍历列表时安全过滤元素？",
                "answer": "优先创建新列表，例如列表推导式或结果列表累加，避免在遍历原列表时直接删除元素。",
                "link_text": "易错点",
                "link_anchor": "易错点",
            },
            {
                "type": "scenario",
                "question": "你在轮询接口状态，直到任务完成或超时，该用什么流程结构更合适？",
                "answer": "通常用 `while`，因为是否继续轮询取决于接口返回状态和超时阈值。循环里应显式维护重试次数或截止时间。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
        ],
    )

    strings_slice_cmd = code_block("python", '''
            text = "playwright"
            print(text[:4])
            print(text[4:])
            print(text[::-1])
            '''.strip(), 'hl_lines="2 3 4"')
    strings_format_cmd = code_block("python", '''
            suite = "api"
            passed = 18
            failed = 2
            summary = f"{suite=} {passed=} {failed=}"
            print(summary)
            '''.strip(), 'hl_lines="4"')
    strings_raw_cmd = code_block("python", '''
            windows_path = r"C:\\Users\\qa\\project"
            doc = """Line 1
            Line 2
            Line 3"""

            print(windows_path.endswith("project"))
            print(doc.splitlines()[1].strip())
            '''.strip(), 'hl_lines="1 2 6 7"')
    strings_and_methods = basic_note(
        title="字符串与常用方法",
        tags=["python", "string", "f-string", "slice", "raw-string"],
        concept=[
            "字符串是不可变序列，绝大多数处理操作都会返回新字符串。",
            "切片、格式化与文本清洗是测试工程里最常见的字符串能力，比如日志处理、接口报文验证、文件路径处理。",
            "理解普通字符串、原始字符串、三引号字符串的边界，有助于减少转义错误。",
        ],
        rules=[
            "切片写法为 `text[start:stop:step]`，左闭右开。",
            "推荐优先使用 f-string 做字符串插值，可读性和性能通常都更好。",
            "原始字符串 `r\"...\"` 对正则、Windows 路径尤其友好，但末尾不能只有一个反斜杠。",
            "三引号字符串适合多行文本、SQL、文档字符串和复杂报文样例。",
        ],
        examples=md(
            """
            ### 示例 1：切片

            {strings_slice_cmd}

            ### 示例 2：f-string 与格式化

            {strings_format_cmd}

            ### 示例 3：原始字符串与三引号

            {strings_raw_cmd}
            """.format(
                strings_slice_cmd=strings_slice_cmd,
                strings_format_cmd=strings_format_cmd,
                strings_raw_cmd=strings_raw_cmd,
            )
        ),
        pitfalls=[
            "误以为字符串是可变对象，直接按索引赋值会报错。",
            "原始字符串末尾单独放一个 `\\` 会导致语法错误，因为转义仍然影响结束引号。",
            "在多层引号嵌套里忽略转义和引号配对，最容易让长 SQL 或 JSON 文本难以维护。",
        ],
        practice=[
            "从 URL `https://example.com/orders/123` 中切出最后的订单号。",
            "用 f-string 生成一条包含环境名、通过数、失败数的测试摘要。",
            "写一个三引号字符串，保存一段 JSON 报文模板，并打印第二行内容。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "为什么说字符串切片是左闭右开？",
                "answer": "因为 `start` 位置会被包含，`stop` 位置不会被包含，这和 `range()` 的规则一致，有助于组合与计算长度。",
                "link_text": "语法规则",
                "link_anchor": "语法规则",
            },
            {
                "type": "concept",
                "question": "为什么推荐优先用 f-string？",
                "answer": "它更直观、可读性更高，也更容易就地展示变量名和值，非常适合调试输出和测试报告摘要。",
                "link_text": "语法规则",
                "link_anchor": "语法规则",
            },
            {
                "type": "concept",
                "question": "原始字符串最适合什么场景？",
                "answer": "适合包含大量反斜杠的文本，如正则表达式、Windows 路径、转义字符较多的模板。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
            {
                "type": "coding",
                "question": "如何把字符串倒序输出？",
                "answer": "使用切片 `text[::-1]`。步长为 `-1` 会从尾到头遍历字符串。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "coding",
                "question": "怎样写一个包含多行内容的文档字符串？",
                "answer": "使用三引号字符串 `\"\"\"...\"\"\"` 或 `'''...'''`。如果在函数定义下方，解释器还会把它识别为 docstring。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "scenario",
                "question": "你要解析 Windows 文件路径和正则表达式，为什么 raw-string 能明显降低出错率？",
                "answer": "因为它减少了反斜杠转义层数，路径或正则会更接近原始写法，代码更容易审查，也不容易漏写转义。",
                "link_text": "易错点",
                "link_anchor": "易错点",
            },
        ],
    )

    collections = basic_note(
        title="列表、元组、集合、字典",
        tags=["python", "list", "tuple", "set", "dict"],
        concept=[
            "列表适合有序可变数据，元组适合不可变记录，集合适合去重与集合运算，字典适合键值映射。",
            "选择容器类型时，先想数据是否需要保持顺序、是否允许重复、是否需要按键快速查找。",
            "推导式让常见转换与过滤操作更紧凑，但表达式过长时仍然应该拆开写。",
        ],
        rules=[
            "列表常用 `append`、`extend`、`pop`；字典常用 `get`、`update`、`items`。",
            "元组一旦创建不可修改，适合表达“不会变”的结构化数据。",
            "集合天然去重，支持交集 `&`、并集 `|`、差集 `-`。",
            "字典基于哈希表实现，按键查找通常是 O(1) 平均复杂度。",
        ],
        examples=md(
            f"""
            ### 示例 1：列表与推导式

            {code_block("python", '''
            raw_scores = [60, 72, 88, 91]
            passed_scores = [score for score in raw_scores if score >= 60]
            doubled = [score * 2 for score in raw_scores]

            print(passed_scores)
            print(doubled)
            '''.strip(), 'hl_lines="2 3"')}

            ### 示例 2：集合去重与交集

            {code_block("python", '''
            api_cases = {"login", "logout", "order"}
            ui_cases = {"login", "dashboard"}

            print(api_cases & ui_cases)
            print(api_cases | ui_cases)
            '''.strip(), 'hl_lines="4 5"')}

            ### 示例 3：字典增删改查

            {code_block("python", '''
            report = {"passed": 18, "failed": 2}
            report["skipped"] = 1
            report["failed"] += 1
            failed = report.get("failed", 0)

            print(report)
            print(failed)
            '''.strip(), 'hl_lines="2 3 4"')}
            """
        ),
        pitfalls=[
            "把默认参数写成空列表或空字典，会让多个调用共享同一份可变对象。",
            "误以为集合有稳定顺序，结果在断言展示或导出时得到不一致顺序。",
            "在推导式里塞太多逻辑会让代码变短但更难读，复杂条件宁可拆成普通循环。",
        ],
        practice=[
            "把一组用户名去重后按字母顺序输出。",
            "统计测试结果列表中每种状态出现的次数，并保存到字典里。",
            "写一个列表推导式，筛选出所有偶数并计算平方。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "什么时候应该优先使用集合而不是列表？",
                "answer": "当你更关心“是否存在”和“去重”而不是顺序时，应优先使用集合，因为查找和集合运算更自然也更高效。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
            {
                "type": "concept",
                "question": "为什么字典适合做测试结果统计？",
                "answer": "因为它能通过键快速累加状态、场景名或接口名对应的计数，写法直观，查找成本也低。",
                "link_text": "语法规则",
                "link_anchor": "语法规则",
            },
            {
                "type": "concept",
                "question": "元组和列表最核心的区别是什么？",
                "answer": "元组不可变，更适合表达固定结构；列表可变，更适合追加、删除和批量处理。",
                "link_text": "语法规则",
                "link_anchor": "语法规则",
            },
            {
                "type": "coding",
                "question": "怎样快速得到两个测试集名称的交集？",
                "answer": "把它们转成集合后做 `set_a & set_b`。这比手工双重循环更简洁也更高效。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "coding",
                "question": "如何安全地从字典读取可能不存在的键？",
                "answer": "使用 `dict.get(key, default)`。这样即使键不存在也不会抛 `KeyError`。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "scenario",
                "question": "你要统计失败用例的标签分布，同时还要快速判断标签是否已出现，选哪种容器组合更合适？",
                "answer": "可用字典做计数，必要时配合集合记录已见标签。字典负责累加，集合负责快速成员检查，职责清晰。",
                "link_text": "易错点",
                "link_anchor": "易错点",
            },
        ],
    )

    function_basics = basic_note(
        title="函数基础",
        tags=["python", "function", "scope", "legb", "kwargs"],
        concept=[
            "函数用于封装可复用逻辑，是测试代码从脚本化迈向工程化的第一步。",
            "理解参数传递和作用域，比记忆 `*args`、`**kwargs` 的符号本身更重要。",
            "一个好函数应该有清晰输入、稳定输出和单一职责。",
        ],
        rules=[
            "`def` 用于定义函数，`return` 决定返回值；未显式返回时默认返回 `None`。",
            "作用域查找遵循 LEGB：Local、Enclosing、Global、Built-in。",
            "默认参数在函数定义时求值，可变默认参数要格外小心。",
            "`*args` 接收额外位置参数，`**kwargs` 接收额外关键字参数。",
        ],
        examples=md(
            f"""
            ### 示例 1：默认参数与关键字参数

            {code_block("python", '''
            def build_url(host: str, path: str = "/health", *, https: bool = True) -> str:
                scheme = "https" if https else "http"
                return f"{scheme}://{host}{path}"


            print(build_url("example.com"))
            print(build_url("localhost:8000", path="/docs", https=False))
            '''.strip(), 'hl_lines="1 2"')}

            ### 示例 2：`*args` 与 `**kwargs`

            {code_block("python", '''
            def collect(*args: int, **kwargs: str) -> tuple[int, dict[str, str]]:
                return sum(args), kwargs


            total, meta = collect(1, 2, 3, env="test", owner="qa")
            print(total)
            print(meta["env"])
            '''.strip(), 'hl_lines="1 4"')}

            ### 示例 3：LEGB 作用域

            {code_block("python", '''
            label = "global"


            def outer() -> str:
                label = "enclosing"

                def inner() -> str:
                    return label

                return inner()


            print(outer())
            print(label)
            '''.strip(), 'hl_lines="5 6 11 12"')}
            """
        ),
        pitfalls=[
            "把空列表、空字典当作默认参数，会让多次调用共享状态。",
            "函数职责过多时，参数会越堆越多，最后很难测试、也很难复用。",
            "滥用 `**kwargs` 会让函数边界不清晰，调用者也不容易知道真正需要哪些参数。",
        ],
        practice=[
            "写一个函数，接收主机名和路径，返回完整 URL，并支持关键字参数控制协议。",
            "写一个函数，接收任意数量的数字并返回总和。",
            "通过嵌套函数演示 LEGB 查找顺序。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "LEGB 规则的四层作用域分别是什么？",
                "answer": "Local、Enclosing、Global、Built-in。解释器会按这个顺序查找名称绑定。",
                "link_text": "语法规则",
                "link_anchor": "语法规则",
            },
            {
                "type": "concept",
                "question": "为什么可变默认参数容易出问题？",
                "answer": "因为默认参数在函数定义时只求值一次，后续调用会共享同一个对象，导致状态泄漏。",
                "link_text": "易错点",
                "link_anchor": "易错点",
            },
            {
                "type": "concept",
                "question": "`*args` 和 `**kwargs` 各自适合什么场景？",
                "answer": "`*args` 适合位置参数数量不固定的场景，`**kwargs` 适合附加命名参数或配置透传场景，但要避免滥用。",
                "link_text": "语法规则",
                "link_anchor": "语法规则",
            },
            {
                "type": "coding",
                "question": "如何定义一个必须用关键字传入的参数？",
                "answer": "在函数签名中放一个 `*`，其后的参数都必须用关键字形式调用，例如 `def f(a, *, debug=False)`。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "coding",
                "question": "怎么重写一个带空列表默认参数的函数？",
                "answer": "把默认值改成 `None`，函数内部再写 `items = [] if items is None else items`，避免多次调用共享同一列表。",
                "link_text": "易错点",
                "link_anchor": "易错点",
            },
            {
                "type": "scenario",
                "question": "你在封装 HTTP 请求辅助函数时，想兼容额外 headers、timeout、params，签名该如何设计？",
                "answer": "优先显式声明核心参数，再用少量关键字参数补充扩展项。只有在透传第三方 SDK 参数时，才谨慎使用 `**kwargs`。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
        ],
    )

    write("02_basic_syntax/variables_and_types.md", variables_and_types)
    write("02_basic_syntax/operators_and_expressions.md", operators_and_expressions)
    write("02_basic_syntax/control_flow.md", control_flow)
    write("02_basic_syntax/strings_and_methods.md", strings_and_methods)
    write("02_basic_syntax/collections.md", collections)
    write("02_basic_syntax/function_basics.md", function_basics)


def build_advanced_notes() -> None:
    iterators_and_generators = advanced_note(
        title="迭代器、生成器与 yield/send/throw/close",
        tags=["python", "iterator", "generator", "yield", "coroutine"],
        concept=[
            "迭代器协议让对象可以被 `for` 循环消费；生成器用更轻量的方式实现惰性计算。",
            "`yield` 会暂停函数执行并保留上下文，下一次继续时从暂停点恢复。",
            "`send`、`throw`、`close` 让生成器不只是“产出数据”，还具备协作式控制能力。",
        ],
        mechanism=[
            "可迭代对象实现 `__iter__`，迭代器还需要实现 `__next__`。",
            "生成器函数一旦包含 `yield`，调用时不会立即执行函数体，而是返回生成器对象。",
            "`send(value)` 把值送回上一个 `yield` 表达式，首次启动时只能 `send(None)`。",
            "`throw(exc)` 会在生成器暂停点抛出异常；`close()` 会触发 `GeneratorExit` 并终止迭代。",
        ],
        examples=md(
            f"""
            ### 示例 1：自定义迭代器

            {code_block("python", '''
            class CountDown:
                def __init__(self, start: int) -> None:
                    self.current = start

                def __iter__(self):
                    return self

                def __next__(self) -> int:
                    if self.current <= 0:
                        raise StopIteration
                    value = self.current
                    self.current -= 1
                    return value


            print(list(CountDown(3)))
            '''.strip(), 'hl_lines="6 8 11"')}

            ### 示例 2：`yield` 与 `send`

            {code_block("python", '''
            def accumulator():
                total = 0
                while True:
                    number = yield total
                    total += 0 if number is None else number


            gen = accumulator()
            print(next(gen))
            print(gen.send(3))
            print(gen.send(5))
            gen.close()
            '''.strip(), 'hl_lines="4 5 9 10 11"')}

            ### 示例 3：`throw` 与异常处理

            {code_block("python", '''
            def receiver():
                try:
                    yield "ready"
                except ValueError:
                    yield "recovered"


            gen = receiver()
            print(next(gen))
            print(gen.throw(ValueError("boom")))
            '''.strip(), 'hl_lines="2 4 9"')}
            """
        ),
        pitfalls=[
            "把生成器当作列表反复消费，第二次通常什么都拿不到，因为它已经被耗尽。",
            "首次对生成器调用 `send(非 None)` 会报错，因为生成器还没有运行到第一个 `yield`。",
            "自定义迭代器如果忘记在结束时抛 `StopIteration`，就会写出错误的无限迭代。",
        ],
        practice=[
            "实现一个每次产出平方数的生成器，支持上限控制。",
            "写一个生成器，接收外部发送的数并累计总和。",
            "把一个列表包装成自定义迭代器，只遍历其中的偶数项。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "可迭代对象和迭代器的区别是什么？",
                "answer": "可迭代对象能返回迭代器，迭代器本身还负责通过 `__next__` 一个个产出元素。不是所有可迭代对象都是迭代器。",
                "link_text": "核心机制",
                "link_anchor": "核心机制",
            },
            {
                "type": "concept",
                "question": "`yield` 和 `return` 在函数里最大的语义差别是什么？",
                "answer": "`return` 会结束函数并返回结果，`yield` 会暂停函数、保留现场，并在后续继续恢复执行。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
            {
                "type": "concept",
                "question": "为什么 `send()` 常被说成是“协作式”的？",
                "answer": "因为调用方和生成器之间会在 `yield` 位置来回切换控制权，调用方能把数据送回生成器，生成器再决定如何继续处理。",
                "link_text": "核心机制",
                "link_anchor": "核心机制",
            },
            {
                "type": "coding",
                "question": "怎样安全地启动一个支持 `send()` 的生成器？",
                "answer": "先调用 `next(gen)` 或 `gen.send(None)`，把执行流推进到第一个 `yield` 位置，然后再发送真实值。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "coding",
                "question": "如何把生成器里的资源释放动作写得更稳妥？",
                "answer": "在消费结束后调用 `close()`，或者在生成器内部配合 `try/finally` 处理清理逻辑，确保提早退出时也能释放资源。",
                "link_text": "易错点",
                "link_anchor": "易错点",
            },
            {
                "type": "scenario",
                "question": "日志流很大，不能一次性全部读入内存，应该优先考虑列表还是生成器？",
                "answer": "优先考虑生成器。它按需产出数据，内存占用更稳定，尤其适合大文件、流式接口和分批处理场景。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
        ],
    )

    decorators = advanced_note(
        title="装饰器",
        tags=["python", "decorator", "wraps", "class-decorator", "aop"],
        concept=[
            "装饰器本质上是“接收一个可调用对象并返回另一个可调用对象”的高阶函数。",
            "它非常适合横切关注点，例如日志、计时、重试、鉴权、缓存和埋点。",
            "理解闭包与调用顺序后，装饰器就不再神秘。",
        ],
        mechanism=[
            "`@decorator` 等价于 `func = decorator(func)`。",
            "无参装饰器直接接收函数；带参装饰器会多一层工厂函数。",
            "`functools.wraps` 用于保留原函数名称、文档和签名元信息。",
            "多个装饰器时，靠近函数定义的那个先应用，调用时则从外到内进入、从内到外返回。",
        ],
        examples=md(
            f"""
            ### 示例 1：无参装饰器

            {code_block("python", '''
            from functools import wraps


            def trace(func):
                @wraps(func)
                def wrapper(*args, **kwargs):
                    print(f"calling {func.__name__}")
                    return func(*args, **kwargs)
                return wrapper


            @trace
            def add(left: int, right: int) -> int:
                return left + right


            print(add(2, 3))
            '''.strip(), 'hl_lines="4 6 11"')}

            ### 示例 2：带参装饰器

            {code_block("python", '''
            from functools import wraps


            def repeat(times: int):
                def decorator(func):
                    @wraps(func)
                    def wrapper(*args, **kwargs):
                        result = None
                        for _ in range(times):
                            result = func(*args, **kwargs)
                        return result
                    return wrapper
                return decorator


            @repeat(3)
            def greet() -> str:
                print("hello")
                return "done"


            print(greet())
            '''.strip(), 'hl_lines="4 5 8 15"')}

            ### 示例 3：类装饰器与执行顺序图

            ```mermaid
            flowchart TD
                A["@outer"] --> B["@inner"]
                B --> C["target()"]
                C --> D["inner wrapper"]
                D --> E["outer wrapper"]
            ```

            {code_block("python", '''
            class Prefix:
                def __init__(self, text: str) -> None:
                    self.text = text

                def __call__(self, func):
                    def wrapper(*args, **kwargs):
                        return f"{self.text}:{func(*args, **kwargs)}"
                    return wrapper


            @Prefix("tag")
            def status() -> str:
                return "ok"


            print(status())
            '''.strip(), 'hl_lines="5 6 10"')}
            """
        ),
        pitfalls=[
            "忘记使用 `@wraps`，会导致被装饰函数的名称、文档和调试信息丢失。",
            "多层装饰器嵌套时，如果不清楚调用顺序，很容易在重试、计时、日志上得到意外行为。",
            "把太多业务逻辑塞进装饰器，会让真实流程隐藏在语法糖背后，反而更难维护。",
        ],
        practice=[
            "写一个计时装饰器，打印函数执行秒数。",
            "写一个带参装饰器，只允许函数执行指定次数。",
            "写一个类装饰器，为函数返回值自动加前缀。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "装饰器语法糖展开后是什么形式？",
                "answer": "`@decorator` 实际等价于 `target = decorator(target)`。理解这一点后，很多嵌套装饰器的行为就不难推导了。",
                "link_text": "核心机制",
                "link_anchor": "核心机制",
            },
            {
                "type": "concept",
                "question": "`wraps` 的主要作用是什么？",
                "answer": "它会把原函数的 `__name__`、`__doc__` 等元信息复制到包装函数上，方便调试、日志和反射工具使用。",
                "link_text": "核心机制",
                "link_anchor": "核心机制",
            },
            {
                "type": "concept",
                "question": "多层装饰器的调用顺序如何理解？",
                "answer": "应用时从下往上包裹，调用时从外层先进入，再逐层调用内层函数，最后再一层层返回。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "coding",
                "question": "怎样给任何函数添加统一日志而不改函数体？",
                "answer": "定义一个装饰器，在包装函数里记录入参与返回值，再调用原函数并返回结果即可。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "coding",
                "question": "带参装饰器为什么需要三层函数？",
                "answer": "第一层接收装饰器参数，第二层接收被装饰函数，第三层是真正的运行时包装器，这样装饰器参数和函数调用参数才能分离。",
                "link_text": "核心机制",
                "link_anchor": "核心机制",
            },
            {
                "type": "scenario",
                "question": "你要给所有接口调用函数统一加重试和耗时统计，为什么装饰器适合这个场景？",
                "answer": "因为这类逻辑与业务本身是横切关注点。用装饰器可以把公共能力集中在一处实现，避免在每个函数里重复写相同模板代码。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
        ],
    )

    context_managers = advanced_note(
        title="上下文管理器",
        tags=["python", "context-manager", "with", "contextlib", "resource"],
        concept=[
            "`with` 语句用于把“获取资源”和“释放资源”绑定到一个清晰边界里。",
            "文件、锁、数据库连接、临时目录、网络会话都非常适合用上下文管理器表达。",
            "上下文管理器让资源释放变成结构化能力，而不是靠人记得手动 `close()`。",
        ],
        mechanism=[
            "实现了 `__enter__` 和 `__exit__` 的对象可以配合 `with` 使用。",
            "`__enter__` 返回要绑定给 `as` 后变量的对象。",
            "`__exit__` 会在退出时被调用，无论代码块正常结束还是发生异常。",
            "`contextlib.contextmanager` 能把生成器快速封装为上下文管理器，适合轻量场景。",
        ],
        examples=md(
            f"""
            ### 示例 1：自定义类实现 `with`

            {code_block("python", '''
            class Recorder:
                def __enter__(self):
                    self.messages = ["open"]
                    return self

                def __exit__(self, exc_type, exc, tb):
                    self.messages.append("close")
                    return False


            with Recorder() as recorder:
                recorder.messages.append("working")

            print(recorder.messages)
            '''.strip(), 'hl_lines="2 6 10"')}

            ### 示例 2：`contextlib.contextmanager`

            {code_block("python", '''
            from contextlib import contextmanager


            @contextmanager
            def managed_flag():
                state = {"opened": True}
                try:
                    yield state
                finally:
                    state["opened"] = False


            with managed_flag() as flag:
                print(flag["opened"])
            '''.strip(), 'hl_lines="4 7 8 11"')}

            ### 示例 3：异常情况下仍然释放资源

            {code_block("python", '''
            class SafeCleanup:
                def __enter__(self):
                    self.cleaned = False
                    return self

                def __exit__(self, exc_type, exc, tb):
                    self.cleaned = True
                    return False


            cleanup = None
            try:
                with SafeCleanup() as cleanup:
                    raise RuntimeError("boom")
            except RuntimeError:
                pass

            print(cleanup.cleaned)
            '''.strip(), 'hl_lines="6 12 16"')}
            """
        ),
        pitfalls=[
            "`__exit__` 返回 `True` 会吞掉异常，如果你只是想做清理但不想隐藏错误，应该返回 `False` 或 `None`。",
            "手写上下文管理器时忘记释放资源，等于只用了 `with` 的语法，没得到它的价值。",
            "用生成器实现上下文管理器时，`yield` 前后代码的职责要清晰：前半段负责准备，后半段负责清理。",
        ],
        practice=[
            "写一个上下文管理器，进入时打印 `start`，退出时打印 `end`。",
            "用 `contextmanager` 封装一个临时配置开关。",
            "模拟一个带异常的代码块，验证 `__exit__` 仍会执行。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "`with` 语句想解决的核心问题是什么？",
                "answer": "它解决的是资源生命周期管理问题：什么时候拿到资源，什么时候一定释放，异常发生时是否还能保证清理动作执行。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
            {
                "type": "concept",
                "question": "`__enter__` 和 `__exit__` 分别负责什么？",
                "answer": "`__enter__` 负责准备并返回上下文对象，`__exit__` 负责退出清理，并决定是否吞掉异常。",
                "link_text": "核心机制",
                "link_anchor": "核心机制",
            },
            {
                "type": "concept",
                "question": "什么情况下 `contextlib.contextmanager` 比类更合适？",
                "answer": "当上下文逻辑简单、状态不多时，用生成器包装会更轻便；如果需要更多方法和复杂状态，类实现通常更清晰。",
                "link_text": "核心机制",
                "link_anchor": "核心机制",
            },
            {
                "type": "coding",
                "question": "如何确保异常发生时也能执行清理逻辑？",
                "answer": "在类实现里把清理写进 `__exit__`，在生成器实现里把清理写进 `finally`。这两种方式都能覆盖异常退出路径。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "coding",
                "question": "为什么很多文件读写示例都推荐 `with open(...) as f`？",
                "answer": "因为它能保证文件句柄在作用域结束后及时关闭，避免忘记 `close()` 或异常导致资源泄漏。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
            {
                "type": "scenario",
                "question": "你在接口测试里需要临时创建一批测试数据，测试结束必须回收，应该怎样组织代码？",
                "answer": "可以把“创建数据”和“回收数据”封装进上下文管理器，在 `with` 块里执行业务断言。这样无论断言是否失败，回收逻辑都能执行。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
        ],
    )

    object_oriented_programming = advanced_note(
        title="面向对象",
        tags=["python", "oop", "property", "slots", "mro"],
        concept=[
            "面向对象的关键不只是“有类和对象”，而是通过封装、继承、多态组织复杂状态与行为。",
            "在 Python 里，类变量、实例变量、属性、描述符、MRO 等机制共同决定对象行为。",
            "测试工程常用 OOP 封装页面对象、接口客户端、测试数据模型和资源句柄。",
        ],
        mechanism=[
            "类变量属于类本身，实例变量属于对象实例，两者查找路径不同。",
            "`property` 让你用属性访问语法包装校验或计算逻辑。",
            "`__slots__` 可限制实例可绑定属性，减少拼写错误和内存开销。",
            "继承、多态和 MRO 决定方法覆盖与查找顺序；抽象基类 `abc` 可约束子类接口。",
        ],
        examples=md(
            f"""
            ### 示例 1：类变量、实例变量与 `property`

            {code_block("python", '''
            class TestUser:
                role = "viewer"

                def __init__(self, name: str, age: int) -> None:
                    self.name = name
                    self._age = age

                @property
                def age(self) -> int:
                    return self._age


            user = TestUser("alice", 18)
            print(TestUser.role, user.age)
            '''.strip(), 'hl_lines="2 5 8 13"')}

            ### 示例 2：`__slots__` 与继承

            {code_block("python", '''
            class Device:
                __slots__ = ("name",)

                def __init__(self, name: str) -> None:
                    self.name = name


            class Phone(Device):
                __slots__ = ("platform",)

                def __init__(self, name: str, platform: str) -> None:
                    super().__init__(name)
                    self.platform = platform


            phone = Phone("pixel", "android")
            print(phone.name, phone.platform)
            '''.strip(), 'hl_lines="2 8 11"')}

            ### 示例 3：多态、MRO 与抽象基类

            {code_block("python", '''
            from abc import ABC, abstractmethod


            class Reporter(ABC):
                @abstractmethod
                def render(self) -> str:
                    raise NotImplementedError


            class JsonReporter(Reporter):
                def render(self) -> str:
                    return '{"status": "ok"}'


            reporter = JsonReporter()
            print(reporter.render())
            print(JsonReporter.mro()[0].__name__)
            '''.strip(), 'hl_lines="4 5 9 14 15"')}
            """
        ),
        pitfalls=[
            "把可变类变量当作实例状态使用，常会导致多个对象意外共享同一份数据。",
            "`property` 里隐藏太多副作用会让调用者误以为只是读属性，结果触发网络请求或昂贵计算。",
            "继承层级过深会让 MRO 和覆盖关系变得难懂，很多时候组合比继承更稳妥。",
        ],
        practice=[
            "设计一个 `PageObject` 基类，并让两个页面子类分别实现 `open()` 方法。",
            "用 `property` 给年龄字段加上非负校验。",
            "写一个抽象基类约束不同报告生成器都实现 `render()` 方法。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "类变量和实例变量的查找顺序有什么差异？",
                "answer": "访问实例属性时会先找实例字典，再回溯到类；类变量定义在类上，会被所有实例共享，除非实例上显式覆盖同名属性。",
                "link_text": "核心机制",
                "link_anchor": "核心机制",
            },
            {
                "type": "concept",
                "question": "`property` 为什么能提升封装性？",
                "answer": "它允许你保留属性访问语法，同时在读取或写入时插入校验、计算和保护逻辑，不需要暴露显式 getter/setter。",
                "link_text": "核心机制",
                "link_anchor": "核心机制",
            },
            {
                "type": "concept",
                "question": "MRO 在多继承下解决了什么问题？",
                "answer": "它定义了方法查找顺序，避免解释器在多继承图里不知道该先调用哪个父类实现。",
                "link_text": "核心机制",
                "link_anchor": "核心机制",
            },
            {
                "type": "coding",
                "question": "如何让子类必须实现某个方法？",
                "answer": "使用 `abc.ABC` 和 `@abstractmethod`。未实现抽象方法的子类将不能被实例化。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "coding",
                "question": "`__slots__` 能帮你防止哪类错误？",
                "answer": "它能限制实例可绑定的属性名，减少拼写错误导致的“悄悄加出一个新属性”的问题，同时也可能降低内存占用。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "scenario",
                "question": "在自动化测试框架里，什么时候适合用继承，什么时候更适合组合？",
                "answer": "当多个对象共享稳定接口和少量共同实现时可用继承；当能力模块彼此独立、组合关系频繁变化时，用组合通常更清晰、更容易测试。",
                "link_text": "易错点",
                "link_anchor": "易错点",
            },
        ],
    )

    exceptions_define_cmd = code_block("python", '''
            class ValidationError(Exception):
                """Raised when input payload is invalid."""


            def validate_age(age: int) -> None:
                if age < 0:
                    raise ValidationError("age must be non-negative")


            validate_age(1)
            print("ok")
            '''.strip(), 'hl_lines="1 6"')
    exceptions_chain_cmd = code_block("python", '''
            def parse_port(value: str) -> int:
                try:
                    return int(value)
                except ValueError as error:
                    raise ValueError(f"invalid port: {value}") from error


            try:
                parse_port("abc")
            except ValueError as exc:
                print(type(exc.__cause__).__name__)
            '''.strip(), 'hl_lines="4 5 10"')
    exceptions_logging_cmd = code_block("python", '''
            import logging

            logging.basicConfig(level=logging.INFO)
            logger = logging.getLogger(__name__)

            try:
                raise RuntimeError("network timeout")
            except RuntimeError:
                logger.exception("request failed")
            '''.strip(), 'hl_lines="7 9"')
    exceptions = advanced_note(
        title="异常体系",
        tags=["python", "exception", "raise-from", "logging", "error-handling"],
        concept=[
            "异常是 Python 里表达错误路径的正式机制，不是“程序崩了以后才会看到的附属产物”。",
            "设计异常时要考虑可读性、可恢复性和排障上下文，而不是只图省事地 `except Exception`。",
            "自定义异常和异常链能让定位问题时保留更多业务语义。",
        ],
        mechanism=[
            "内置异常按层级组织，`BaseException` 在最顶层，业务代码通常只处理 `Exception` 体系。",
            "`raise` 抛出异常，`raise from` 用于显式建立异常链。",
            "`try/except/else/finally` 分别用于捕获、正常分支、以及清理收尾。",
            "日志记录异常时优先使用 `logger.exception` 或 `exc_info=True`，不要吞掉关键信息。",
        ],
        examples=md(
            """
            ### 示例 1：自定义异常

            {exceptions_define_cmd}

            ### 示例 2：`raise from`

            {exceptions_chain_cmd}

            ### 示例 3：日志记录最佳实践

            {exceptions_logging_cmd}
            """.format(
                exceptions_define_cmd=exceptions_define_cmd,
                exceptions_chain_cmd=exceptions_chain_cmd,
                exceptions_logging_cmd=exceptions_logging_cmd,
            )
        ),
        pitfalls=[
            "直接 `except Exception: pass` 会吞掉错误，让问题在更远的地方以更隐蔽的方式爆出来。",
            "把业务校验错误和系统错误混在同一个异常类型里，会让调用方难以决定是否可重试。",
            "日志里只记录“失败了”而不带异常栈，等于放弃了最重要的排障线索。",
        ],
        practice=[
            "为配置加载逻辑定义一个自定义异常，表达“必填字段缺失”。",
            "把底层 `KeyError` 包装成更易懂的业务异常，并保留原始异常链。",
            "写一个 `try/except/finally` 示例，验证 finally 始终执行。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "为什么业务代码通常只捕获 `Exception` 体系，而不去捕获 `BaseException`？",
                "answer": "因为 `BaseException` 还包含 `SystemExit`、`KeyboardInterrupt` 等系统级信号，业务代码不应该随意吞掉这些退出机制。",
                "link_text": "核心机制",
                "link_anchor": "核心机制",
            },
            {
                "type": "concept",
                "question": "`raise from` 相比直接重新抛异常，多了什么价值？",
                "answer": "它显式保留了底层异常作为 `__cause__`，方便你同时看到业务语义和原始错误来源。",
                "link_text": "核心机制",
                "link_anchor": "核心机制",
            },
            {
                "type": "concept",
                "question": "为什么“异常日志要带栈信息”是基本要求？",
                "answer": "因为没有栈就很难知道错误是在哪一层、哪条路径发生的。只靠一条字符串日志通常无法复盘完整上下文。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
            {
                "type": "coding",
                "question": "如何把 `KeyError` 包装成更易懂的配置异常？",
                "answer": "在 `except KeyError as error` 中抛出自定义异常，并用 `raise ConfigError(...) from error` 保留原始因果关系。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "coding",
                "question": "如何在记录日志时自动附带当前异常栈？",
                "answer": "在 `except` 块中调用 `logger.exception(\"...\")`，或者 `logger.error(\"...\", exc_info=True)`。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "scenario",
                "question": "在自动化测试框架里，哪些异常应该被重试，哪些应该直接失败？",
                "answer": "网络抖动、临时超时等可恢复错误可以考虑重试；断言失败、数据不合法、配置缺失等确定性错误应直接失败并尽快暴露。",
                "link_text": "易错点",
                "link_anchor": "易错点",
            },
        ],
    )

    modules_import_cmd = code_block("python", '''
            import importlib

            json_module = importlib.import_module("json")
            print(json_module.dumps({"status": "ok"}, sort_keys=True))
            '''.strip(), 'hl_lines="3"')
    modules_all_cmd = code_block("python", '''
            __all__ = ["build_message"]


            def build_message(name: str) -> str:
                return f"hello, {name}"


            print(build_message("qa"))
            '''.strip(), 'hl_lines="1"')
    modules_zipapp_cmd = code_block("python", '''
            import tempfile
            import zipapp
            from pathlib import Path

            with tempfile.TemporaryDirectory() as temp_dir:
                root = Path(temp_dir) / "demo_app"
                root.mkdir()
                (root / "__main__.py").write_text('print("zipapp ready")\\n', encoding="utf-8")
                target = Path(temp_dir) / "demo.pyz"
                zipapp.create_archive(root, target)
                print(target.exists())
            '''.strip(), 'hl_lines="7 9 10"')
    modules_and_packages = advanced_note(
        title="模块与包",
        tags=["python", "module", "package", "import", "zipapp"],
        concept=[
            "模块是单个 `.py` 文件，包是可以组织多个模块的目录结构。",
            "合理的包结构能让测试工具、业务封装和共享能力边界更清晰，也能减少循环导入。",
            "理解绝对导入、相对导入、命名空间包和打包入口，是项目工程化的重要基础。",
        ],
        mechanism=[
            "`__init__.py` 常用于标记传统包、暴露公共 API 或执行轻量初始化。",
            "绝对导入从项目根包开始写路径，清晰稳定；相对导入更适合包内部协作。",
            "`__all__` 可以控制 `from package import *` 暴露的名称，但团队代码里仍应少用星号导入。",
            "`zipapp` 可以把一个可执行包目录打成单文件归档，便于分发命令行工具。",
        ],
        examples=md(
            """
            ### 示例 1：动态导入标准库模块

            {modules_import_cmd}

            ### 示例 2：定义 `__all__`

            {modules_all_cmd}

            ### 示例 3：用 `zipapp` 生成可执行包

            {modules_zipapp_cmd}
            """.format(
                modules_import_cmd=modules_import_cmd,
                modules_all_cmd=modules_all_cmd,
                modules_zipapp_cmd=modules_zipapp_cmd,
            )
        ),
        pitfalls=[
            "随意在脚本根目录里使用相对导入，脱离包上下文运行时很容易直接报错。",
            "在 `__init__.py` 里放太重的初始化逻辑，会让导入成本和副作用都变大。",
            "循环导入往往不是导入语法本身的问题，而是模块职责拆分不清。",
        ],
        practice=[
            "设计一个 `client/` 包，对外只暴露 `HttpClient`。",
            "尝试把一个最小命令行脚本打成 `.pyz` 文件。",
            "把散落在脚本里的工具函数整理到包结构中，并改成绝对导入。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "模块和包的最小区别是什么？",
                "answer": "模块通常是一个 `.py` 文件；包是组织多个模块的目录结构，能表达更清晰的命名空间和层次关系。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
            {
                "type": "concept",
                "question": "绝对导入和相对导入各自适合什么场景？",
                "answer": "绝对导入更清晰稳定，适合跨包依赖；相对导入适合包内部相邻模块协作，但不宜过深或过度复杂。",
                "link_text": "核心机制",
                "link_anchor": "核心机制",
            },
            {
                "type": "concept",
                "question": "`__all__` 真正控制的是什么？",
                "answer": "它主要控制 `from module import *` 时可导出的名称集合，是一种 API 暴露声明，而不是访问权限控制。",
                "link_text": "核心机制",
                "link_anchor": "核心机制",
            },
            {
                "type": "coding",
                "question": "如何把一个目录快速打成可执行 `.pyz` 文件？",
                "answer": "准备好包含 `__main__.py` 的目录后，调用 `zipapp.create_archive(source_dir, target_path)` 即可生成归档。",
                "link_text": "代码示例",
                "link_anchor": "代码示例",
            },
            {
                "type": "coding",
                "question": "为什么很多团队会在包根目录的 `__init__.py` 里只做轻量暴露？",
                "answer": "因为这样导入成本更稳定，也更容易控制对外 API，避免引入复杂副作用和循环依赖。",
                "link_text": "易错点",
                "link_anchor": "易错点",
            },
            {
                "type": "scenario",
                "question": "你的自动化项目里既有 API 客户端、页面对象、公共断言、数据工厂，为什么应该尽早整理成包？",
                "answer": "因为包结构能明确模块边界，减少脚本式堆叠造成的循环依赖，也方便团队逐步演进到可测试、可分发、可复用的工程结构。",
                "link_text": "概念",
                "link_anchor": "概念",
            },
        ],
    )

    write("03_advanced_syntax/iterators_and_generators.md", iterators_and_generators)
    write("03_advanced_syntax/decorators.md", decorators)
    write("03_advanced_syntax/context_managers.md", context_managers)
    write("03_advanced_syntax/object_oriented_programming.md", object_oriented_programming)
    write("03_advanced_syntax/exceptions.md", exceptions)
    write("03_advanced_syntax/modules_and_packages.md", modules_and_packages)


def build_progressive_notes() -> None:
    python_re_main_cmd = code_block("python", '''
            import re

            pattern = re.compile(
                r"^(?P<level>INFO|ERROR)\\s+user=(?P<user>\\w+)\\s+cost=(?P<cost>\\d+)ms$"
            )

            line = "ERROR user=alice cost=128ms"
            match = pattern.search(line)

            assert match is not None
            print(match.group("level"))
            print(match.groupdict())
            '''.strip(), 'hl_lines="3 8 10 11"')
    python_re_advanced_cmd = code_block("python", '''
            import re

            html = "<title>alpha</title><title>beta</title>"
            titles = re.findall(r"<title>(.*?)</title>", html)
            digits_before_ms = re.findall(r"\\d+(?=ms)", "cost=18ms retry=2")

            print(titles)
            print(digits_before_ms)
            '''.strip(), 'hl_lines="4 5"')
    python_re = progressive_note(
        title="正则表达式与 re 模块",
        tags=["python", "regex", "re", "log-parsing", "pattern"],
        why=[
            "测试工程经常要处理日志、接口报文、批量文本清洗和字段抽取，正则是非常高频的工具。",
            "会写简单正则不够，真正落地时更重要的是知道如何控制可读性、贪婪行为和命名分组。",
            "掌握 `re` 后，你可以更稳定地做日志解析、结果校验和模糊匹配断言。",
        ],
        what=[
            "元字符：`.`、`*`、`+`、`?`、`[]`、`()`、`{m,n}`、`^`、`$` 等。",
            "贪婪与非贪婪匹配的差异，以及如何通过 `?` 控制。",
            "捕获分组、命名分组、前向断言与常用 API：`search`、`findall`、`sub`、`compile`。",
        ],
        how=md(
            """
            ### 核心代码：日志解析

            {python_re_main_cmd}

            ### 进阶技巧：非贪婪匹配与前向断言

            {python_re_advanced_cmd}

            落地建议:
            - 高频模式先 `compile()`，避免重复解析。
            - 对复杂正则配上命名分组和注释，降低后续维护成本。
            - 遇到结构化数据（JSON、HTML、XML）时，优先考虑专门解析器，正则只作为补充工具。
            """.format(
                python_re_main_cmd=python_re_main_cmd,
                python_re_advanced_cmd=python_re_advanced_cmd,
            )
        ),
        cases=[
            "日志平台常用正则从文本行中抽出 trace_id、状态码、耗时和用户标识。",
            "接口测试会用正则校验时间戳、订单号、脱敏手机号等动态字段。",
            "CI 流水线里经常用正则从命令行输出中提取失败摘要或覆盖率数字。",
        ],
        extra_reading=[
            "[Python re 文档](https://docs.python.org/3/library/re.html)",
            "[Regex101 交互式调试工具](https://regex101.com/)",
            "优先使用原始字符串书写模式，降低转义噪音。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "什么是贪婪匹配，为什么 HTML 场景里经常要改成非贪婪？",
                "answer": "贪婪匹配会尽可能多地吞字符，HTML 中容易一下子跨过多个标签；改成 `.*?` 这样的非贪婪写法后，通常更容易只拿到最近的匹配。",
                "link_text": "学什么",
                "link_anchor": "学什么",
            },
            {
                "type": "concept",
                "question": "命名分组相比普通分组有什么优势？",
                "answer": "它让提取结果带上语义名称，调用时可用 `group(\"name\")` 或 `groupdict()`，可读性和维护性都更好。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "concept",
                "question": "前向断言适合解决什么问题？",
                "answer": "它适合“只在某个后缀条件成立时匹配当前内容，但不把后缀吃掉”的场景，例如匹配 `ms` 前面的数字。",
                "link_text": "学什么",
                "link_anchor": "学什么",
            },
            {
                "type": "coding",
                "question": "怎样从一行日志里提取 `level`、`user` 和 `cost` 三个字段？",
                "answer": "可以用命名分组的 `re.compile()` 模式，然后通过 `match.groupdict()` 一次拿到结构化字典。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "coding",
                "question": "如何匹配多个 `<title>...</title>` 标签中的内容而不过度吞噬文本？",
                "answer": "使用非贪婪模式 `r\"<title>(.*?)</title>\"`，而不是默认的贪婪 `.*`。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "scenario",
                "question": "你要在 CI 输出里提取覆盖率百分比和失败用例名，为什么正则合适，但也不能滥用？",
                "answer": "因为终端输出本质上是文本，正则提取很方便；但如果源数据已经是 JSON、XML 或 HTML，就应优先使用结构化解析器，避免脆弱模式。",
                "link_text": "业界案例",
                "link_anchor": "业界案例",
            },
        ],
    )

    python_keywords = progressive_note(
        title="Python 关键字全集",
        tags=["python", "keywords", "syntax", "parser", "highlight"],
        why=[
            "关键字是语言语法的地基。很多看似“记不住”的语法，其实都围绕关键字的语义边界展开。",
            "测试工程里做代码生成、AST 分析、关键字高亮或样例审查时，理解关键字集合很有帮助。",
            "随着 Python 版本演进，关键字也会变化，例如 `match`、`case` 就是较新的语法关键字。",
        ],
        what=[
            "Python 3.12 常见关键字包括 `False`、`None`、`True`、`and`、`as`、`assert`、`async`、`await`、`break`、`class`、`continue`、`def`、`del`、`elif`、`else`、`except`、`finally`、`for`、`from`、`global`、`if`、`import`、`in`、`is`、`lambda`、`nonlocal`、`not`、`or`、`pass`、`raise`、`return`、`try`、`while`、`with`、`yield`。",
            "版本差异重点关注 `async` / `await`、`match` / `case` 等在新语法里引入的保留字或软关键字。",
            "关键字高亮通常来自词法分析器，它会把这些保留字映射到特定 token 类型，再交给编辑器着色。",
        ],
        how=md(
            f"""
            ### 用标准库查看关键字列表

            {code_block("python", '''
            import keyword

            words = keyword.kwlist
            print(len(words))
            print(words[:10])
            print("async" in words, "await" in words)
            '''.strip(), 'hl_lines="3 5"')}

            ### 判断一个标识符是否与关键字冲突

            {code_block("python", '''
            import keyword

            candidates = ["status", "class", "case", "yield_value"]
            conflicts = [name for name in candidates if keyword.iskeyword(name)]

            print(conflicts)
            '''.strip(), 'hl_lines="4"')}

            学习建议:
            - 不必死记硬背全部列表，但要知道哪些关键字承载控制流、定义、导入、异常和异步语义。
            - 对版本敏感语法要结合当前解释器版本学习，不要混用旧语法与新语法。
            - 关键字不能直接作为变量名；如果业务字段撞名，可通过后缀 `_` 规避，如 `class_`。
            """
        ),
        cases=[
            "代码生成器在输出 Python 变量名时，需要先检查是否撞上关键字。",
            "语法高亮器和 LSP 服务器会基于关键字与上下文做 token 分类。",
            "版本升级时，团队脚本可能因为新关键字保留而出现命名冲突，需要批量修复。",
        ],
        extra_reading=[
            "[keyword 模块文档](https://docs.python.org/3/library/keyword.html)",
            "[Python 词法分析文档](https://docs.python.org/3/reference/lexical_analysis.html)",
            "关注 `match` / `case` 这类新语法的版本边界。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "关键字和普通标识符的根本区别是什么？",
                "answer": "关键字是解释器保留给语法结构的词，不能随意作为变量、函数或类名使用；普通标识符则由开发者自由定义。",
                "link_text": "学什么",
                "link_anchor": "学什么",
            },
            {
                "type": "concept",
                "question": "为什么说某些关键字会受版本影响？",
                "answer": "因为随着语法演进，解释器可能把原本普通的词升级为关键字或软关键字。升级 Python 版本前，需要注意兼容性变化。",
                "link_text": "为什么学",
                "link_anchor": "为什么学",
            },
            {
                "type": "concept",
                "question": "编辑器里的关键字高亮大致是如何工作的？",
                "answer": "词法分析器会扫描源码，把关键字标成特定 token 类型；编辑器再根据主题把这些 token 渲染成不同颜色。",
                "link_text": "学什么",
                "link_anchor": "学什么",
            },
            {
                "type": "coding",
                "question": "如何检查一个名字是否是 Python 关键字？",
                "answer": "使用标准库 `keyword.iskeyword(name)`。如果返回 `True`，就应该避免直接拿它做标识符。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "coding",
                "question": "如果业务字段恰好叫 `class`，变量名该如何处理？",
                "answer": "常见做法是加下划线后缀，例如 `class_`，既避开关键字冲突，又保留业务含义。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "scenario",
                "question": "团队有一套模板脚本会根据 JSON 字段名自动生成 Python 模型，为什么要先做关键字检查？",
                "answer": "因为字段名可能正好是 `class`、`from`、`global` 等关键字，不做检查就会生成无法运行的代码。生成器应在输出前自动规避这些名字。",
                "link_text": "业界案例",
                "link_anchor": "业界案例",
            },
        ],
    )

    python_concurrency = progressive_note(
        title="并发模型：线程、进程、协程与 GIL",
        tags=["python", "concurrency", "threading", "asyncio", "multiprocessing"],
        why=[
            "测试工程会同时面对 I/O 密集型任务、CPU 密集型任务和高并发调度问题，单靠同步脚本很快就会遇到瓶颈。",
            "理解线程、进程、协程和 GIL 的边界，能帮助你选择正确模型，而不是盲目“并发化”。",
            "本节重点是“什么时候该用什么”，而不只是会写几个 API 调用。",
        ],
        what=[
            "线程适合 I/O 密集型任务；进程适合 CPU 密集型任务；协程适合大量可挂起的异步 I/O 任务。",
            "CPython 的 GIL 限制了同一进程内多个线程并行执行 Python 字节码，但不阻止 I/O 并发。",
            "`multiprocessing`、`concurrent.futures`、`asyncio` 是最常见的三套工程化入口。",
        ],
        how=md(
            f"""
            ### 示例 1：ThreadPoolExecutor

            {code_block("python", '''
            from concurrent.futures import ThreadPoolExecutor
            import time


            def fetch(name: str) -> str:
                time.sleep(0.01)
                return f"done:{name}"


            with ThreadPoolExecutor(max_workers=2) as executor:
                results = list(executor.map(fetch, ["api", "ui", "perf"]))

            print(results)
            '''.strip(), 'hl_lines="5 9"')}

            ### 示例 2：asyncio 事件循环

            {code_block("python", '''
            import asyncio


            async def fetch(name: str) -> str:
                await asyncio.sleep(0.01)
                return f"async:{name}"


            async def main() -> None:
                results = await asyncio.gather(fetch("a"), fetch("b"))
                print(results)


            asyncio.run(main())
            '''.strip(), 'hl_lines="4 8 12"')}

            ### 示例 3：进程池入口示意

            {code_block("python", '''
            from concurrent.futures import ProcessPoolExecutor


            def square(value: int) -> int:
                return value * value


            if __name__ == "__main__":
                with ProcessPoolExecutor(max_workers=2) as executor:
                    print(list(executor.map(square, [1, 2, 3])))
            else:
                print("process example skipped in imported mode")
            '''.strip(), 'hl_lines="8 9"')}

            选型口诀:
            - I/O 密集：优先线程或协程。
            - CPU 密集：优先进程。
            - 数量巨大且大多在等待：优先协程。
            """
        ),
        cases=[
            "批量接口巡检、批量页面冒烟、批量文件上传下载通常适合线程池或协程。",
            "压测数据预处理、日志大规模解析、图像对比等 CPU 密集任务更适合进程池。",
            "异步爬虫、消息消费、WebSocket 监听这类高连接数场景通常会选 asyncio。",
        ],
        extra_reading=[
            "[asyncio 文档](https://docs.python.org/3/library/asyncio.html)",
            "[concurrent.futures 文档](https://docs.python.org/3/library/concurrent.futures.html)",
            "选型时先看任务类型，再看团队维护成本和生态配套。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "GIL 为什么不意味着“Python 线程没用”？",
                "answer": "因为 GIL 主要限制的是同一时刻执行 Python 字节码的线程数量，但 I/O 等待期间线程仍然可以切换，所以线程对 I/O 密集任务依然有效。",
                "link_text": "学什么",
                "link_anchor": "学什么",
            },
            {
                "type": "concept",
                "question": "线程、进程、协程三者最核心的选择依据是什么？",
                "answer": "看任务是 I/O 密集还是 CPU 密集，以及任务规模和调用栈是否天然适合异步。线程偏 I/O，进程偏 CPU，协程偏海量可挂起 I/O。",
                "link_text": "学什么",
                "link_anchor": "学什么",
            },
            {
                "type": "concept",
                "question": "`asyncio` 的事件循环在做什么？",
                "answer": "它负责调度协程，在它们遇到 `await` 可挂起点时切换执行，让单线程也能高效处理大量并发 I/O 任务。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "coding",
                "question": "如何快速把多个 I/O 任务并发执行起来？",
                "answer": "同步代码可先用 `ThreadPoolExecutor`；异步代码可用 `asyncio.gather()` 同时等待多个协程结果。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "coding",
                "question": "为什么进程池示例常写在 `if __name__ == \"__main__\":` 里？",
                "answer": "尤其在 Windows 上，子进程会重新导入主模块。加这层保护可以避免递归创建进程和入口重复执行。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "scenario",
                "question": "你要同时跑 300 个接口健康检查，每个请求都要等待网络返回，最先考虑哪种并发模型？",
                "answer": "优先考虑线程池或 asyncio，因为这类任务主要卡在网络 I/O。是否选协程，再看现有代码栈是不是异步友好。",
                "link_text": "业界案例",
                "link_anchor": "业界案例",
            },
        ],
    )

    python_profiling = progressive_note(
        title="性能剖析",
        tags=["python", "profiling", "timeit", "cprofile", "memory"],
        why=[
            "性能优化最容易犯的错就是“没测就改”。剖析工具的作用是先找热点，再谈优化。",
            "测试工程虽然不一定天天写高性能服务，但经常会写数据处理脚本、日志分析工具和批量任务，性能问题并不少见。",
            "掌握时间、CPU、内存三个维度的观测方式，才能避免只看一种指标就做结论。",
        ],
        what=[
            "`timeit` 适合测小片段耗时，`cProfile` 适合看函数级调用统计。",
            "`line_profiler` 适合定位慢行，`memory_profiler` 和 `objgraph` 适合观察内存增长与对象关系。",
            "火焰图适合做更直观的热点可视化，但前提仍然是先拿到可靠 profile 数据。",
        ],
        how=md(
            f"""
            ### 示例 1：`timeit`

            {code_block("python", '''
            import timeit

            result = timeit.timeit("sum(range(100))", number=1000)
            print(round(result, 4))
            '''.strip(), 'hl_lines="3"')}

            ### 示例 2：`cProfile`

            {code_block("python", '''
            import cProfile
            import io
            import pstats


            def compute() -> int:
                return sum(i * i for i in range(1000))


            profiler = cProfile.Profile()
            profiler.enable()
            compute()
            profiler.disable()

            stream = io.StringIO()
            stats = pstats.Stats(profiler, stream=stream).sort_stats("cumulative")
            stats.print_stats(3)
            print("compute" in stream.getvalue())
            '''.strip(), 'hl_lines="9 10 15 17"')}

            ### 示例 3：第三方工具的安全导入

            {code_block("python", '''
            optional_tools = {}

            for name in ("line_profiler", "memory_profiler", "objgraph"):
                try:
                    optional_tools[name] = __import__(name)
                except ImportError:
                    optional_tools[name] = None

            print(sorted(optional_tools))
            '''.strip(), 'hl_lines="3 5 7"')}

            实战建议:
            - 先用 `timeit` 或真实压测场景确认“真的慢”。
            - 再用 `cProfile` 看热点函数，必要时下钻到逐行或内存分析。
            - 优化后重新测量，确保收益真实存在。
            """
        ),
        cases=[
            "批量日志解析脚本跑得慢时，先看是不是字符串处理、正则或 I/O 成为热点。",
            "测试报告生成耗时过长时，可用 `cProfile` 找出最重的聚合和序列化步骤。",
            "长时间运行的守护脚本内存上涨时，可用 `memory_profiler` 或 `objgraph` 排查对象泄漏。",
        ],
        extra_reading=[
            "[timeit 文档](https://docs.python.org/3/library/timeit.html)",
            "[cProfile 文档](https://docs.python.org/3/library/profile.html)",
            "火焰图常与 `py-spy`、`snakeviz` 等工具配合使用。",
        ],
        checks=[
            {
                "type": "concept",
                "question": "为什么性能优化前必须先做测量？",
                "answer": "因为性能问题常常不是直觉里最慢的那一段。先测量才能知道真正热点在哪，避免在错误位置浪费时间。",
                "link_text": "为什么学",
                "link_anchor": "为什么学",
            },
            {
                "type": "concept",
                "question": "`timeit` 和 `cProfile` 的使用场景有什么区别？",
                "answer": "`timeit` 更适合微基准和小片段耗时，`cProfile` 更适合从整体调用栈看函数级热点。",
                "link_text": "学什么",
                "link_anchor": "学什么",
            },
            {
                "type": "concept",
                "question": "逐行分析工具为什么通常不应该作为第一步？",
                "answer": "因为逐行分析成本更高、信息更细。通常先用粗粒度工具定位热点区域，再决定是否下钻到逐行或内存层面。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "coding",
                "question": "如何用 `cProfile` 快速查看最耗时的几个函数？",
                "answer": "创建 `Profile()`，在 `enable()` 和 `disable()` 之间执行目标函数，再通过 `pstats.Stats(...).sort_stats(\"cumulative\").print_stats(n)` 输出热点列表。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "coding",
                "question": "如果某些性能分析库在当前环境未安装，示例代码怎样才能仍然安全运行？",
                "answer": "可以像本节示例那样用 `try/except ImportError` 做可选导入，把工具缺失当成能力降级而不是直接崩溃。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "scenario",
                "question": "测试报告生成变慢了，你应该直接优化模板渲染，还是先做 profile？",
                "answer": "先做 profile。慢点可能不在模板渲染，而在数据聚合、文件 I/O、序列化或排序阶段。没有证据就下手优化，常常会偏离真正瓶颈。",
                "link_text": "业界案例",
                "link_anchor": "业界案例",
            },
        ],
    )

    type_hints_and_static_checking = progressive_note(
        title="类型提示与静态检查",
        tags=["python", "typing", "mypy", "protocol", "pydantic"],
        why=[
            "Python 动态灵活，但项目一大、团队一多，接口边界不清晰就会成为维护成本来源。",
            "类型提示不是为了追求形式主义，而是为了让 IDE、静态检查和数据校验工具更早发现问题。",
            "测试框架、工具脚本和业务 SDK 一旦加上稳定的类型边界，重构与协作都会轻松很多。",
        ],
        what=[
            "`typing` 提供 `list[str]`、`Literal`、`TypedDict`、`Protocol`、`Callable` 等表达能力。",
            "`mypy` 严格模式能在提交前发现返回值不匹配、可选值漏判空、接口不一致等问题。",
            "`pydantic` 在运行时做结构化数据验证，与静态类型形成互补。",
        ],
        how=md(
            f"""
            ### 示例 1：`TypedDict` 与 `Protocol`

            {code_block("python", '''
            from typing import Protocol, TypedDict


            class UserPayload(TypedDict):
                name: str
                age: int


            class Renderer(Protocol):
                def render(self, payload: UserPayload) -> str:
                    ...


            class JsonRenderer:
                def render(self, payload: UserPayload) -> str:
                    return f"{payload['name']}:{payload['age']}"


            payload: UserPayload = {"name": "alice", "age": 18}
            print(JsonRenderer().render(payload))
            '''.strip(), 'hl_lines="4 8 12 17"')}

            ### 示例 2：可选导入 `pydantic`

            {code_block("python", '''
            try:
                from pydantic import BaseModel
            except ImportError:
                BaseModel = None


            if BaseModel is not None:
                class UserModel(BaseModel):
                    name: str
                    age: int


                user = UserModel(name="bob", age=20)
                print(user.model_dump())
            else:
                print({"name": "bob", "age": 20})
            '''.strip(), 'hl_lines="1 7 12"')}

            ### 示例 3：mypy 严格模式建议

            {code_block("ini", '''
            [mypy]
            python_version = 3.11
            strict = True
            warn_unused_ignores = True
            ''')}

            落地建议:
            - 先给公共函数、工具层和核心数据结构加类型，再逐步扩展到业务层。
            - 对外部输入数据，静态类型提示不够，仍要用运行时校验兜底。
            - 团队启用 `mypy` 时建议分阶段推进，先从 `basic` 约束逐步走向 `strict`。
            """
        ),
        cases=[
            "接口客户端 SDK 里，类型提示能让调用者更早发现参数遗漏或返回值结构变化。",
            "测试数据工厂、页面对象和公共断言函数一旦有类型边界，IDE 跳转和补全体验会明显提升。",
            "数据校验场景里，Pydantic 常作为请求/响应模型和配置模型的运行时守门员。",
        ],
        extra_reading=[
            "[typing 文档](https://docs.python.org/3/library/typing.html)",
            "[mypy 文档](https://mypy.readthedocs.io/)",
            "[Pydantic 文档](https://docs.pydantic.dev/)",
        ],
        checks=[
            {
                "type": "concept",
                "question": "静态类型检查和运行时数据校验为什么是互补关系？",
                "answer": "静态检查主要在编码和提交阶段发现接口不一致；运行时校验负责处理外部输入和真实数据。前者保证开发体验，后者保证生产边界安全。",
                "link_text": "为什么学",
                "link_anchor": "为什么学",
            },
            {
                "type": "concept",
                "question": "`TypedDict` 和普通 `dict` 注解相比，多了什么表达能力？",
                "answer": "`TypedDict` 能精确描述字典有哪些键、每个键是什么类型，更适合表达结构化 JSON 或配置对象。",
                "link_text": "学什么",
                "link_anchor": "学什么",
            },
            {
                "type": "concept",
                "question": "`Protocol` 为什么适合表达“鸭子类型”接口？",
                "answer": "因为它关心对象是否实现了某组方法，而不强制要求继承某个基类，特别适合抽象可替换能力。",
                "link_text": "学什么",
                "link_anchor": "学什么",
            },
            {
                "type": "coding",
                "question": "如何给一个 JSON 风格字典定义清晰类型？",
                "answer": "优先考虑 `TypedDict`，如果还需要运行时验证，则再用 Pydantic 模型承接外部输入。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "coding",
                "question": "团队刚引入 `mypy` 时，为什么不建议直接要求所有仓库一夜之间 `strict`？",
                "answer": "因为存量告警会非常多，容易让团队失去推进信心。更可行的做法是先限制新增代码，再逐步提升规则级别。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "scenario",
                "question": "你的接口测试项目经常因为响应字段缺失才在运行时崩溃，类型提示和 Pydantic 可以怎样配合改进？",
                "answer": "先用类型提示定义预期结构，让调用方清楚字段边界；再用 Pydantic 在解析响应时做运行时验证，把错误尽早且明确地暴露出来。",
                "link_text": "业界案例",
                "link_anchor": "业界案例",
            },
        ],
    )

    testing_pyramid_and_pytest = progressive_note(
        title="测试金字塔、pytest fixture、参数化与 CI",
        tags=["python", "pytest", "testing", "mock", "coverage"],
        why=[
            "测试工程不是堆更多用例，而是让不同层级的测试承担正确职责。",
            "理解测试金字塔能帮助你决定哪些能力放在单元测试、哪些放在集成测试、哪些再上升到 UI 或端到端层。",
            "Pytest 之所以流行，不只是语法简洁，还因为 fixture、参数化、mock 和插件生态足够成熟。",
        ],
        what=[
            "金字塔强调底层测试多、上层测试少且精，避免把所有成本都压到 UI 回归上。",
            "Pytest 核心能力包括 fixture、参数化、marker、mock、覆盖率统计和与 CI 的无缝集成。",
            "好的测试不止“能跑”，还要稳定、可维护、反馈快、失败信息清晰。",
        ],
        how=md(
            f"""
            ### 示例 1：fixture 与参数化

            {code_block("python", '''
            import pytest


            @pytest.fixture
            def base_url() -> str:
                return "https://example.com"


            @pytest.mark.parametrize(
                "path, expected",
                [("/health", 200), ("/docs", 200)],
            )
            def test_endpoint_meta(base_url: str, path: str, expected: int) -> None:
                assert expected == 200
                assert path.startswith("/")
                assert base_url.startswith("https://")
            '''.strip(), 'hl_lines="4 8 11"')}

            ### 示例 2：mock

            {code_block("python", '''
            from unittest.mock import Mock

            notifier = Mock()
            notifier.send.return_value = True

            result = notifier.send("done")
            print(result, notifier.send.call_count)
            '''.strip(), 'hl_lines="4 6"')}

            ### 示例 3：GitHub Actions 片段

            {code_block("yaml", '''
            name: python-tests
            on: [push, pull_request]
            jobs:
              test:
                runs-on: ubuntu-latest
                steps:
                  - uses: actions/checkout@v4
                  - uses: actions/setup-python@v5
                    with:
                      python-version: "3.11"
                  - run: pip install -r requirements.txt
                  - run: pytest --cov
            ''')}

            落地建议:
            - 单元测试覆盖纯逻辑和边界条件，集成测试覆盖模块协作，UI 测试覆盖关键主流程。
            - fixture 用来管理共享上下文，避免复制初始化代码。
            - 覆盖率只是护栏，不是目标；别为了数字写无意义断言。
            """
        ),
        cases=[
            "中后台系统常把大部分校验下沉到单元和接口层，只保留少量关键 UI 冒烟。",
            "CI 流水线通常在 PR 阶段运行单元与快速集成测试，在夜间任务中补跑重型回归。",
            "Mock 适合隔离邮件、短信、第三方回调等不稳定外部依赖。",
        ],
        extra_reading=[
            "[pytest 文档](https://docs.pytest.org/)",
            "[unittest.mock 文档](https://docs.python.org/3/library/unittest.mock.html)",
            "[coverage.py 文档](https://coverage.readthedocs.io/)",
        ],
        checks=[
            {
                "type": "concept",
                "question": "测试金字塔想解决的核心问题是什么？",
                "answer": "它想解决“测试越往上越昂贵、越脆弱”的问题，鼓励把大部分验证放在反馈更快、维护成本更低的底层测试中。",
                "link_text": "为什么学",
                "link_anchor": "为什么学",
            },
            {
                "type": "concept",
                "question": "fixture 为什么是 Pytest 的核心能力？",
                "answer": "因为它能把测试准备和清理逻辑复用起来，既减少重复，也让依赖关系通过函数签名显式呈现。",
                "link_text": "学什么",
                "link_anchor": "学什么",
            },
            {
                "type": "concept",
                "question": "为什么覆盖率不能替代测试质量？",
                "answer": "因为覆盖率只说明代码被执行过，不说明断言是否有价值，也不说明关键业务路径是否被正确验证。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "coding",
                "question": "怎样把同一条断言逻辑在多组数据上重复执行？",
                "answer": "使用 `@pytest.mark.parametrize`。它能让测试数据显式列在装饰器里，失败时也更容易定位是哪组参数出问题。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "coding",
                "question": "什么时候应该优先使用 mock？",
                "answer": "当测试目标是当前模块自身逻辑，而外部依赖会让测试变慢、不稳定或难以构造时，优先用 mock 隔离边界。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "scenario",
                "question": "团队的 UI 回归越来越慢、越来越不稳定，应该怎么按金字塔思路调整？",
                "answer": "先把可下沉的校验迁到单元和接口层，把 UI 层缩成关键主路径验证；同时梳理 fixture、数据构造和并行执行，减少上层测试的冗余与脆弱点。",
                "link_text": "业界案例",
                "link_anchor": "业界案例",
            },
        ],
    )

    packaging_toml_block = code_block("toml", '''
            [build-system]
            requires = ["setuptools>=68", "wheel"]
            build-backend = "setuptools.build_meta"

            [project]
            name = "qa-tools"
            version = "0.1.0"
            description = "Utilities for test automation"
            requires-python = ">=3.8"
            ''')
    packaging_version_block = code_block("python", '''
            import re

            version = "1.4.2"
            pattern = re.compile(r"^(\\d+)\\.(\\d+)\\.(\\d+)$")
            match = pattern.match(version)

            assert match is not None
            print(tuple(int(part) for part in match.groups()))
            '''.strip(), 'hl_lines="4 6 7"')
    packaging_publish_block = code_block("bash", r'''
            python -m pip install --upgrade build twine
            python -m build
            twine check dist/*
            twine upload --repository-url https://pypi.example.com/simple/ dist/*
            '''.strip())
    packaging_and_publishing = progressive_note(
        title="打包发布：setuptools、wheel、twine 与私有 PyPI",
        tags=["python", "packaging", "wheel", "twine", "pep517"],
        why=[
            "当脚本开始被多个仓库复用时，复制粘贴会迅速变成维护噩梦，打包发布是把代码升级为可分发能力的关键一步。",
            "理解构建、分发、安装三个阶段的边界，能帮助你在工具脚本、SDK 和测试框架之间形成稳定交付链路。",
            "即使不公开发布到 PyPI，私有源和内部包管理在团队协作中也非常常见。",
        ],
        what=[
            "`pyproject.toml`、PEP 517、PEP 518 负责描述构建后端和项目元数据。",
            "`wheel` 是常见二进制分发格式，`twine` 负责安全上传构建产物。",
            "语义化版本号通过 `MAJOR.MINOR.PATCH` 表达兼容性变化，是团队发布协作的基础语言。",
        ],
        how=md(
            """
            ### 示例 1：最小 `pyproject.toml`

            {packaging_toml_block}

            ### 示例 2：版本号校验脚本

            {packaging_version_block}

            ### 示例 3：构建与发布命令

            {packaging_publish_block}

            发布建议:
            - 新项目优先用 `pyproject.toml`，避免旧式 `setup.py` 配置分散。
            - 先在测试环境或私有源验证安装链路，再决定是否提升版本并正式发布。
            - 对外发布遵循语义化版本；对内发布也建议保留清晰版本节奏和变更记录。
            """.format(
                packaging_toml_block=packaging_toml_block,
                packaging_version_block=packaging_version_block,
                packaging_publish_block=packaging_publish_block,
            )
        ),
        cases=[
            "团队会把公共 API 客户端、测试数据工具和报告 SDK 打成内部包，供多个仓库复用。",
            "CI 常在打 tag 后自动构建 wheel，并发布到私有 PyPI 或制品仓库。",
            "版本号语义清晰时，调用方能更快判断升级是否涉及破坏性变更。",
        ],
        extra_reading=[
            "[Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)",
            "[PEP 517](https://peps.python.org/pep-0517/)",
            "[PEP 518](https://peps.python.org/pep-0518/)",
        ],
        checks=[
            {
                "type": "concept",
                "question": "构建、分发、安装三个阶段分别关注什么？",
                "answer": "构建生成可分发产物，分发负责把产物上传到仓库，安装则是调用方从仓库拉取并装到环境里。三者是相邻但不同的链路阶段。",
                "link_text": "为什么学",
                "link_anchor": "为什么学",
            },
            {
                "type": "concept",
                "question": "为什么现代 Python 项目更推荐 `pyproject.toml`？",
                "answer": "因为它把构建系统和项目元数据集中到一个标准文件里，更符合新工具链，也更容易被生态统一识别。",
                "link_text": "学什么",
                "link_anchor": "学什么",
            },
            {
                "type": "concept",
                "question": "语义化版本号里何时应该升级主版本？",
                "answer": "当你引入不向后兼容的变更时，应该提升主版本号。新增兼容功能升次版本，兼容性修复升补丁版本。",
                "link_text": "学什么",
                "link_anchor": "学什么",
            },
            {
                "type": "coding",
                "question": "如何在脚本里粗略校验一个版本号是否符合 `MAJOR.MINOR.PATCH`？",
                "answer": "可以像示例 2 那样用正则 `^(\\d+)\\.(\\d+)\\.(\\d+)$` 匹配，再把各段转成整数。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "coding",
                "question": "构建 wheel 并检查发布包通常需要哪几步？",
                "answer": "先安装 `build` 和 `twine`，执行 `python -m build` 构建产物，再用 `twine check dist/*` 做基础校验，最后上传到目标仓库。",
                "link_text": "怎么用",
                "link_anchor": "怎么用",
            },
            {
                "type": "scenario",
                "question": "你们团队有多个自动化仓库都在复制同一套公共工具函数，什么时候该考虑打包发布？",
                "answer": "当重复代码已经开始频繁同步、修一个地方要到处手改时，就应该考虑抽出公共包并通过版本发布统一分发，减少维护分叉。",
                "link_text": "业界案例",
                "link_anchor": "业界案例",
            },
        ],
    )

    write("04_progressive_topics/python_re.md", python_re)
    write("04_progressive_topics/python_keywords.md", python_keywords)
    write("04_progressive_topics/python_concurrency.md", python_concurrency)
    write("04_progressive_topics/python_profiling.md", python_profiling)
    write("04_progressive_topics/type_hints_and_static_checking.md", type_hints_and_static_checking)
    write("04_progressive_topics/testing_pyramid_and_pytest.md", testing_pyramid_and_pytest)
    write("04_progressive_topics/packaging_and_publishing.md", packaging_and_publishing)


def build_readme() -> None:
    content = md(
        """
        # Python 学习笔记体系

        > 面向测试工程师的 Python 系统学习路径，覆盖环境搭建、语言基础、高级语法与工程化专题。

        ## 学习路径

        | 阶段 | 目录 | 目标 | 预计时长 | 前置知识 |
        | :--- | :--- | :--- | :--- | :--- |
        | 环境篇 | `01_environment/` | 配好解释器、依赖管理和 IDE 调试体验 | 4-6 小时 | 基本命令行操作 |
        | 基础语法篇 | `02_basic_syntax/` | 建立数据类型、流程控制、容器与函数基础 | 10-14 小时 | 环境篇 |
        | 高级语法篇 | `03_advanced_syntax/` | 掌握生成器、装饰器、上下文管理器、OOP 与异常体系 | 12-16 小时 | 基础语法篇 |
        | 进阶专题篇 | `04_progressive_topics/` | 把 Python 能力落到并发、性能、类型、测试与发布链路 | 14-20 小时 | 高级语法篇 |

        ## 建议学习顺序

        1. 先把环境篇走通，确保解释器、依赖与编辑器体验稳定。
        2. 基础语法篇按“变量 -> 运算符 -> 流程控制 -> 字符串 -> 容器 -> 函数”的顺序推进。
        3. 高级语法篇重点理解“抽象边界”和“资源管理”，不要只背语法。
        4. 进阶专题篇按工作场景挑重点，测试工程优先看正则、并发、测试金字塔与类型检查。

        ## 内容索引

        ### 环境篇

        | 主题 | 文件 |
        | :--- | :--- |
        | Python 多版本管理 | [python_version_management.md](./01_environment/python_version_management.md) |
        | pip 与 Poetry 依赖管理 | [dependency_management.md](./01_environment/dependency_management.md) |
        | VS Code 一体化配置 | [ide_setup.md](./01_environment/ide_setup.md) |

        ### 基础语法篇

        | 主题 | 文件 |
        | :--- | :--- |
        | 变量与数据类型 | [variables_and_types.md](./02_basic_syntax/variables_and_types.md) |
        | 运算符与表达式 | [operators_and_expressions.md](./02_basic_syntax/operators_and_expressions.md) |
        | 流程控制 | [control_flow.md](./02_basic_syntax/control_flow.md) |
        | 字符串与常用方法 | [strings_and_methods.md](./02_basic_syntax/strings_and_methods.md) |
        | 列表、元组、集合、字典 | [collections.md](./02_basic_syntax/collections.md) |
        | 函数基础 | [function_basics.md](./02_basic_syntax/function_basics.md) |

        ### 高级语法篇

        | 主题 | 文件 |
        | :--- | :--- |
        | 迭代器、生成器与 yield/send/throw/close | [iterators_and_generators.md](./03_advanced_syntax/iterators_and_generators.md) |
        | 装饰器 | [decorators.md](./03_advanced_syntax/decorators.md) |
        | 上下文管理器 | [context_managers.md](./03_advanced_syntax/context_managers.md) |
        | 面向对象 | [object_oriented_programming.md](./03_advanced_syntax/object_oriented_programming.md) |
        | 异常体系 | [exceptions.md](./03_advanced_syntax/exceptions.md) |
        | 模块与包 | [modules_and_packages.md](./03_advanced_syntax/modules_and_packages.md) |

        ### 进阶专题篇

        | 主题 | 文件 |
        | :--- | :--- |
        | 正则表达式与 re 模块 | [python_re.md](./04_progressive_topics/python_re.md) |
        | Python 关键字全集 | [python_keywords.md](./04_progressive_topics/python_keywords.md) |
        | 并发模型 | [python_concurrency.md](./04_progressive_topics/python_concurrency.md) |
        | 性能剖析 | [python_profiling.md](./04_progressive_topics/python_profiling.md) |
        | 类型提示与静态检查 | [type_hints_and_static_checking.md](./04_progressive_topics/type_hints_and_static_checking.md) |
        | 测试金字塔与 Pytest | [testing_pyramid_and_pytest.md](./04_progressive_topics/testing_pyramid_and_pytest.md) |
        | 打包发布 | [packaging_and_publishing.md](./04_progressive_topics/packaging_and_publishing.md) |

        ## 一键初始化

        ```bash
        cd testing/python_notes
        python -m pip install -r requirements.txt
        pytest tests -q
        ```

        ## 工程化约定

        - 所有笔记使用 GitHub Flavored Markdown。
        - 每篇笔记都包含 front matter、目录锚点、Self-Check、参考答案、参考链接和版本记录。
        - 代码块优先保证“可读、可运行、可复制”，测试脚本会执行所有 `python` 代码块。
        - `images/` 目录按“笔记名_序号.png”维护截图与示意图资源。
        - 根目录 `Makefile` 提供 `install`、`serve`、`test`、`lint`、`format` 等命令入口。

        ## 关联入口

        - 示例校验脚本: [tests/test_markdown_examples.py](./tests/test_markdown_examples.py)
        - 依赖清单: [requirements.txt](./requirements.txt)
        - 常用命令: [Makefile](./Makefile)
        - 知识汇总页: [../../common/docs/indexes/knowledge_hub.md](../../common/docs/indexes/knowledge_hub.md)
        - 模板参考: [../../common/docs/template.md](../../common/docs/template.md)
        """
    )
    write("README.md", content)


def build_requirements() -> None:
    content = md(
        """
        pytest>=8.3,<9.0
        pytest-cov>=5.0,<6.0
        black>=24.4,<25.0
        isort>=5.13,<6.0
        flake8>=7.1,<8.0
        mypy>=1.11,<2.0
        pydantic>=2.8,<3.0
        line-profiler>=4.1,<5.0
        memory-profiler>=0.61,<1.0
        objgraph>=3.6,<4.0
        """
    )
    write("requirements.txt", content)


def build_makefile() -> None:
    content = md(
        """
        PYTHON ?= python
        PORT ?= 8000

        .PHONY: install serve test lint format check

        install:
        	$(PYTHON) -m pip install -r requirements.txt

        serve:
        	$(PYTHON) -m http.server $(PORT) -d .

        test:
        	$(PYTHON) -m pytest tests -q

        lint:
        	$(PYTHON) -m flake8 tests
        	$(PYTHON) -m mypy tests

        format:
        	$(PYTHON) -m isort tests
        	$(PYTHON) -m black tests

        check: test lint
        """
    )
    write("Makefile", content)


def build_test_script() -> None:
    content = dedent(
        """
        from __future__ import annotations

        import re
        from pathlib import Path


        ROOT = Path(__file__).resolve().parent.parent
        NOTE_DIRECTORIES = (
            "01_environment",
            "02_basic_syntax",
            "03_advanced_syntax",
            "04_progressive_topics",
        )
        EXPECTED_FILES = {
            "01_environment": {
                "dependency_management.md",
                "ide_setup.md",
                "python_version_management.md",
            },
            "02_basic_syntax": {
                "collections.md",
                "control_flow.md",
                "function_basics.md",
                "operators_and_expressions.md",
                "strings_and_methods.md",
                "variables_and_types.md",
            },
            "03_advanced_syntax": {
                "context_managers.md",
                "decorators.md",
                "exceptions.md",
                "iterators_and_generators.md",
                "modules_and_packages.md",
                "object_oriented_programming.md",
            },
            "04_progressive_topics": {
                "packaging_and_publishing.md",
                "python_concurrency.md",
                "python_keywords.md",
                "python_profiling.md",
                "python_re.md",
                "testing_pyramid_and_pytest.md",
                "type_hints_and_static_checking.md",
            },
        }
        REQUIRED_HEADINGS = (
            "## 目录",
            "## Self-Check",
            "## 参考答案",
            "## 参考链接",
            "## 版本记录",
        )
        FRONT_MATTER_KEYS = (
            "title:",
            "module:",
            "area:",
            "stack:",
            "level:",
            "status:",
            "tags:",
            "updated:",
        )
        PYTHON_BLOCK_PATTERN = re.compile(r"```python[^\\n]*\\n(.*?)```", re.DOTALL)


        def iter_note_files() -> list[Path]:
            files: list[Path] = []
            for directory in NOTE_DIRECTORIES:
                files.extend(sorted((ROOT / directory).glob("*.md")))
            return files


        def test_expected_files_exist() -> None:
            for directory, expected_names in EXPECTED_FILES.items():
                actual_names = {path.name for path in (ROOT / directory).glob("*.md")}
                assert actual_names == expected_names


        def test_images_directories_exist() -> None:
            for directory in NOTE_DIRECTORIES:
                image_dir = ROOT / directory / "images"
                assert image_dir.is_dir()
                assert (image_dir / "README.md").exists()


        def test_note_front_matter_and_headings() -> None:
            files = iter_note_files()
            assert len(files) == 22

            for note_file in files:
                content = note_file.read_text(encoding="utf-8")
                assert content.startswith("---\\n"), note_file
                for key in FRONT_MATTER_KEYS:
                    assert key in content, f"{note_file} missing {key}"
                for heading in REQUIRED_HEADINGS:
                    assert heading in content, f"{note_file} missing {heading}"


        def test_python_code_blocks_compile_and_run() -> None:
            for note_file in iter_note_files():
                content = note_file.read_text(encoding="utf-8")
                blocks = PYTHON_BLOCK_PATTERN.findall(content)
                assert blocks, f"{note_file} has no python code blocks"

                for block in blocks:
                    namespace = {"__name__": "__markdown_example__"}
                    code = compile(block, str(note_file), "exec")
                    exec(code, namespace, namespace)
        """
    ).lstrip()
    write("tests/test_markdown_examples.py", content)


def build_image_readmes() -> None:
    inventories = {
        "01_environment": [
            "python_version_management_01.png",
            "python_version_management_02.png",
            "python_version_management_03.png",
            "dependency_management_01.png",
            "dependency_management_02.png",
            "dependency_management_03.png",
            "ide_setup_01.png",
            "ide_setup_02.png",
            "ide_setup_03.png",
        ],
        "02_basic_syntax": [
            "variables_and_types_01.png",
            "operators_and_expressions_01.png",
            "control_flow_01.png",
            "strings_and_methods_01.png",
            "collections_01.png",
            "function_basics_01.png",
        ],
        "03_advanced_syntax": [
            "iterators_and_generators_01.png",
            "decorators_01.png",
            "context_managers_01.png",
            "object_oriented_programming_01.png",
            "exceptions_01.png",
            "modules_and_packages_01.png",
        ],
        "04_progressive_topics": [
            "python_re_01.png",
            "python_keywords_01.png",
            "python_concurrency_01.png",
            "python_profiling_01.png",
            "type_hints_and_static_checking_01.png",
            "testing_pyramid_and_pytest_01.png",
            "packaging_and_publishing_01.png",
        ],
    }
    for directory, files in inventories.items():
        content = md(
            "# Images\n\n"
            "本目录用于保存该阶段笔记配套截图与示意图资源。\n\n"
            "命名约定:\n"
            + "\n".join(f"- `{name}`" for name in files)
            + "\n\n建议规范:\n"
            "- PNG 格式\n"
            "- 建议按照 4K 截图后再缩放到 50%\n"
            "- 一张图只表达一个关键步骤，优先展示命令、输出和关键配置项\n"
        )
        write(f"{directory}/images/README.md", content)


def main() -> None:
    build_environment_notes()
    build_basic_notes()
    build_advanced_notes()
    build_progressive_notes()
    build_readme()
    build_requirements()
    build_makefile()
    build_test_script()
    build_image_readmes()


if __name__ == "__main__":
    main()
