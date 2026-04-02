import serial.tools.list_ports
import cv2
import socket
import sys

def check_serial_ports():
    ports = list(serial.tools.list_ports.comports())
    found_devices = []
    for port in ports:
        found_devices.append(f"{port.device} - {port.description}")
    return found_devices

def check_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return False
    ret, frame = cap.read()
    cap.release()
    return ret

def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def run_diagnostics():
    print("\n--- Starting Hardware Environment Check ---")
    
    devices = check_serial_ports()
    if devices:
        print("[OK] Serial Devices Found:")
        for dev in devices:
            print(f"     - {dev}")
    else:
        print("[!] No Serial Devices Detected")

    if check_camera():
        print("[OK] Camera System: Operational")
    else:
        print("[X] Camera System: Not Detected/Access Denied")

    if check_internet():
        print("[OK] Network: Connected")
    else:
        print("[X] Network: No Internet Connection")

    print("\n" + "="*40)
    if devices and check_camera() and check_internet():
        print("SYSTEM STATUS: READY")
    else:
        print("SYSTEM STATUS: MAINTENANCE REQUIRED")
    print("="*40 + "\n")

if __name__ == "__main__":
    run_diagnostics()