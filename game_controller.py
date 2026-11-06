import serial
import keyboard
import time

PORT = "COM8"   # change this to your ESP32's COM port

KEY_MAP = {
    "UP": "up",
    "DOWN": "down",
    "LEFT": "left",
    "RIGHT": "right",
    "NONE": None
}

def main():
    ser = serial.Serial(PORT, 115200, timeout=1)
    print("Connected! Start tilting your sensor.")
    current_key = None

    while True:
        line = ser.readline().decode(errors="ignore").strip()

        if line in KEY_MAP:
            new_key = KEY_MAP[line]
            if current_key and current_key != new_key:
                keyboard.release(current_key)   # let go of the old key
            if new_key:
                keyboard.press(new_key)         # hold the new key
            current_key = new_key
        else:
            if current_key:
                keyboard.release(current_key)
                current_key = None

        time.sleep(0.05)

main()