#!/usr/bin/env python3
"""Validate the portable skill kit manifest, skills, and repository references."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"
INSTALL = ROOT / "INSTALL.md"
MANIFEST = ROOT / "skill-kit.json"
NAME_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
VERSION_CORE = r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)"
VERSION_PATTERN = re.compile(VERSION_CORE)
README_VERSION_PATTERN = re.compile(
    rf"^\| \*\*Release\*\* \| (?P<version>{VERSION_CORE}) · .+ \|$",
    re.MULTILINE,
)
FRONTMATTER_PATTERN = re.compile(r"\A---\n(?P<fields>.*?)\n---(?:\n|\Z)", re.DOTALL)
SKILL_REFERENCE_PATTERN = re.compile(r"`/([a-z0-9]+(?:-[a-z0-9]+)*)`")
README_LINK_PATTERN = re.compile(r"\]\((skills/[a-z0-9-]+\.md)\)")
MANIFEST_FIELDS = {"schemaVersion", "id", "name", "version", "entryPoints", "skills"}
MANIFEST_SKILL_FIELDS = {"command", "path"}


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
        key = key.strip()
        if key in fields:
            raise ValueError(f"{path}: duplicate frontmatter field {key!r}")
        fields[key] = value.strip()
    return fields


def reject_duplicate_json_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def is_safe_skill_path(value: object) -> bool:
    if not isinstance(value, str) or not value or "\\" in value:
        return False
    path = PurePosixPath(value)
    return bool(
        not path.is_absolute()
        and path.as_posix() == value
        and len(path.parts) == 2
        and path.parts[0] == "skills"
        and path.suffix == ".md"
        and NAME_PATTERN.fullmatch(path.stem)
    )


def validate() -> list[str]:
    errors: list[str] = []
    if SKILLS_DIR.is_symlink():
        return [f"{SKILLS_DIR}: skills directory must not be a symlink"]
    skill_paths = sorted(SKILLS_DIR.glob("*.md"))
    if not skill_paths:
        return [f"{SKILLS_DIR}: no skill files found"]

    names: set[str] = set()
    contents: dict[str, str] = {}
    names_by_path: dict[str, str] = {}
    actual_paths = {path.relative_to(ROOT).as_posix() for path in skill_paths}

    for path in skill_paths:
        relative_path = path.relative_to(ROOT).as_posix()
        if path.is_symlink():
            errors.append(f"{relative_path}: skill files must not be symlinks")
            continue
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
        names_by_path[relative_path] = name

        if not description or len(description) > 1024:
            errors.append(f"{path}: description must contain 1-1024 characters")
        if "[TODO:" in content or "FIXME" in content:
            errors.append(f"{path}: unfinished placeholder found")

    manifest_commands: set[str] = set()
    manifest_paths: set[str] = set()
    manifest_version = ""

    if not MANIFEST.exists():
        errors.append(f"{MANIFEST}: missing")
    elif MANIFEST.is_symlink():
        errors.append(f"{MANIFEST}: manifest must not be a symlink")
    else:
        try:
            manifest = json.loads(
                MANIFEST.read_text(encoding="utf-8"),
                object_pairs_hook=reject_duplicate_json_keys,
            )
        except (json.JSONDecodeError, ValueError) as error:
            errors.append(f"{MANIFEST}: invalid JSON: {error}")
            manifest = None

        if manifest is not None and not isinstance(manifest, dict):
            errors.append(f"{MANIFEST}: root must be a JSON object")
            manifest = None

        if manifest is not None:
            missing_fields = MANIFEST_FIELDS - set(manifest)
            unexpected_fields = set(manifest) - MANIFEST_FIELDS
            if missing_fields:
                errors.append(f"{MANIFEST}: missing fields: {', '.join(sorted(missing_fields))}")
            if unexpected_fields:
                errors.append(f"{MANIFEST}: unsupported fields: {', '.join(sorted(unexpected_fields))}")

            if type(manifest.get("schemaVersion")) is not int or manifest.get("schemaVersion") != 1:
                errors.append(f"{MANIFEST}: schemaVersion must be the integer 1")

            kit_id = manifest.get("id")
            if not isinstance(kit_id, str) or not NAME_PATTERN.fullmatch(kit_id) or len(kit_id) > 64:
                errors.append(f"{MANIFEST}: id must be a lowercase hyphenated name of at most 64 characters")

            kit_name = manifest.get("name")
            if not isinstance(kit_name, str) or not kit_name.strip() or len(kit_name) > 100:
                errors.append(f"{MANIFEST}: name must contain 1-100 characters")

            version = manifest.get("version")
            if not isinstance(version, str) or not VERSION_PATTERN.fullmatch(version):
                errors.append(f"{MANIFEST}: version must use Semantic Versioning as major.minor.patch")
            else:
                manifest_version = version

            skill_entries = manifest.get("skills")
            if not isinstance(skill_entries, list) or not skill_entries:
                errors.append(f"{MANIFEST}: skills must be a non-empty array")
            else:
                for index, entry in enumerate(skill_entries):
                    label = f"{MANIFEST}: skills[{index}]"
                    if not isinstance(entry, dict):
                        errors.append(f"{label} must be an object")
                        continue

                    missing_entry_fields = MANIFEST_SKILL_FIELDS - set(entry)
                    unexpected_entry_fields = set(entry) - MANIFEST_SKILL_FIELDS
                    if missing_entry_fields:
                        errors.append(f"{label} missing fields: {', '.join(sorted(missing_entry_fields))}")
                    if unexpected_entry_fields:
                        errors.append(f"{label} unsupported fields: {', '.join(sorted(unexpected_entry_fields))}")

                    command = entry.get("command")
                    path_value = entry.get("path")

                    if not isinstance(command, str) or not NAME_PATTERN.fullmatch(command) or len(command) > 64:
                        errors.append(f"{label} command must be a lowercase hyphenated name of at most 64 characters")
                    elif command in manifest_commands:
                        errors.append(f"{label} duplicates command {command!r}")
                    else:
                        manifest_commands.add(command)

                    if not is_safe_skill_path(path_value):
                        errors.append(f"{label} path must be a canonical skills/<name>.md path")
                        continue
                    if path_value in manifest_paths:
                        errors.append(f"{label} duplicates path {path_value!r}")
                    else:
                        manifest_paths.add(path_value)

                    target = ROOT / path_value
                    if target.is_symlink():
                        errors.append(f"{label} path must not be a symlink")
                    elif not target.is_file():
                        errors.append(f"{label} path does not exist: {path_value}")

                    if isinstance(command, str) and PurePosixPath(path_value).stem != command:
                        errors.append(f"{label} command must match its filename")
                    frontmatter_name = names_by_path.get(path_value)
                    if frontmatter_name and command != frontmatter_name:
                        errors.append(f"{label} command must match frontmatter name {frontmatter_name!r}")

            entry_points = manifest.get("entryPoints")
            if not isinstance(entry_points, list) or not entry_points:
                errors.append(f"{MANIFEST}: entryPoints must be a non-empty array")
            else:
                seen_entry_points: set[str] = set()
                for index, entry_point in enumerate(entry_points):
                    label = f"{MANIFEST}: entryPoints[{index}]"
                    if not isinstance(entry_point, str) or not NAME_PATTERN.fullmatch(entry_point):
                        errors.append(f"{label} must be a lowercase hyphenated command")
                    elif entry_point in seen_entry_points:
                        errors.append(f"{label} duplicates entry point {entry_point!r}")
                    else:
                        seen_entry_points.add(entry_point)
                        if entry_point not in manifest_commands:
                            errors.append(f"{label} is not listed in skills")

    for unlisted_path in sorted(actual_paths - manifest_paths):
        errors.append(f"{MANIFEST}: skill file is not listed: {unlisted_path}")
    for missing_path in sorted(manifest_paths - actual_paths):
        errors.append(f"{MANIFEST}: listed path is not a repository skill: {missing_path}")

    for source_name, content in contents.items():
        for reference in SKILL_REFERENCE_PATTERN.findall(content):
            if reference not in manifest_commands:
                errors.append(f"skills/{source_name}.md: missing referenced skill /{reference}")

    if not README.exists():
        errors.append(f"{README}: missing")
        return errors

    readme = README.read_text(encoding="utf-8")
    if not INSTALL.is_file() or INSTALL.is_symlink():
        errors.append(f"{INSTALL}: missing")
    elif "[INSTALL.md](INSTALL.md)" not in readme:
        errors.append("README.md: missing INSTALL.md link")
    version_match = README_VERSION_PATTERN.search(readme)
    if not version_match:
        errors.append("README.md: missing Semantic Versioning release line")
    else:
        readme_version = version_match.group("version")
        if manifest_version and readme_version != manifest_version:
            errors.append(f"README.md: release {readme_version} does not match manifest version {manifest_version}")
        if f"### {readme_version} ·" not in readme:
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
    assert VERSION_PATTERN.fullmatch("1.0.0")
    assert not VERSION_PATTERN.fullmatch("v1")
    assert not VERSION_PATTERN.fullmatch("01.0.0")
    assert is_safe_skill_path("skills/sample-skill.md")
    assert not is_safe_skill_path("../sample-skill.md")
    assert not is_safe_skill_path("skills/nested/sample-skill.md")
    try:
        json.loads('{"id":"first","id":"second"}', object_pairs_hook=reject_duplicate_json_keys)
    except ValueError:
        pass
    else:
        raise AssertionError("duplicate JSON keys must be rejected")
    assert README_VERSION_PATTERN.search("| **Release** | 1.0.0 · 10 November 2026 |")
    assert not README_VERSION_PATTERN.search("| **Release** | v1 |")


if __name__ == "__main__":
    self_check()
    validation_errors = validate()
    if validation_errors:
        print("\n".join(f"ERROR: {error}" for error in validation_errors), file=sys.stderr)
        raise SystemExit(1)
    count = len(list(SKILLS_DIR.glob("*.md")))
    print(f"Validated {count} skills, manifest, and README references.")
