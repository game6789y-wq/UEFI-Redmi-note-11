#!/usr/bin/env python3
"""Validate the documentation-only UEFI bring-up scaffold."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "docs/hardware.md",
    "docs/bringup-plan.md",
    "docs/safety.md",
    "docs/research-sources.md",
    "docs/next-data-needed.md",
    "platform/README.md",
)

missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
if missing:
    print("Missing required project files:")
    for name in missing:
        print(f" - {name}")
    sys.exit(1)

readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
if "not bootable firmware" not in readme:
    print("README must clearly identify the repository as non-bootable scaffolding.")
    sys.exit(1)

platform_files = [p for p in (ROOT / "platform").rglob("*") if p.is_file()]
if any(p.suffix.lower() in {".fd", ".img", ".efi"} for p in platform_files):
    print("Unexpected firmware artifact found in platform/: require manual review before publishing.")
    sys.exit(1)

print("Scaffold checks passed. This is documentation validation only; it does not build or test UEFI firmware.")
