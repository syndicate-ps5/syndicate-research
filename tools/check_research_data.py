#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Prüft Forschungsdaten, Quellen-IDs und interne Markdown-Links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "research.json"
SCHEMA = ROOT / "data" / "schema.json"
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"FAIL {message}")
    raise SystemExit(1)


def check_schema() -> dict:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    document = json.loads(DATA.read_text(encoding="utf-8"))
    errors = sorted(
        Draft202012Validator(schema).iter_errors(document),
        key=lambda item: list(item.absolute_path),
    )
    if errors:
        rendered = "; ".join(
            f"{'/'.join(map(str, error.absolute_path))}: {error.message}" for error in errors
        )
        fail(f"JSON-Schema: {rendered}")
    print("PASS JSON-Schema")
    return document


def check_source_ids(document: dict) -> None:
    sources = document["sources"]
    identifiers = [source["id"] for source in sources]
    duplicates = sorted({item for item in identifiers if identifiers.count(item) > 1})
    if duplicates:
        fail(f"doppelte Quellen-IDs: {', '.join(duplicates)}")
    known = set(identifiers)
    used: set[str] = set()

    def require(source_id: str, where: str) -> None:
        used.add(source_id)
        if source_id not in known:
            fail(f"{where} verweist auf unbekannte Quelle {source_id}")

    for model in document["models"]:
        for statement in model["statements"] + model["retailModelNumbers"]:
            require(statement["sourceId"], model["id"])
    for firmware in document["firmware"]:
        require(firmware["sourceId"], firmware["id"])
        for statement in firmware["quotedStatements"]:
            require(statement["sourceId"], firmware["id"])
    for entry in document["compatibility"]["entries"]:
        require(entry["sourceId"], entry["id"])

    unused = known - used
    for source in sources:
        if source["id"] in unused and "assignmentNote" not in source:
            fail(f"{source['id']} ist keiner Aussage zugeordnet und hat keine assignmentNote")
    print(f"PASS Quellen-IDs ({len(known)} Quellen, {len(used)} verwendet)")


def check_markdown_links() -> None:
    missing: list[str] = []
    checked = 0
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for match in LINK.finditer(text):
            target = match.group(1).split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            checked += 1
            destination = (path.parent / target).resolve()
            if not destination.exists():
                missing.append(f"{path.relative_to(ROOT)} -> {target}")
    if missing:
        fail("interne Markdown-Links: " + "; ".join(missing))
    print(f"PASS interne Markdown-Links ({checked} geprüft)")


def main() -> None:
    document = check_schema()
    check_source_ids(document)
    check_markdown_links()


if __name__ == "__main__":
    sys.exit(main())
