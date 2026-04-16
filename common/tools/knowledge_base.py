from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


FRONT_MATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


@dataclass
class KnowledgeEntry:
    title: str
    module: str
    area: str
    stack: str
    level: str
    status: str
    tags: list[str]
    updated: str
    path: Path
    body: str
    modified_at: float

    @property
    def relative_path(self) -> str:
        return self.path.as_posix()


def parse_front_matter(content: str) -> tuple[dict[str, object], str]:
    match = FRONT_MATTER_PATTERN.match(content)
    if not match:
        return {}, content

    raw_front_matter = match.group(1)
    body = content[match.end():]
    metadata: dict[str, object] = {}

    for line in raw_front_matter.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if value.startswith("[") and value.endswith("]"):
            items = [item.strip().strip("\"'") for item in value[1:-1].split(",")]
            metadata[key] = [item for item in items if item]
        else:
            metadata[key] = value.strip("\"'")

    return metadata, body


def load_knowledge_entries(root: Path, modules: Iterable[str] | None = None) -> list[KnowledgeEntry]:
    targets = list(modules or ("testing", "frontend", "backend", "ai"))
    entries: list[KnowledgeEntry] = []

    for module_name in targets:
        module_path = root / module_name
        if not module_path.exists():
            continue

        for file_path in module_path.rglob("*.md"):
            if file_path.name.lower() == "readme.md":
                continue

            content = file_path.read_text(encoding="utf-8")
            metadata, body = parse_front_matter(content)
            if not metadata:
                continue

            entries.append(
                KnowledgeEntry(
                    title=str(metadata.get("title", file_path.stem)),
                    module=str(metadata.get("module", module_name)),
                    area=str(metadata.get("area", "")),
                    stack=str(metadata.get("stack", "")),
                    level=str(metadata.get("level", "")),
                    status=str(metadata.get("status", "")),
                    tags=[str(tag) for tag in metadata.get("tags", [])],
                    updated=str(metadata.get("updated", "")),
                    path=file_path.relative_to(root),
                    body=body,
                    modified_at=file_path.stat().st_mtime,
                )
            )

    return sorted(entries, key=lambda entry: (entry.module, entry.area, entry.stack, entry.level, entry.title))


def make_excerpt(body: str, query: str = "", length: int = 120) -> str:
    normalized = re.sub(r"\s+", " ", body).strip()
    if not normalized:
        return ""

    if query:
        lowered = normalized.lower()
        index = lowered.find(query.lower())
        if index != -1:
            start = max(0, index - 30)
            end = min(len(normalized), index + length)
            return normalized[start:end].strip()

    return normalized[:length].strip()
