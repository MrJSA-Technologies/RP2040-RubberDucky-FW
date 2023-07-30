# RP2040-RubberDucky-FW

You can find the Payloads for the RubberDucky in the [official Hak5 Repository](https://github.com/hak5/usbrubberducky-payloads) aswell as on the [official Hak5 Payload Hub](https://hak5.org/blogs/payloads/tagged/usb-rubber-ducky)

## Installation

### The fast way

1. Download the latest release.
2. Set the switch to `BOOTSEL`
3. When it shows up set the switch to `PAYLOAD`
4. Copy the `*.uf2` file in the `RubberDucky` folder to the root of your RubberDucky
5. After it reboots copy the rest of the files in the RubberDucky folder to the root of your RubberDucky
6. Put your payload to the root of your RubberDucky and rename it to `payload.dd`
7. Set the switch to `Stealth` and you are ready to go.
8. To change the payload set the switch to `PAYLOAD` again and connect it to your device.

### The difficult way

1. Download the latest Adafruit Citcuit Python from the [Circuit Python Website](https://circuitpython.org/board/raspberry_pi_pico/)
2. Plug the RubberDucky into the Computer with the switch set to `BOOTSEL`. It will show up as a removable media device.
3. After it shows up set the switch to `PAYLOAD`.
4. Copy the `adafruit-circuitpython-raspberry_pi_pico-en_US-[Version].uf2` to the root of the RubberDucky.
5. The RubberDucky will reboot and connect as `CIRCUITPY`.
6. Download the latest `adafruit-circuitpython-bundle-8.x-mpy-[Date].zip` from the [Adafruit Repository](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases)
7. In the lib Folder copy the `adafruit_hid`, `asyncio` and `adafruit_wsgi` folders aswell as the `adafruit_debouncer.mpy` and `adafruit_ticks.mpy` files into the `lib` folder on the RubberDucky.
8. Download the latest `circuitpython-keyboard-layouts-8.x-mpy-[Date]` from [Neradoc](https://github.com/Neradoc/Circuitpython_Keyboard_Layouts/releases)
9. Copy all files of the `lib` Folder into the `lib` folder of the RubberDucky.
10. Copy the files `boot.py`, `code.py` and `duckyinpython.py` of the latest release to the root of your RubberDucky.
11. Download or create your own payload, copy it to the root of your RubberDucky and rename it to `payload.dd`.
12. Unplug your RubberDucky and set the switch to `STEALTH` and you are ready to go.
13. To change the payload set the switch to `PAYLOAD` again and connect it to your device.
