# EDK II platform requirements — Redmi Note 11 4G (spes)

Reviewed: 2026-11-20

## Purpose

Define the evidence and software components required before creating a device-specific EDK II platform for the owner-reported Xiaomi Redmi Note 11 4G, model `2201117TG` (6 GB RAM, 128 GB storage, HyperOS `OS1.0.8.0.TGCMIXM`, Android 13).

This document is an engineering requirements checklist. It is not a platform implementation and contains no device-specific register addresses, memory addresses, flash layout, or boot instructions.

## EDK II porting model decision

TianoCore describes two broad porting models:

1. **Cold-boot firmware** — EDK II owns execution from the first firmware instruction and must perform early platform initialization, including memory and CPU/platform setup.
2. **Later-stage bootloader** — EDK II is entered by an earlier firmware stage that has already initialized enough hardware to provide a documented handoff environment.

For this phone, neither path is verified. A later-stage model is only a possible research direction if a documented, supported handoff into a third-party AArch64 payload is established. Do not assume that an Android boot image, a generic ARM64 EFI binary, or a kernel boot argument is such a handoff.

The cold-boot model is out of scope unless authoritative platform documentation and a safe development/recovery route become available.

Reference: https://www.tianocore.org/tianocore-wiki.github.io/platforms-packages/core-packages/arm_platform_pkg.html

## Required evidence gates

| Gate | Evidence required | Current status |
|---|---|---|
| Exact target | Confirmed model, SoC family, software build | Partially documented from owner-provided details and public Android source leads |
| Entry contract | Documented entry point, execution level/state, registers, arguments, cache/MMU state, exception level, and ownership of initialized hardware | **Missing** |
| RAM map | Verified installed RAM ranges, reserved regions, secure carve-outs, firmware/bootloader allocations, and usable ranges | **Missing** |
| CPU/platform | CPU topology, supported architectural features, coherency assumptions, and secondary-core state | **Missing** |
| Interrupts | Interrupt controller type/version, distributor/redistributor access and initialization state | **Missing** |
| Timer | Available architectural/platform timer, frequency, access permissions, and initialization state | **Missing** |
| Console | Verified UART/controller, clock, pin configuration, access permissions, and safe console method at payload entry | **Missing** |
| Device description | Verified Device Tree handoff or ACPI table strategy, including ownership and lifetime of the data | **Missing** |
| Storage/boot | Documented read-only device discovery and boot-source interface | **Missing** |
| Recovery/test | Non-destructive test route and independently verified recovery plan | **Missing** |

No platform-specific addresses or PCD values should be guessed to make a build succeed.

## EDK II components to evaluate after the gates pass

These are candidate EDK II building blocks, not a declaration that the phone supports them:

- **EDK II core and build tooling:** `edk2`, BaseTools, and the AArch64 toolchain.
- **Architecture packages:** `ArmPkg` and the applicable AArch64 CPU/architecture libraries.
- **Common platform components:** `ArmPlatformPkg` where its interfaces fit the verified handoff model.
- **UEFI drivers and shell:** selected `MdeModulePkg` DXE components and the UEFI Shell package.
- **Platform-specific library instances:** `ArmPlatformLib`, `SerialPortLib`, `TimerLib`, interrupt-controller support, and reset-system support, each selected or implemented only from verified hardware facts.
- **Platform description:** a DSC describing the platform components/library instances and an FDF only when a legitimate image packaging format and delivery mechanism are known.

The official AArch64 FVP/Juno build guide is a useful build-environment reference, but those outputs target the documented virtual platforms or Juno board, not this Xiaomi phone:
https://github.com/tianocore/edk2-platforms/blob/master/Platform/ARM/Readme.md

## Proposed repository layout (planning only)

```text
Platform/Qualcomm/RedmiNote11/
  RedmiNote11.dsc             # create only after verified platform values exist
  RedmiNote11.fdf             # defer until image format and handoff are documented
  Include/
    Platform.h                # verified platform constants only
  Library/
    PlatformLib/               # handoff-specific platform services
    SerialPortLib/             # only after UART is verified
    TimerLib/                  # only after timer is verified
  Drivers/
    README.md                  # document driver evidence and validation
```

This is a proposed directory plan, not committed source code. The repository must not contain placeholder register values or a misleading build target.

## First implementation milestone

The first acceptable milestone is **host-side build-environment validation using an official EDK II reference platform**, not a phone image:

1. Record the exact EDK II and edk2-platforms revisions used for a reproducible host build.
2. Build an official AArch64 FVP target following TianoCore's documented procedure.
3. Preserve logs and generated artifact names as evidence that the toolchain works.
4. Label that output as an FVP artifact only. It is not compatible with or bootable on Redmi Note 11.
5. Keep the phone-specific platform target disabled until the entry contract, RAM map, and safe test route are documented.

## Acceptance criteria before a phone-specific DSC/FDF

- Every platform PCD and hardware address has a cited device-specific source or an independently reviewed measurement.
- The entry contract and memory ownership are documented.
- Timer, interrupt-controller, and console assumptions are independently supported.
- The selected Device Tree/ACPI handoff is defined.
- A non-destructive test method and recovery plan are reviewed.
- A host build and static checks pass; a real-device result is claimed only after a real-device test.

## References

- TianoCore ArmPlatformPkg porting guidance: https://www.tianocore.org/tianocore-wiki.github.io/platforms-packages/core-packages/arm_platform_pkg.html
- TianoCore AArch64 FVP/Juno build guide: https://github.com/tianocore/edk2-platforms/blob/master/Platform/ARM/Readme.md
- TianoCore EDK II build description files: https://www.tianocore.org/tianocore-wiki.github.io/build-tooling/build-workflows/build_description_files.html
- UEFI memory-map concept: https://uefi.org/specs/ACPI/6.6/15_System_Address_Map_Interfaces.html

## Status

No phone-specific DSC/FDF, platform driver, UEFI image, or real-device boot test is produced by this requirements document.
