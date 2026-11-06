Custom Arduino & Python Game Controller
Overview
An interactive hardware-to-software project that bridges physical computing with Python programming. This project utilizes an Arduino microcontroller to read physical inputs (such as buttons, joysticks, or sensors) and transmits the data in real-time via Serial communication (PySerial) to a Python backend, which translates the inputs into game controls or application commands.

Key Features
Hardware-Software Integration: Seamless real-time communication between an Arduino board and a Python script over a serial port (UART).

Custom Input Mapping: Python script processes incoming raw sensor or button states and maps them to keyboard/mouse events or game actions.

Modular Design: Easily expandable to support additional analog joysticks, digital push buttons, or motion sensors (like the MPU6050).

Lightweight & Efficient: Utilizes clean Python logic for event handling and data parsing without heavy driver dependencies.

Technologies Used
Microcontroller: Arduino (Uno / Nano / Mega)

Programming Languages:

C/C++ (Arduino Firmware for reading GPIO pins and analog sensors)

Python (Data parsing, serial communication, and input emulation)

Libraries/Modules: pyserial, pyautogui or pynput (for keyboard/mouse simulation)

How It Works
Input Generation: The user interacts with physical controls wired to the Arduino (e.g., pressing a button or moving a joystick).

Serial Transmission: The Arduino reads the pin states and sends formatted data packets (e.g., JSON strings or comma-separated values) over the USB serial connection.

Python Processing: A Python script continuously listens to the serial port, reads the incoming data stream, parses the values using conditional logic and loops, and triggers corresponding virtual keypresses or mouse movements.
