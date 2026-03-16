#!/usr/bin/env python3
"""Function-style runner + live-update mode for generate_graphs.py.

This script does not modify your existing generate_graphs.py.
It parses diagram blocks from that file and executes only what you request.
"""

from __future__ import annotations

import argparse
import os
import re
import time
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

# Diagram headings in generate_graphs.py are like: "# ── 2.1  Market Equilibrium ..."
DIAGRAM_HEADER_RE = re.compile(r"^# ──\s+\d")
SAVE_CALL_RE = re.compile(r"save\(\s*['\"]([^'\"]+)['\"]\s*\)")


@dataclass
class DiagramBlock:
    name: str
    title: str
    code: str
    start_line: int


def _clean_title(header_line: str) -> str:
    t = header_line.strip()
    if t.startswith("#"):
        t = t[1:].strip()
    t = t.strip("─").strip()
    return t


def parse_source(source_path: Path) -> tuple[str, list[DiagramBlock]]:
    if not source_path.exists():
        raise FileNotFoundError(f"Source file not found: {source_path}")

    text = source_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    section_starts = [i for i, line in enumerate(lines) if DIAGRAM_HEADER_RE.match(line)]
    if not section_starts:
        raise RuntimeError("Could not find diagram sections in source file.")

    prelude = "".join(lines[: section_starts[0]])
    blocks: list[DiagramBlock] = []

    all_starts = section_starts + [len(lines)]
    for start, end in zip(all_starts, all_starts[1:]):
        block_code = "".join(lines[start:end])
        save_match = SAVE_CALL_RE.search(block_code)
        if not save_match:
            continue

        name = save_match.group(1)
        title = _clean_title(lines[start])
        blocks.append(
            DiagramBlock(
                name=name,
                title=title,
                code=block_code,
                start_line=start + 1,
            )
        )

    if not blocks:
        raise RuntimeError("Found headers, but no save(...) calls for diagrams.")

    return prelude, blocks


def build_registry(
    prelude: str,
    blocks: list[DiagramBlock],
    out_dir: str | None = None,
) -> tuple[dict, dict[str, Callable[[], None]], list[str]]:
    env: dict = {"__name__": "__graph_runtime__"}
    exec(prelude, env, env)

    if out_dir is not None:
        env["OUT_DIR"] = out_dir
        os.makedirs(out_dir, exist_ok=True)

    registry: dict[str, Callable[[], None]] = {}
    ordered_names: list[str] = []

    for block in blocks:
        ordered_names.append(block.name)
        code = block.code

        def _make_runner(src: str) -> Callable[[], None]:
            def _run() -> None:
                exec(src, env, env)

            return _run

        registry[block.name] = _make_runner(code)

    return env, registry, ordered_names


def run_once(source_path: Path, selected: list[str] | None, out_dir: str | None) -> None:
    prelude, blocks = parse_source(source_path)
    _, registry, ordered_names = build_registry(prelude, blocks, out_dir=out_dir)

    selected_names = selected or ordered_names

    missing = [name for name in selected_names if name not in registry]
    if missing:
        available_preview = ", ".join(ordered_names[:10])
        raise KeyError(
            "Unknown diagram(s): "
            + ", ".join(missing)
            + f"\nUse --list. First available: {available_preview}"
        )

    for name in selected_names:
        print(f"[run] {name}")
        registry[name]()


def list_diagrams(source_path: Path) -> None:
    _, blocks = parse_source(source_path)
    for block in blocks:
        print(f"{block.name}\t{block.title} (line {block.start_line})")


def watch_mode(source_path: Path, selected: list[str], out_dir: str | None, interval: float) -> None:
    if len(selected) != 1:
        raise ValueError("Watch mode requires exactly one diagram. Use: --watch --only <name>")

    target = selected[0]
    print(f"[watch] Source: {source_path}")
    print(f"[watch] Diagram: {target}")
    print(f"[watch] Poll interval: {interval:.2f}s")
    print("[watch] Press Ctrl+C to stop.\n")

    last_mtime = -1.0

    while True:
        try:
            mtime = source_path.stat().st_mtime
            first_run = last_mtime < 0
            changed = mtime != last_mtime

            if first_run or changed:
                last_mtime = mtime
                print("=" * 70)
                print(f"[watch] Detected change at {time.strftime('%H:%M:%S')}")
                run_once(source_path, [target], out_dir)
                print("[watch] Render complete. Waiting for next change...")

            time.sleep(interval)

        except KeyboardInterrupt:
            print("\n[watch] Stopped.")
            return
        except Exception:
            print("\n[watch] Render failed:")
            traceback.print_exc()
            print("\n[watch] Waiting for another file change...")
            time.sleep(interval)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run selected diagrams from generate_graphs.py with optional live watch mode."
    )
    parser.add_argument(
        "--source",
        default="generate_graphs.py",
        help="Path to source diagrams file (default: generate_graphs.py)",
    )
    parser.add_argument(
        "--only",
        nargs="+",
        help="One or more diagram names to run (e.g. 2_1_market_equilibrium)",
    )
    parser.add_argument("--list", action="store_true", help="List available diagram names")
    parser.add_argument(
        "--watch",
        action="store_true",
        help="Watch source file and re-render selected diagram on save",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=0.8,
        help="Watch polling interval in seconds (default: 0.8)",
    )
    parser.add_argument(
        "--out-dir",
        default=None,
        help="Override output directory (otherwise uses OUT_DIR from source file)",
    )

    args = parser.parse_args()
    source_path = Path(args.source).resolve()

    if args.list:
        list_diagrams(source_path)
        return

    if args.watch:
        if not args.only:
            raise ValueError("Watch mode needs --only <diagram_name>")
        watch_mode(source_path, args.only, args.out_dir, args.interval)
        return

    run_once(source_path, args.only, args.out_dir)


if __name__ == "__main__":
    main()
