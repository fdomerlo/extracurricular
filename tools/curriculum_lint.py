#!/usr/bin/env python3
"""Validate explicit curriculum structure and traceability metadata."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any
import yaml

ROOT = Path(__file__).resolve().parents[1]
COMPETENCIES = ROOT / "curriculum" / "competencies.md"
MATRIX = ROOT / "curriculum" / "competency-matrix.md"

REQUIRED = {
    "id",
    "título",
    "semestre",
    "stack de referencia",
    "nivel",
    "duración estimada",
    "prerrequisitos",
    "competencias",
    "evidencia",
}
ID_RE = re.compile(r"^S[1-6]-\d{2}$")
EVID_ID_RE = re.compile(r"^E-S[1-6]-\d{2}$")
MILESTONE_RE = re.compile(r"^M-S[1-6]$")
COMP_RE = re.compile(r"^C(?:0[1-9]|[1-7][0-9])$")
LEVELS = {"L1", "L2", "L3", "L4"}
ROLES = {"introducción", "práctica", "consolidación", "demostración"}


def frontmatter(text: str) -> tuple[dict[str, Any], list[str]]:
    lines = text.splitlines()
    start_idx = -1
    for i, line in enumerate(lines):
        if line.strip() == "---":
            start_idx = i
            break
        elif line.strip():
            return {}, ["missing YAML frontmatter"]

    if start_idx == -1:
        return {}, ["missing YAML frontmatter"]

    try:
        end_idx = lines.index("---", start_idx + 1)
    except ValueError:
        return {}, ["unterminated YAML frontmatter"]

    raw_yaml = "\n".join(lines[start_idx + 1 : end_idx])
    try:
        data = yaml.safe_load(raw_yaml)
    except yaml.YAMLError as exc:
        return {}, [f"malformed YAML frontmatter: {exc}"]

    if data is None:
        return {}, ["empty YAML frontmatter"]
    if not isinstance(data, dict):
        return {}, ["frontmatter must be a YAML mapping"]

    return data, []


def parse_roles(value: str) -> dict[str, str]:
    value = value.strip()
    if not (value.startswith("{") and value.endswith("}")):
        return {}
    result = {}
    for item in value[1:-1].split(","):
        if ":" not in item:
            continue
        key, role = item.split(":", 1)
        result[key.strip().strip("'\"")] = role.strip().strip("'\"")
    return result


def competency_ids(text: str) -> set[str]:
    return set(re.findall(r"\bC\d{2}\b", text))


def check_class(
    path: Path, known: set[str], matrix: set[str], root: Path | None = None
) -> tuple[list[str], set[str]]:
    base_root = root if root is not None else ROOT
    try:
        prefix = str(path.resolve().relative_to(base_root.resolve()))
    except ValueError:
        prefix = path.name

    data, errors = frontmatter(path.read_text(encoding="utf-8"))
    if errors:
        return [f"{prefix}: {err}" for err in errors], set()

    for key in REQUIRED - data.keys():
        errors.append(f"{prefix}: missing frontmatter field '{key}'")

    cid = data.get("id")
    if cid is not None:
        if not isinstance(cid, str) or not ID_RE.fullmatch(cid):
            errors.append(f"{prefix}: invalid id '{cid}'")
        elif path.stem != cid:
            errors.append(f"{prefix}: filename and id differ ({path.stem} != {cid})")

    nivel = data.get("nivel")
    if nivel is not None and nivel not in LEVELS:
        errors.append(f"{prefix}: invalid level '{nivel}'")

    semestre = data.get("semestre")
    if semestre is not None and not re.fullmatch(r"^S[1-6]$", str(semestre)):
        errors.append(f"{prefix}: invalid semester '{semestre}'")

    # Validate evidencia
    evidencia = data.get("evidencia")
    if evidencia is not None:
        if isinstance(evidencia, dict):
            ev_id = evidencia.get("id")
            ev_ms = evidencia.get("milestone")
            if not ev_id:
                errors.append(f"{prefix}: evidencia missing 'id'")
            elif not isinstance(ev_id, str) or not EVID_ID_RE.fullmatch(ev_id):
                errors.append(f"{prefix}: invalid evidencia id format '{ev_id}'")
            if not ev_ms:
                errors.append(f"{prefix}: evidencia missing 'milestone'")
            elif not isinstance(ev_ms, str) or not MILESTONE_RE.fullmatch(ev_ms):
                errors.append(f"{prefix}: invalid evidencia milestone format '{ev_ms}'")
        elif isinstance(evidencia, str):
            # transitional flat format
            if not EVID_ID_RE.fullmatch(evidencia):
                errors.append(f"{prefix}: invalid evidencia id format '{evidencia}'")
            ms = data.get("milestone")
            if not ms or not isinstance(ms, str) or not MILESTONE_RE.fullmatch(ms):
                errors.append(f"{prefix}: invalid milestone format '{ms}'")
        else:
            errors.append(f"{prefix}: 'evidencia' must be a mapping with 'id' and 'milestone'")

    # Validate competencias and roles
    raw_comps = data.get("competencias")
    comp_map: dict[str, dict[str, Any]] = {}
    if raw_comps is None:
        pass  # missing field already added to errors
    elif isinstance(raw_comps, dict):
        for k, v in raw_comps.items():
            if isinstance(v, dict):
                comp_map[str(k)] = v
            else:
                errors.append(f"{prefix}: competency '{k}' specification must be a mapping")
    elif isinstance(raw_comps, list):
        # transitional list format
        raw_roles = data.get("roles", {})
        if isinstance(raw_roles, str):
            raw_roles = parse_roles(raw_roles)
        for item in raw_comps:
            c_code = str(item)
            role = raw_roles.get(c_code) if isinstance(raw_roles, dict) else None
            comp_map[c_code] = {"role": role} if role else {}
    else:
        errors.append(f"{prefix}: 'competencias' must be a mapping of competency ID to metadata")

    if raw_comps is not None and not comp_map:
        errors.append(f"{prefix}: no competencies declared")

    for c_code, cinfo in comp_map.items():
        if not COMP_RE.fullmatch(c_code):
            errors.append(f"{prefix}: invalid competency id '{c_code}'")
        elif c_code not in known:
            errors.append(f"{prefix}: unknown competency '{c_code}'")
        elif c_code not in matrix:
            errors.append(f"{prefix}: competency '{c_code}' absent from competency-matrix.md")

        role = cinfo.get("role")
        if not role:
            errors.append(f"{prefix}: missing role for competency '{c_code}'")
        elif role not in ROLES:
            errors.append(f"{prefix}: invalid role for {c_code}: '{role}'")

        if "gate" in cinfo:
            gate = cinfo["gate"]
            if not isinstance(gate, str) or not MILESTONE_RE.fullmatch(gate):
                errors.append(f"{prefix}: invalid gate format for {c_code}: '{gate}'")

    if isinstance(raw_comps, list) and isinstance(data.get("roles"), dict):
        for c_code in data["roles"]:
            if c_code not in comp_map:
                errors.append(f"{prefix}: role declared for non-declared competency {c_code}")

    valid_cids = {c for c in comp_map if COMP_RE.fullmatch(c) and c in known and c in matrix}
    return errors, valid_cids


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint Extracurricular curriculum metadata")
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root")
    parser.add_argument(
        "--semester",
        type=str,
        default="S1",
        help="semester to lint (default: S1, or 'all')",
    )
    parser.add_argument("files", nargs="*", type=Path, help="optional specific files to check")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    competencies = root / "curriculum" / "competencies.md"
    matrix = root / "curriculum" / "competency-matrix.md"
    if not competencies.exists():
        print("ERROR: missing curriculum/competencies.md")
        return 2
    known = competency_ids(competencies.read_text(encoding="utf-8"))
    matrix_ids = competency_ids(matrix.read_text(encoding="utf-8")) if matrix.exists() else set()

    if args.files:
        classes = sorted([f.resolve() for f in args.files])
    elif args.semester.lower() == "all":
        classes = sorted(root.glob("practice/s*/classes/S[1-6]-*.md"))
    else:
        sem = args.semester.lower()
        if not sem.startswith("s"):
            sem = f"s{sem}"
        classes = sorted(root.glob(f"practice/{sem}/classes/S[1-6]-*.md"))

    if not classes:
        print(f"ERROR: no class files found for semester {args.semester}")
        return 2

    errors: list[str] = []
    covered: dict[str, list[str]] = {}
    for path in classes:
        class_errors, ids = check_class(path, known, matrix_ids, root=root)
        errors.extend(class_errors)
        for c_code in ids:
            covered.setdefault(c_code, []).append(path.stem)

    sem_label = args.semester.upper()
    if args.semester.lower() == "all":
        warnings = [
            f"{cid}: no class explicitly references this competency yet"
            for cid in sorted(known)
            if COMP_RE.fullmatch(cid) and cid not in covered
        ]
    else:
        warnings = [
            f"{cid}: no class in {sem_label} explicitly references this competency yet"
            for cid in sorted(known)
            if COMP_RE.fullmatch(cid) and cid not in covered
        ]

    print("Curriculum Lint")
    print("===============")
    print(f"Semester: {sem_label}")
    print(f"Classes: {len(classes)}")
    print(f"Competencies defined: {len(known)}")
    print(f"Competencies covered by classes: {len(covered)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
