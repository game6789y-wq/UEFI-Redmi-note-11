# Research sources

These sources are starting points for research, not proof that a particular boot image or firmware is compatible with this phone. Re-check revisions and exact model applicability before using any hardware data.

## Device identity and Android platform references

- [Xiaomi Redmi Note 11 user guide](https://alsgp0.fds.api.xiaomi.com/xiaomi-b2c-i18n-upload/user-guides/416e669a3e5ed6aa2e28b749b478288f.pdf) — Xiaomi documentation identifies model 2201117TG.
- [Xiaomi SDM680 development device tree for spes](https://github.com/xiaomi-sdm680-development/android_device_xiaomi_spes) — community Android device configuration; useful for identifying the software platform and related repositories.
- [LineageOS / crDroid device tree for spes](https://github.com/crdroidandroid/android_device_xiaomi_spes) — another community device-tree reference. Compare branches and commits rather than assuming all variants share identical details.
- [Qualcomm Snapdragon 680 4G product brief](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/product_brief_-_snapdragon_680_4g_mobile_platform.pdf) — official SoC-level feature summary; it does not document Xiaomi board wiring or the phone's boot chain.

## What these sources do not establish

They do not establish the exact bootloader entry contract, DRAM map, interrupt-controller configuration, secure-boot policy, display initialization sequence, UFS controller setup, or a safe method to launch a third-party UEFI image on model 2201117TG. Those details require device-specific evidence and testing.

## Evidence log policy

When adding a hardware fact, record the source URL, exact branch/commit or document revision, date checked, and whether it was verified on a physical 2201117TG. Label unverified assumptions explicitly.