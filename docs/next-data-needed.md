# Device data needed before implementing the platform

The repository currently has documentation only. Do not create a board DSC/FDF or a phone-targeted image until the following information is collected.

## Owner-provided device details

- [ ] Confirm model shown in Settings / device label: 2201117TG.
- [ ] Android version and MIUI/HyperOS version/build fingerprint.
- [ ] RAM and storage capacity.
- [ ] Confirm whether the device is a standard Redmi Note 11 (`spes`) rather than a related NFC/other regional variant.

## Technical evidence

- [ ] Matching official stock firmware package and checksum.
- [ ] Read-only partition metadata and boot image header details from the matching build.
- [ ] Kernel source/device-tree revision matching the firmware build.
- [ ] Bootloader handoff documentation or reproducible, non-destructive observations.
- [ ] Memory map, timer, interrupt controller, and console/debug details.
- [ ] Confirmed test and recovery plan reviewed before any device-side experiment.

## Platform design decisions

- [ ] Select and pin an EDK2 revision.
- [ ] Identify the supported entry mechanism and required image format.
- [ ] Determine whether the firmware must consume a device tree or provide ACPI tables.
- [ ] Define a minimal serial/console path for first-stage debugging.
- [ ] Define success criteria for entering UEFI Shell without writing to persistent partitions.

Do not request or commit private keys, account credentials, device identifiers that are not needed, or proprietary firmware blobs. Do not publish a flashable artifact until device-specific validation is complete.