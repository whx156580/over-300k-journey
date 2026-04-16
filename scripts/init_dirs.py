from pathlib import Path
import argparse


CONTENT_LAYERS = ("basics", "advanced", "projects", "interview", "assets")


def layered_topic(extra_children=None):
    children = {name: {} for name in CONTENT_LAYERS}
    for name in extra_children or ():
        children[name] = {}
    return children


PROJECT_STRUCTURE = {
    "testing": {
        "ui": {
            "playwright": layered_topic(),
            "selenium": layered_topic(),
        },
        "api": {
            "pytest": layered_topic(("tests",)),
            "rest-assured": layered_topic(),
        },
        "mobile": {
            "appium": layered_topic(),
        },
        "performance": {
            "k6": layered_topic(),
            "jmeter": layered_topic(),
        },
        "ai-eval": {
            "ragas": layered_topic(),
            "deepeval": layered_topic(),
        },
        "strategy": {
            "methodologies": {},
            "quality-gates": {},
            "metrics": {},
            "templates": {},
            "tests": {},
        },
        "python_notes": {
            "01_environment": {},
            "02_basic_syntax": {},
            "03_standard_library": {},
            "04_testing_basics": {},
        },
    },
    "frontend": {
        "frameworks": {
            "react": layered_topic(),
            "vue": layered_topic(),
            "typescript": layered_topic(),
            "cross-platform": layered_topic(),
        },
        "engineering": {
            "build-tools": layered_topic(),
            "ci-cd": layered_topic(),
            "testing": layered_topic(),
            "lint-format": layered_topic(),
        },
        "performance": {
            "web-vitals": layered_topic(),
            "lighthouse": layered_topic(),
            "optimization": layered_topic(),
        },
    },
    "backend": {
        "distributed": {
            "microservices": layered_topic(),
            "messaging": layered_topic(),
            "caching": layered_topic(),
            "resilience": layered_topic(),
        },
        "database": {
            "mysql": layered_topic(),
            "redis": layered_topic(),
            "mongodb": layered_topic(),
            "design-and-tuning": layered_topic(),
        },
        "system-design": {
            "high-availability": layered_topic(),
            "scalability": layered_topic(),
            "observability": layered_topic(),
            "case-studies": layered_topic(),
        },
    },
    "ai": {
        "llm-agent": {
            "prompt": layered_topic(),
            "rag": layered_topic(),
            "agent": layered_topic(),
            "safety": layered_topic(),
        },
        "mlops": {
            "training": layered_topic(),
            "deployment": layered_topic(),
            "monitoring": layered_topic(),
            "feature-store": layered_topic(),
        },
        "dataset": {
            "collection": layered_topic(),
            "cleaning": layered_topic(),
            "annotation": layered_topic(),
            "evaluation-data": layered_topic(),
        },
    },
    "common": {
        "checklists": {},
        "snippets": {
            "python": {},
            "javascript": {},
            "sql": {},
            "shell": {},
        },
        "tools": {},
        "docs": {
            "architecture": {},
            "standards": {},
            "roadmaps": {},
            "indexes": {},
        },
    },
    "scripts": {},
}


def ensure_gitkeep(directory: Path) -> bool:
    gitkeep = directory / ".gitkeep"
    if gitkeep.exists():
        return False

    gitkeep.touch()
    return True


def create_tree(base_path: Path, tree: dict, stats: dict, with_gitkeep: bool) -> None:
    for name, children in tree.items():
        current = base_path / name
        if not current.exists():
            current.mkdir(parents=True, exist_ok=True)
            stats["created_dirs"] += 1
            print(f"[Created] {current}")

        if children:
            create_tree(current, children, stats, with_gitkeep)
        elif with_gitkeep and ensure_gitkeep(current):
            stats["created_gitkeep"] += 1
            print(f"  [Added] {current / '.gitkeep'}")


def init_project_structure(with_gitkeep: bool = False):
    stats = {"created_dirs": 0, "created_gitkeep": 0}
    root = Path(__file__).resolve().parent.parent

    print("Starting knowledge base structure initialization...")
    create_tree(root, PROJECT_STRUCTURE, stats, with_gitkeep)

    if with_gitkeep:
        summary = (
            "Initialization completed: "
            f"{stats['created_dirs']} directories created, "
            f"{stats['created_gitkeep']} .gitkeep files added."
        )
    else:
        summary = (
            "Initialization completed: "
            f"{stats['created_dirs']} directories created. "
            "No .gitkeep files were generated."
        )

    print(summary)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize the knowledge base directory structure.")
    parser.add_argument(
        "--with-gitkeep",
        action="store_true",
        help="Also create .gitkeep placeholder files for empty leaf directories.",
    )
    args = parser.parse_args()
    init_project_structure(with_gitkeep=args.with_gitkeep)
