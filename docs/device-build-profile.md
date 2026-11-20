# Confirmed device software profile

## Owner-confirmed information

| Field | Value | Evidence |
|---|---|---|
| Device | Xiaomi Redmi Note 11 4G | Owner-provided model |
| Model number | `2201117TG` | Owner-provided |
| HyperOS build shown in Settings | `OS1.0.8.0.TGCMIXM` | Owner-provided verbatim |
| Android version | Android 13 | Owner-provided |
| Firmware region suffix | `MIXM` (Global branch identifier) | Parsed from supplied build string; verify against the matching stock package before using firmware files |
| UEFI target | UEFI Shell research / bring-up | Project requirement |

## What this confirms

The project can track the exact HyperOS build string and Android version reported by the device. These are useful matching keys when locating corresponding stock firmware, kernel sources, and device-tree sources.

## What it does not confirm

These details alone do **not** establish:
- the complete Android build fingerprint or security patch level;
- the exact bootloader version/state or boot-chain handoff;
- partition layout, image headers, or boot image format;
- DRAM map, timer, interrupt controller, or console configuration;
- that a generic EDK2 build can boot on this phone.

Do not treat a firmware package as matching until its device codename, region, build identifier, and checksum are verified. Do not flash experimental images based only on this profile.

## Next evidence to collect

1. Full Android build fingerprint and security patch level from Settings > About phone / Android version (menu wording may vary).
2. RAM and storage capacity.
3. Matching official stock firmware package metadata and checksum (do not upload proprietary firmware blobs or private data to this repository).
4. Read-only boot/partition metadata and matching kernel/device-tree source revision.
5. Documented bootloader handoff and a non-destructive recovery/test plan.

The repository remains a documentation and research scaffold. No device-specific EDK2 platform, bootable UEFI image, or tested firmware is claimed by this file.
