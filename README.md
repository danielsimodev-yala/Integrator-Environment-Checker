# Integrator-Environment-Checker 🛠️

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Hardware](https://img.shields.io/badge/Hardware-ESP32%20%7C%20Arduino%20%7C%20Sensors-orange)

## 📋 Overview
In complex hardware integration environments (such as Electro-Optics or Robotics), system readiness is the foundation of successful development. This utility is a pre-flight diagnostic tool designed for hardware integrators and embedded engineers. 

It automates the tedious process of manually checking COM ports, camera feed availability, and network stability, ensuring your workstation is "Ready for Mission" in seconds.

## ✨ Key Features
- **Smart Serial Detection:** Automatically scans and identifies active communication ports (CP210x, FTDI, Arduino, etc.) without port locking.
- **Optical Sensor Validation:** Performs a low-level handshake with primary camera sensors using OpenCV to verify frame buffer availability.
- **Network Health Check:** Validates internet connectivity via TCP handshake to ensure cloud-based APIs or update servers are reachable.
- **Integrator's Report:** Generates a structured terminal summary with a clear "READY" or "MAINTENANCE" status.

---

## 🛠 Project Structure
```text
Integrator-Environment-Checker/
├── main.py              # Core diagnostic logic & hardware probes
├── requirements.txt     # Dependency manifest
├── .gitignore           # Version control exclusions (Python/IDE)
└── README.md            # Professional documentation