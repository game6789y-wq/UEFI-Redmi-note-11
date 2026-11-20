# ARM64 FVP reference build

This workflow validates that the upstream EDK2 toolchain can build an ARM64 reference platform in GitHub Actions. It is a development-environment milestone only.

## Run it

1. Open the repository's **Actions** tab.
2. Select **EDK2 ARM64 FVP reference build**.
3. Select **Run workflow** on the default branch.
4. Wait for the `build-fvp-reference` job to finish.
5. If the job succeeds, download the artifact named `fvp-reference-not-phone-firmware`.

The workflow is manual (`workflow_dispatch`) so normal documentation changes do not trigger a long toolchain build. It records the exact upstream EDK2 and edk2-platforms commit IDs in the job log. The upstream repositories are fetched at their current default-branch heads, so repeat runs may use different revisions.

## Expected output

The upstream Arm FVP Base platform build target is:

```text
Platform/ARM/VExpressPkg/ArmVExpress-FVP-AArch64.dsc
```

Expected firmware-volume file:

```text
Build/ArmVExpress-FVP-AArch64/DEBUG_GCC5/FV/FVP_AARCH64_EFI.fd
```

The artifact is an **Arm FVP reference-platform image**. It is not designed for, compatible with, or flashable on the Xiaomi Redmi Note 11 4G.

## What a successful run proves

- The hosted Linux runner can install the required build dependencies.
- The fetched upstream EDK2 and edk2-platforms sources can be prepared.
- The upstream AArch64 FVP reference DSC can be built with the selected toolchain.
- The expected FVP output file exists and is non-empty.

It does **not** prove anything about the Redmi Note 11 boot chain, Qualcomm handoff, DRAM map, UART, timer, interrupt controller, storage, display, or device-specific UEFI support.

## Local build outline

Follow the official upstream instructions rather than treating this repository as a device firmware tree:

- [TianoCore edk2-platforms ARM build guide](https://github.com/tianocore/edk2-platforms/blob/master/Platform/ARM/Readme.md)
- [TianoCore ArmPlatformPkg AArch64 guide](https://www.tianocore.org/tianocore-wiki.github.io/platforms-packages/core-packages/armplatformpkg_aarch64.html)

The reference build command is:

```bash
build -a AARCH64 -t GCC5 \
  -p Platform/ARM/VExpressPkg/ArmVExpress-FVP-AArch64.dsc \
  -b DEBUG
```

## Status

The workflow has been added but has not yet been run in GitHub Actions. Do not report a successful build until the workflow has completed and the artifact is present.
