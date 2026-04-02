import serial.tools.list_ports
import cv2

def check_serial_ports():
    ports = list(serial.tools.list_ports.comports())
    return [f"{p.device} - {p.description}" for p in ports]

def check_camera(index):
    # שימוש ב-DirectShow למניעת שגיאות לוג בווינדוס
    cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
    if not cap.isOpened():
        return False
    ret, frame = cap.read()
    cap.release()
    return ret