#!/usr/bin/env python3
# pylint: skip-file

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import zipfile
from dataclasses import dataclass
from pathlib import Path


CSV_RE = re.compile(
    r"^(?P<date>\d{4}_\d{2}_\d{2})_"
    r"(?P<time>\d{2}_\d{2}_\d{2})_"
    r"(?P<rest>.+)_"
    r"(?P<tail>Results|\d+)\.csv$"
)


@dataclass(frozen=True)
class Move:
    src: Path
    dest: Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Reorganize SMART500 CSV exports into creep/modulus folders, "
            "group each Results file with its numbered CSVs, and create "
            ".smart500 archives for each result-set folder."
        )
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Root directory containing the raw or partially organized exports.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned moves and archives without modifying files.",
    )
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_csv_files(root: Path) -> list[Path]:
    return sorted(
        path for path in root.rglob("*.csv") if ".git" not in path.parts and path.is_file()
    )


def classify_top_folder(anchor_stem: str) -> str:
    match = re.match(r"^(\d{4}_\d{2}_\d{2})_\d{2}_\d{2}_\d{2}_(.+)$", anchor_stem)
    if not match:
        raise ValueError(f"Cannot classify anchor: {anchor_stem}")

    date, rest = match.groups()
    if rest.startswith("WG_FS_TAF"):
        return f"{date}_WG_FS_TAF"
    if "_300nm_Creep1000s" in rest:
        specimen = rest.split("_300nm_Creep1000s", 1)[0]
        return f"{date}_{specimen}_Creep1000s"
    if "_600nm_elasticModulus" in rest:
        specimen = rest.split("_600nm_elasticModulus", 1)[0]
        return f"{date}_{specimen}_ElasticModulus"
    if "_600nm_ElasticModulus" in rest:
        specimen = rest.split("_600nm_ElasticModulus", 1)[0]
        return f"{date}_{specimen}_ElasticModulus"

    raise ValueError(f"Unsupported measurement pattern: {anchor_stem}")


def plan_moves(root: Path) -> list[Move]:
    by_key: dict[str, list[Path]] = {}
    for path in iter_csv_files(root):
        match = CSV_RE.match(path.name)
        if not match:
            continue
        by_key.setdefault(match.group("rest"), []).append(path)

    moves: list[Move] = []
    for key, files in sorted(by_key.items()):
        anchor_stem: str | None = None
        for path in sorted(files, key=lambda item: item.name):
            match = CSV_RE.match(path.name)
            if match is None:
                continue
            tail = match.group("tail")
            if tail == "Results":
                anchor_stem = path.stem[: -len("_Results")]
            elif anchor_stem is None:
                raise RuntimeError(
                    f"Found numbered CSV before any Results file for key {key}: {path}"
                )

            top_folder = classify_top_folder(anchor_stem)
            dest = root / top_folder / anchor_stem / path.name
            moves.append(Move(src=path, dest=dest))
    return moves


def execute_moves(moves: list[Move], dry_run: bool) -> tuple[int, int]:
    moved = 0
    deleted_dupes = 0

    for move in moves:
        if dry_run:
            continue
        move.dest.parent.mkdir(parents=True, exist_ok=True)

    for move in moves:
        if move.src.resolve() == move.dest.resolve():
            continue
        if dry_run:
            moved += 1
            continue
        if move.dest.exists():
            if sha256(move.src) != sha256(move.dest):
                raise RuntimeError(f"Conflicting duplicate: {move.src} -> {move.dest}")
            move.src.unlink()
            deleted_dupes += 1
            continue
        shutil.move(str(move.src), str(move.dest))
        moved += 1

    return moved, deleted_dupes


def prune_empty_dirs(root: Path, dry_run: bool) -> int:
    removed = 0
    candidates = sorted(
        (path for path in root.rglob("*") if path.is_dir() and ".git" not in path.parts),
        key=lambda item: len(item.parts),
        reverse=True,
    )
    for path in candidates:
        try:
            next(path.iterdir())
        except StopIteration:
            if not dry_run:
                path.rmdir()
            removed += 1
    return removed


def collect_result_dirs(root: Path) -> list[Path]:
    return sorted({path.parent for path in root.rglob("*_Results.csv") if ".git" not in path.parts})


def create_archives(root: Path, dry_run: bool) -> tuple[int, int]:
    created = 0
    skipped = 0
    for run_dir in collect_result_dirs(root):
        archive = run_dir.with_suffix(".smart500")
        if archive.exists():
            skipped += 1
            continue
        if dry_run:
            created += 1
            continue
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as handle:
            for path in sorted(run_dir.rglob("*")):
                if path.is_file():
                    handle.write(path, arcname=path.relative_to(run_dir.parent))
        created += 1
    return created, skipped


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    moves = plan_moves(root)
    moved, deleted_dupes = execute_moves(moves, dry_run=args.dry_run)
    removed = prune_empty_dirs(root, dry_run=args.dry_run)
    archives_created, archives_skipped = create_archives(root, dry_run=args.dry_run)

    print(f"root={root}")
    print(f"dry_run={args.dry_run}")
    print(f"planned_csv_moves={len(moves)}")
    print(f"moved_csv_files={moved}")
    print(f"deleted_duplicate_csv_files={deleted_dupes}")
    print(f"removed_empty_directories={removed}")
    print(f"smart500_created={archives_created}")
    print(f"smart500_skipped_existing={archives_skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
