# Platform research notes — Redmi Note 11 4G (spes)

Last reviewed: 2026-11-20

## Scope

This note records public source-code leads for the owner-confirmed Redmi Note 11 4G, model `2201117TG`, with 6 GB RAM, 128 GB storage, HyperOS `OS1.0.8.0.TGCMIXM`, and Android 13.

This is source discovery for a research bring-up. It is **not** a verified hardware specification, boot-chain description, memory map, or bootable firmware implementation.

## Public source-code leads

| Area | Candidate source | What it can help investigate | What remains unverified |
|---|---|---|---|
| Android device tree | https://github.com/xiaomi-sdm680-development/android_device_xiaomi_spes | Android product/device configuration for `spes` | Whether its current branch matches this exact HyperOS build and hardware revision |
| Alternative device tree | https://github.com/Jabiyeff/android_device_xiaomi_spes | Device configuration and references to related vendor/kernel trees | Exact branch/build compatibility |
| Kernel source lead | https://github.com/Jabiyeff/kernel_xiaomi_sm6225 | Candidate SM6225 kernel source referenced by the device-tree project | Exact commit, config, vendor modifications, and match to `OS1.0.8.0.TGCMIXM` |
| EDK II background | https://github.com/tianocore/edk2 | Generic UEFI implementation and build-system reference | No Redmi Note 11 / SM6225 platform support is established by the generic project |

The public device-tree listings identify Redmi Note 11 as `spes/spesn` and list Snapdragon 680 / SM6225 variants with 4 GB or 6 GB RAM and 64 GB or 128 GB storage. This is useful corroboration for the reported configuration, but does not prove the exact DRAM layout or boot handoff for this handset.

## What can be concluded now

- The device profile is sufficiently specific to focus further source review on the `spes` family and SM6225.
- Android device-tree repositories are useful for identifying software configuration and possible kernel-source dependencies.
- Android device trees and Linux kernel sources are **not** substitutes for a UEFI platform package. They do not, by themselves, establish the required early boot initialization for EDK II.
- The generic EDK II project is a framework/reference, not evidence that a ready-made build can boot on this phone.

## Required investigation before any device-specific UEFI image

1. Pin the exact matching kernel and device-tree commits; record branch names and commit hashes.
2. Review publicly available board configuration and device-tree sources for documented hardware facts. Separate documented values from guesses.
3. Establish the actual boot-chain entry point and the interface passed to a later-stage payload. Do not infer this from Android's ability to boot.
4. Establish the memory map and reserved regions from reliable device-specific evidence.
5. Identify required timer, interrupt-controller, serial/console, storage, and cache initialization.
6. Decide whether the intended UEFI environment will use Device Tree or ACPI, based on verified platform support.
7. Define a non-destructive test and recovery plan before any device test.

## Current implementation status

- Documentation and source-discovery scaffold: **present**.
- Device-specific EDK II DSC/FDF/platform initialization: **not implemented**.
- Verified boot-chain handoff: **not established**.
- Verified DRAM map / interrupt / timer / console: **not established**.
- UEFI image: **not built**.
- Real-device boot test: **not performed**.

No flashable artifacts should be produced or described as usable until the missing platform facts and a safe test path are independently verified.
