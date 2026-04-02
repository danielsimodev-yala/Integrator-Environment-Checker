# Contributing to Integrator-Environment-Checker 🚀

First off, thank you for considering contributing to this tool! It's built by integrators, for integrators.

## How Can I Contribute?

### 1. Reporting Bugs
- Use the GitHub "Issues" tab.
- Describe the hardware and OS you are using.
- Attach the terminal output or logs.

### 2. Adding New Probes (Checks)
We want to support more hardware! If you want to add a check for a Lidar, IMU, or GPU:
1. Fork the repo.
2. Create a new file in `src/` or add a function to `hardware_probes.py`.
3. Update `main.py` to include your new check.
4. Open a Pull Request.

## Coding Standards
- Use modular functions.
- Add comments explaining what the hardware check does.
- Keep the `config.json` flexible.

**Let's build a better diagnostic environment together!**