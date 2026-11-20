# UEFI Shell bring-up plan

## Phase 0 — identify and preserve

- Confirm model `2201117TG`, codename, SoC, region, and exact stock build.
- Obtain matching stock firmware and preserve original boot/vendor_boot/dtbo and other required partitions.
- Document a tested restore path before attempting any boot-chain modification.
- Map the boot chain and determine the supported image format and handoff contract.

**Exit criteria:** evidence-backed hardware profile and recovery plan.

## Phase 1 — EDK2 foundation

- Pin an EDK2 revision and toolchain versions.
- Create a real platform package, DSC/FDF, target architecture configuration, and reproducible build scripts only after the entry point and memory map are understood.
- Keep host-side build validation separate from device boot validation.

**Exit criteria:** reproducible build of the platform target; this alone does not prove device bootability.

## Phase 2 — minimal platform bring-up

- Implement the device-specific entry point and memory/CPU/interrupt/timer initialization.
- Establish a reliable debug console.
- Add only the minimum protocols needed to launch the UEFI Shell.
- Validate memory map, exception behavior, and stable shell entry using a non-destructive test method.

**Exit criteria:** repeatable UEFI Shell on the exact target with logs and recovery verified.

## Phase 3 — device interfaces

- Add and validate display, USB, and storage support independently.
- Document limitations and tested peripherals; do not advertise unsupported drivers.

## Phase 4 — release

- Require clean CI builds, artifact hashes, exact supported model/firmware list, test logs, known issues, and a recovery guide.
- Do not publish a flashable release until real-device validation is complete.

## Current status

Only repository documentation exists. No EDK2 platform target or bootable firmware has been implemented.