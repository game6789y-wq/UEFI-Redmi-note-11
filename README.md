# UEFI research for Xiaomi Redmi Note 11 4G (2201117TG)

> **Status: research / bring-up scaffold — not bootable firmware.** Do not flash or use this repository as a recovery image.

This project investigates a device-specific ARM64 UEFI implementation for the Xiaomi Redmi Note 11 4G, model **2201117TG** (Qualcomm Snapdragon 680 / SM6225; device family commonly identified as `spes`). The initial target is an interactive **UEFI Shell**.

## Confirmed device profile

| Field | Reported value |
|---|---|
| Model | Xiaomi Redmi Note 11 4G |
| Model number | `2201117TG` |
| RAM | 6 GB |
| Internal storage | 128 GB |
| HyperOS build | `OS1.0.8.0.TGCMIXM` |
| Android version | Android 13 |
| UEFI target | UEFI Shell research / bring-up |

These software and capacity details are owner-provided. They do not establish the boot-chain handoff, physical memory map, partition layout, or UEFI hardware initialization requirements.

## Goals

- Identify the exact boot chain, firmware interfaces, and hardware revision for model 2201117TG.
- Establish a reproducible EDK II-based ARM64 development environment.
- Bring up only hardware interfaces that can be safely and independently validated.
- Reach a UEFI Shell with documented console, memory map, and boot-device behavior.
- Publish a release only after device-specific validation and a tested recovery path.

## Research notes

- [Device build profile](docs/device-build-profile.md) — owner-confirmed model, software build, RAM, and storage.
- [Platform research](docs/platform-research.md) — public source-code leads and remaining platform blockers.
- [Android device-tree review](docs/android-device-tree-review.md) — reviewed Android `BoardConfig.mk` and board compatibility metadata, with UEFI-specific caveats.
- [Hardware notes](docs/hardware.md) — device facts and open questions.
- [Bring-up plan](docs/bringup-plan.md) — staged development and validation plan.
- [Safety policy](docs/safety.md) — non-destructive testing and recovery requirements.

## Current implementation status

- Research/documentation scaffold: **present**.
- Public Android device-tree configuration review: **documented**.
- Device-specific EDK II DSC/FDF and platform initialization: **not implemented**.
- Verified Qualcomm/Xiaomi boot-chain handoff: **not established**.
- Verified DRAM map and reserved-memory layout: **not established**.
- Verified UEFI timer, interrupt controller, and console: **not established**.
- UEFI image: **not built**.
- Real-device UEFI boot test: **not performed**.

Android device-tree settings are not a UEFI board specification. In particular, Android kernel console arguments and Android image partition-size variables must not be treated as validated UEFI UART settings or as the handset's live GPT map.

A generic ARM64 EDK2 build is **not** equivalent to firmware for this phone. Do not claim Windows/Linux boot support or working touchscreen, display, USB, storage, or battery drivers until each is implemented and tested.

## Getting involved

Start with the research notes, then follow the staged bring-up plan. Keep all findings labeled as owner-reported, source-observed, or independently verified. Do not create or test a device image until the boot handoff, memory map, and a non-destructive recovery path are established.
