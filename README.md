# Integrator-Environment-Checker 🛠️

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Open Source](https://img.shields.io/badge/Open%20Source-Heart-red)
![Hardware](https://img.shields.io/badge/Hardware-ESP32%20%7C%20Arduino%20%7C%20Sensors-orange)

## 📋 Overview
In complex hardware integration environments (Robotics, Electro-Optics, Embedded Systems), ensuring system readiness is the foundation of successful development. 

**Integrator-Environment-Checker** is a professional pre-flight diagnostic tool. It automates the verification of COM ports, optical sensors (cameras), network stability, and system telemetry (CPU/RAM/Battery), ensuring your workstation is "Ready for Mission" in seconds.

---

## ✨ Key Features
- **Modular Probe Architecture:** Easily extendable system to add new hardware checks.
- **Smart Serial Detection:** Scans and identifies active communication ports (CP210x, FTDI, Arduino, etc.).
- **Optical Sensor Validation:** Handshakes with camera sensors using OpenCV (DirectShow support for Windows stability).
- **System Telemetry:** Real-time monitoring of CPU load, RAM availability, and Battery/Power status.
- **Network Health:** TCP-level connectivity check to ensure cloud-sync and API availability.
- **JSON Configuration:** Highly flexible setup via `config.json` without touching the core logic.

---

## 🛠 Project Structure
The project follows a modular design to support open-source contributions:

Integrator-Environment-Checker
├── src/
│   ├── hardware_probes.py   # Serial & Camera logic           
│   ├── main.py              # Application Entry Point
│   ├── network_probes.py    # Connectivity & DNS checks
│   └── system_probes.py     # CPU, RAM & Battery telemetry
│
├── .gitignore    
├── config.json              # User-defined thresholds & IDs        
├── CONTRIBUTING.md          # Guidelines for contributors
├── LICENSE                  # MIT License
├── README.md                # This documentation
└── requirements.txt         # Dependency manifest