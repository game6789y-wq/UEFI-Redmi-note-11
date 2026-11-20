# Device testing and recovery safety

- This repository is a research scaffold, not a flashable firmware package.
- Do not flash generic ARM64 UEFI images, PC firmware, or images built for another Redmi Note 11 variant.
- Never overwrite bootloader, modem, persist, or other critical partitions as an experiment.
- Preserve the exact stock firmware and verify a recovery method before any device-side test.
- Keep test procedures reversible and use documented, model-matched tools.
- A successful compile does not establish that an image can boot safely on the phone.
- Releases must clearly state the exact tested model, stock firmware fingerprint, test method, known limitations, and recovery instructions.