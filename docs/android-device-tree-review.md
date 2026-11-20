# Android device-tree review — Redmi Note 11 (spes/spesn)

Reviewed: 2026-11-20

## Source examined

Public Android device-tree repository:
- Repository: https://github.com/sayann70/device_xiaomi_spes
- Branch returned by GitHub Contents API: `17`
- Files reviewed: `BoardConfig.mk`, `board-info.txt`, and `README.md`

This is an Android ROM build configuration. It is useful evidence about how an Android build targets the device, but it is not a UEFI firmware specification.

## Findings from the reviewed files

| Item | Value in source | Interpretation / limitation |
|---|---|---|
| Device identifiers | `spes` / `spesn` | Android board compatibility names; check exact handset variant before assuming every `spesn` configuration applies |
| SoC family | `sm6225` in kernel source/header paths | Supports focusing research on Qualcomm SM6225 |
| Target architecture | `arm64` | Android kernel/userspace target architecture; not a complete UEFI platform definition |
| Boot header version | `3` | Android boot-image build setting, not proof of the bootloader's complete accepted image formats |
| Android bootloader build flag | `TARGET_NO_BOOTLOADER := true` | Means this Android build configuration does not build a bootloader component; it does **not** mean the physical device has no bootloader |
| Android board label | `bengal` | Android build target label; not enough to identify a UEFI board implementation |
| Kernel console arguments | `console=ttyMSM0,115200n8` and `earlycon=msm_geni_serial,0x4a90000` | Kernel boot console configuration; not proof that UEFI can use this UART or that the address is valid in UEFI's execution stage |
| Android partition build values | boot, dtbo, vendor_boot, super, and dynamic-partition size variables | Android image-build metadata only; do not treat these values as a verified live GPT/physical partition map |
| Kernel source path in config | `kernel/xiaomi/sm6225` | Android build-tree path, not a pinned source revision |

The accompanying `board-info.txt` contains the compatibility requirement `board=spes|spesn`. The README describes the device as Redmi Note 11, Snapdragon 680 / SM6225, with 4/6 GB RAM and 64/128 GB UFS 2.2 configurations. The owner's 6 GB / 128 GB configuration is consistent with one listed SKU, but this does not identify the DRAM chip, memory topology, or address map.

## Implications for the UEFI project

1. Use `arm64` and SM6225 as source-review filters, not as sufficient platform configuration.
2. Keep the Android boot-header setting separate from UEFI image-format decisions.
3. Do not copy Android kernel console arguments into UEFI code without hardware-level confirmation of UART controller state, clocking, pin mux, access permissions, and address mapping at the UEFI entry point.
4. Do not copy Android partition-size variables into a UEFI storage driver or partition map. Verify the actual device partition table from authoritative, read-only device evidence first.
5. The Android build's `TARGET_NO_BOOTLOADER` setting says nothing conclusive about the handset's proprietary Qualcomm/Xiaomi boot chain or a supported third-party payload handoff.

## Current conclusion

The reviewed Android configuration gives useful identifiers and kernel-build context, but it does not provide the verified early-boot contract required to start EDK II on the phone. In particular, there is still no confirmed UEFI entry point, DRAM map, reserved-memory layout, interrupt/timer setup, or usable UEFI console.

## Next safe research tasks

- Pin the exact kernel repository URL, branch, and commit that corresponds to the installed HyperOS build.
- Compare the Android device-tree branch and kernel revision against the exact installed build before treating either as matching.
- Search source documentation for SoC-level UART, GIC, timer, and memory-controller facts, and label any facts not specific to this board as provisional.
- Draft an EDK II platform requirements checklist only after the boot handoff and memory map have authoritative evidence.

No firmware image was built or tested as part of this review.
