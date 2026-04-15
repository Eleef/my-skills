#!/usr/bin/env python3
"""
Read bounded YAML front matter from managed markdown docs.

This helper supports metadata-first triage without loading full document bodies.
It intentionally caps bytes, lines, file count, and returned field length so the
caller can inspect many docs safely before deciding which bodies to open.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

MAX_FRONT_MATTER_BYTES = 8192
MAX_FRONT_MATTER_LINES = 80
MAX_FILES_DEFAULT = 200
MAX_VALUE_LENGTH = 280
ALLOWED_SUFFIXES = {".md", ".markdown"}
DEFAULT_KEYS = [
    "name",
    "description",
    "kind",
    "scope",
    "lifecycle",
    "authority",
    "summary",
    "updated_at",
]


def clip(value: str, limit: int = MAX_VALUE_LENGTH) -> str:
    text = " ".join(value.strip().split())
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def parse_front_matter(path: Path) -> dict:
    result = {
        "path": str(path),
        "has_front_matter": False,
        "truncated": False,
        "error": None,
        "metadata": {},
    }
    try:
        with path.open("r", encoding="utf-8") as handle:
            first = handle.readline()
            if first.strip() != "---":
                return result

            result["has_front_matter"] = True
            lines = []
            total_bytes = len(first.encode("utf-8"))
            for index, line in enumerate(handle, start=1):
                total_bytes += len(line.encode("utf-8"))
                if total_bytes > MAX_FRONT_MATTER_BYTES or index > MAX_FRONT_MATTER_LINES:
                    result["truncated"] = True
                    break
                if line.strip() == "---":
                    break
                lines.append(line.rstrip("\n"))
            else:
                result["error"] = "front_matter_not_closed"
                return result

        metadata = {}
        for raw in lines:
            stripped = raw.strip()
            if not stripped or stripped.startswith("#") or ":" not in raw:
                continue
            key, value = raw.split(":", 1)
            metadata[key.strip()] = clip(value.strip().strip("'\""))
        result["metadata"] = metadata
        return result
    except UnicodeDecodeError:
        result["error"] = "decode_error"
        return result
    except OSError as exc:
        result["error"] = str(exc)
        return result


def iter_markdown_files(target: Path, recursive: bool) -> list[Path]:
    if target.is_file():
        return [target]
    pattern = "**/*" if recursive else "*"
    files = [
        path
        for path in target.glob(pattern)
        if path.is_file() and path.suffix.lower() in ALLOWED_SUFFIXES
    ]
    files.sort()
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description="List bounded YAML front matter for markdown docs.")
    parser.add_argument("target", nargs="?", default=".", help="File or directory to inspect.")
    parser.add_argument("--recursive", action="store_true", help="Recurse into subdirectories.")
    parser.add_argument("--max-files", type=int, default=MAX_FILES_DEFAULT, help="Maximum number of files to inspect.")
    parser.add_argument(
        "--keys",
        default=",".join(DEFAULT_KEYS),
        help="Comma-separated metadata keys to keep in output. Use '*' for all parsed keys.",
    )
    args = parser.parse_args()

    target = Path(args.target).resolve()
    if not target.exists():
        print(json.dumps({"error": f"target_not_found: {target}"}))
        return 1

    keep_all = args.keys.strip() == "*"
    wanted_keys = {key.strip() for key in args.keys.split(",") if key.strip()}
    files = iter_markdown_files(target, args.recursive)
    limited_files = files[: max(args.max_files, 0)]

    results = []
    for path in limited_files:
        entry = parse_front_matter(path)
        if not keep_all:
            entry["metadata"] = {
                key: value for key, value in entry["metadata"].items() if key in wanted_keys
            }
        results.append(entry)

    payload = {
        "target": str(target),
        "recursive": args.recursive,
        "returned_files": len(results),
        "total_candidate_files": len(files),
        "truncated_file_list": len(files) > len(limited_files),
        "limits": {
            "max_files": args.max_files,
            "max_front_matter_bytes": MAX_FRONT_MATTER_BYTES,
            "max_front_matter_lines": MAX_FRONT_MATTER_LINES,
            "max_value_length": MAX_VALUE_LENGTH,
        },
        "results": results,
    }
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
