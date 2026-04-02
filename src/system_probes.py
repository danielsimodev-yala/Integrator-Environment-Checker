import psutil

def get_system_telemetry():
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()
    
    batt_percent = battery.percent if battery else "N/A"
    is_plugged = battery.power_plugged if battery else True
    
    return cpu, ram, batt_percent, is_plugged