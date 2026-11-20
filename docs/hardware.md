# Hardware research: Redmi Note 11 4G (2201117TG)

## Initial target identification

| Item | Current identification | Confidence / note |
|---|---|---|
| Commercial model | Xiaomi Redmi Note 11 4G, 2201117TG | Supplied by device owner; confirm in Settings and device label |
| SoC | Qualcomm Snapdragon 680, SM6225 | Commonly associated with the global 4G variant; verify against the actual unit |
| Device codename | `spes` | Commonly used for Redmi Note 11 4G; verify exact firmware/device tree |
| CPU architecture | ARM64 / AArch64 | Expected for this SoC |
| Initial firmware goal | UEFI Shell | Project requirement |

## Required evidence before platform code

1. Exact stock firmware build fingerprint and region.
2. Bootloader state and documented unlock method/status.
3. Partition map and boot image format from the matching stock firmware package.
4. Existing kernel device tree and Qualcomm boot-chain handoff details.
5. Available serial/debug console and a verified recovery procedure.
6. Whether the device's secure boot chain permits the intended test image.

Do not infer compatibility from the marketing name alone. Redmi Note 11 variants can have different SoCs, partition layouts, and firmware. Record evidence and source links for every hardware-specific assumption.

## Bring-up constraints

A phone does not provide a PC-style UEFI environment by default. EDK2 needs a device-specific entry path and platform integration, including memory discovery, interrupt/timer setup, console/display, storage/boot media, and a correct handoff from the existing Qualcomm boot chain. ACPI versus device-tree handoff must be decided from the target boot path, not guessed.

No flashable image is produced by this research scaffold.