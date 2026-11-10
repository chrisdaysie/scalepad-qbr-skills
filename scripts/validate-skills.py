#!/usr/bin/env python3
"""Validate portable single-file skills and their repository references."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"
NAME_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
README_VERSION_PATTERN = re.compile(r"^\| \*\*Release\*\* \| (?P<version>[0-9]+\.[0-9]+\.[0-9]+) · .+ \|$", re.MULTILINE)
FRONTMATTER_PATTERN = re.compile(r"\A---\n(?P<fields>.*?)\n---(?:\n|\Z)", re.DOTALL)
SKILL_REFERENCE_PATTERN = re.compile(r"`/([a-z0-9]+(?:-[a-z0-9]+)*)`")
README_LINK_PATTERN = re.compile(r"\]\((skills/[a-z0-9-]+\.md)\)")


def parse_frontmatter(content: str, path: Path) -> dict[str, str]:
    match = FRONTMATTER_PATTERN.match(content)
    if not match:
        raise ValueError(f"{path}: missing or malformed YAML frontmatter")

    fields: dict[str, str] = {}
    for line in match.group("fields").splitlines():
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        if not separator or not key.strip() or not value.strip():
            raise ValueError(f"{path}: frontmatter must use one-line key-value fields")
        fields[key.strip()] = value.strip()
    return fields


def validate() -> list[str]:
    errors: list[str] = []
    skill_paths = sorted(SKILLS_DIR.glob("*.md"))
    if not skill_paths:
        return [f"{SKILLS_DIR}: no skill files found"]

    names: set[str] = set()
    contents: dict[str, str] = {}

    for path in skill_paths:
        content = path.read_text(encoding="utf-8")
        contents[path.stem] = content
        try:
            fields = parse_frontmatter(content, path)
        except ValueError as error:
            errors.append(str(error))
            continue

        unexpected = set(fields) - {"name", "description"}
        if unexpected:
            errors.append(f"{path}: unsupported frontmatter fields: {', '.join(sorted(unexpected))}")

        name = fields.get("name", "")
        description = fields.get("description", "")
        if not NAME_PATTERN.fullmatch(name) or len(name) > 64:
            errors.append(f"{path}: invalid skill name {name!r}")
        if name != path.stem:
            errors.append(f"{path}: name must match filename {path.stem!r}")
        if name in names:
            errors.append(f"{path}: duplicate skill name {name!r}")
        names.add(name)

        if not description or len(description) > 1024:
            errors.append(f"{path}: description must contain 1-1024 characters")
        if "[TODO:" in content or "FIXME" in content:
            errors.append(f"{path}: unfinished placeholder found")

    for source_name, content in contents.items():
        for reference in SKILL_REFERENCE_PATTERN.findall(content):
            if reference not in names:
                errors.append(f"skills/{source_name}.md: missing referenced skill /{reference}")

    if not README.exists():
        errors.append(f"{README}: missing")
        return errors

    readme = README.read_text(encoding="utf-8")
    version_match = README_VERSION_PATTERN.search(readme)
    if not version_match:
        errors.append("README.md: missing Semantic Versioning release line")
    elif f"### {version_match.group('version')} ·" not in readme:
        errors.append("README.md: current version is missing from its Changelog")
    linked_skills: set[str] = set()
    for relative_link in README_LINK_PATTERN.findall(readme):
        target = ROOT / relative_link
        if not target.is_file():
            errors.append(f"README.md: broken link {relative_link}")
        linked_skills.add(target.stem)

    for missing_name in sorted(names - linked_skills):
        errors.append(f"README.md: skill /{missing_name} is missing from the catalog")

    return errors


def self_check() -> None:
    sample = "---\nname: sample-skill\ndescription: Sample.\n---\n"
    assert parse_frontmatter(sample, Path("sample.md"))["name"] == "sample-skill"
    assert NAME_PATTERN.fullmatch("sample-skill")
    assert not NAME_PATTERN.fullmatch("Sample_Skill")
    assert README_VERSION_PATTERN.search("| **Release** | 1.0.0 · 10 November 2026 |")
    assert not README_VERSION_PATTERN.search("| **Release** | v1 |")


if __name__ == "__main__":
    self_check()
    validation_errors = validate()
    if validation_errors:
        print("\n".join(f"ERROR: {error}" for error in validation_errors), file=sys.stderr)
        raise SystemExit(1)
    count = len(list(SKILLS_DIR.glob("*.md")))
    print(f"Validated {count} skills and README references.")
