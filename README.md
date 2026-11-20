# UEFI for Xiaomi Redmi Note 11 4G (2201117TG)

> **Status: research / bring-up scaffold — not bootable firmware.** Do not flash or use this repository as a recovery image.

This project investigates a device-specific ARM64 UEFI implementation for the Xiaomi Redmi Note 11 4G, model **2201117TG** (Qualcomm Snapdragon 680 / SM6225, device codename commonly identified as `spes`). The initial target is an interactive **UEFI Shell**.

## Goals

- Identify the exact boot chain, partition layout, firmware interfaces, and hardware revision for 2201117TG.
- Establish a reproducible EDK2-based ARM64 development environment.
- Bring up only hardware interfaces that can be safely and independently validated.
- Reach a UEFI Shell with documented console, memory map, and boot-device behavior.
- Publish a release only after device-specific validation and a tested recovery path.

## Repository layout

```text
.
├── README.md
├── docs/
│   ├── hardware.md       # verified device facts and open questions
│   ├── bringup-plan.md   # staged porting and validation plan
│   └── safety.md        # flashing and recovery policy
└── platform/
    └── README.md        # EDK2 platform integration notes
```

## Current limitations

There is currently no platform DSC/FDF, board initialization, Qualcomm firmware interface implementation, device tree/ACPI handoff, or bootable image in this repository. A generic ARM64 EDK2 build is **not** equivalent to firmware for this phone. The project must not claim Windows/Linux boot support or working touchscreen, display, USB, storage, or battery drivers until each is implemented and tested.

## Getting involved

Start with [hardware research](docs/hardware.md), then follow the [bring-up plan](docs/bringup-plan.md). See [safety policy](docs/safety.md) before any device testing.