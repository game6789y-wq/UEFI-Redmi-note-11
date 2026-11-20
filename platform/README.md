# EDK2 platform integration

This directory is reserved for the device-specific EDK2 platform package.

No DSC/FDF, PEI/DXE platform modules, entry point, device drivers, or flashable image are present yet. These must not be stubbed with generic PC platform settings and presented as phone support.

Before adding platform code, document the verified Qualcomm boot-chain entry contract, memory map, interrupt controller, timer, console/debug path, and device-tree/ACPI handoff for model 2201117TG. Pin the EDK2 revision and toolchain in the eventual build configuration.