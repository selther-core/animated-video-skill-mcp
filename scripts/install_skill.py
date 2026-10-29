#!/usr/bin/env python3
"""Plan or install the skill to a caller-selected, existing skills directory.

Default is a read-only plan. --apply copies the skill; never overwrites.
Does not configure MCP, download dependencies, or change agent settings.
"""
from __future__ import annotations
import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_NAME = "cinematic-narrative-video"
SOURCE = ROOT / ".agents" / "skills" / SKILL_NAME


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--skills-dir", required=True, help="Existing host skills directory (consult your host's documentation)")
    p.add_argument("--apply", action="store_true", help="Actually copy the skill; default only prints a plan")
    args = p.parse_args()
    parent = Path(args.skills_dir).expanduser().resolve()
    if not parent.is_dir():
        print(f"Skills directory does not exist: {parent}", file=sys.stderr)
        return 2
    if not (SOURCE / "SKILL.md").is_file():
        print(f"Source skill not found: {SOURCE}", file=sys.stderr)
        return 2
    dest = parent / SKILL_NAME
    if dest.exists() or dest.is_symlink():
        print(f"Destination already exists; refusing to overwrite: {dest}", file=sys.stderr)
        return 2
    if parent == SOURCE or SOURCE in parent.parents:
        print("Destination cannot be inside the source skill", file=sys.stderr)
        return 2
    print(f"Source: {SOURCE}\nDestination: {dest}")
    print("Includes reference stills; check redistribution rights. MCP is not installed by this script.")
    if not args.apply:
        print("PLAN ONLY: rerun with --apply to copy. No files changed.")
        return 0
    try:
        shutil.copytree(SOURCE, dest, symlinks=False)
    except OSError as e:
        print(f"Copy failed: {e}. Check whether a partial destination exists: {dest}", file=sys.stderr)
        return 1
    if not (dest / "SKILL.md").is_file():
        print(f"Installed entry point missing; inspect destination: {dest}", file=sys.stderr)
        return 1
    print("Installed skill files. Reload the agent and verify discovery; see mcp/README.md for optional MCP setup.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
