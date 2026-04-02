import json
import os
import hardware_probes as hw
import system_probes as sys
import network_probes as net

def load_config():
    # טעינת הגדרות מקובץ חיצוני
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, '../config.json')
    
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    return {"camera_index": 0, "target_dns": "8.8.8.8"}

def run_diagnostics():
    config = load_config()
    print("\n--- [ Integrator Diagnostic Tool ] ---")
    
    # בדיקות חומרה
    serials = hw.check_serial_ports()
    print(f"[OK] Peripherals: {serials}" if serials else "[!] No Serial Devices")
    
    cam = hw.check_camera(config['camera_index'])
    print(f"[OK] Camera (ID:{config['camera_index']}): Ready" if cam else "[X] Camera: Error/Not Found")
    
    # בדיקת רשת
    online = net.check_internet(config['target_dns'])
    print(f"[OK] Network: Connected" if online else "[X] Network: Offline")
    
    # בדיקת מערכת
    cpu, ram, batt, plugged = sys.get_system_telemetry()
    print(f"[SYS] CPU: {cpu}% | RAM: {ram}% | Battery: {batt}% ({'Charging' if plugged else 'Battery Only'})")
    
    print("\n" + "="*35)
    if cam and serials and online:
        print("FINAL STATUS: SYSTEM OPERATIONAL")
    else:
        print("FINAL STATUS: MAINTENANCE REQUIRED")
    print("="*35 + "\n")

if __name__ == "__main__":
    run_diagnostics()