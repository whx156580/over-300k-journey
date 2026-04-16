from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common.tools.knowledge_base import load_knowledge_entries, make_excerpt


def score_entry(entry, query: str) -> int:
    if not query:
        return 1

    score = 0
    lowered_query = query.lower()
    title = entry.title.lower()
    tags = " ".join(entry.tags).lower()
    path = entry.relative_path.lower()
    body = entry.body.lower()

    if lowered_query in title:
        score += 5
    if lowered_query in tags:
        score += 4
    if lowered_query in path:
        score += 3
    if lowered_query in body:
        score += 1

    return score


def main() -> int:
    parser = argparse.ArgumentParser(description="Search structured knowledge notes.")
    parser.add_argument("query", nargs="?", default="", help="Keyword to search in title, tags, path, and body.")
    parser.add_argument("--module", help="Filter by module, for example testing or frontend.")
    parser.add_argument("--area", help="Filter by area, for example ui or api.")
    parser.add_argument("--stack", help="Filter by stack, for example playwright or pytest.")
    parser.add_argument("--tag", help="Filter by tag, for example rag or performance.")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of results to print.")
    parser.add_argument("--json", action="store_true", help="Print results as JSON.")
    args = parser.parse_args()

    entries = load_knowledge_entries(ROOT)

    filtered = []
    for entry in entries:
        if args.module and entry.module != args.module:
            continue
        if args.area and entry.area != args.area:
            continue
        if args.stack and entry.stack != args.stack:
            continue
        if args.tag and args.tag not in entry.tags:
            continue

        score = score_entry(entry, args.query)
        if args.query and score == 0:
            continue

        filtered.append((score, entry))

    filtered.sort(key=lambda item: (-item[0], item[1].title))
    filtered = filtered[: args.limit]

    if args.json:
        payload = [
            {
                "title": entry.title,
                "module": entry.module,
                "area": entry.area,
                "stack": entry.stack,
                "level": entry.level,
                "tags": entry.tags,
                "updated": entry.updated,
                "path": entry.relative_path,
                "score": score,
                "excerpt": make_excerpt(entry.body, args.query),
            }
            for score, entry in filtered
        ]
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    if not filtered:
        print("No knowledge notes matched your query.")
        return 0

    for index, (score, entry) in enumerate(filtered, start=1):
        print(f"[{index}] {entry.title}")
        print(f"    score : {score}")
        print(f"    scope : {entry.module}/{entry.area}/{entry.stack}/{entry.level}")
        print(f"    tags  : {', '.join(entry.tags) if entry.tags else '-'}")
        print(f"    path  : {entry.relative_path}")
        print(f"    note  : {make_excerpt(entry.body, args.query)}")
        print("")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
