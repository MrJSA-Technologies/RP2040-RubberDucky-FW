# RP2040-RubberDucky-FW

You can find the Payloads for the RubberDucky in the [official Hak5 Repository](https://github.com/hak5/usbrubberducky-payloads) aswell as on the [official Hak5 Payload Hub](https://hak5.org/blogs/payloads/tagged/usb-rubber-ducky)

## Installation

1. Download the latest Adafruit Citcuit Python from the [Adafruit Repository](https://circuitpython.org/board/raspberry_pi_pico/)
2. Plug the RubberDucky into the Computer with the switch set to BOOTSEL. It will show up as a removable media device.
3. After it shows up set the switch to SETUP.
4. Copy the adafruit-circuitpython-raspberry_pi_pico-de_[Language]-[Version].uf2 for you Language, to the root of the RubberDucky.
5. The RubberDucky will reboot and connect as CIRCUITPY.
6. Download the latest adafruit-circuitpython-bundle-8.x-mpy-[Date].zip from the [Adafruit Repository](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases)
7. In the lib Folder copy the adafruit_hid, asyncio and adafruit_wsgi folders aswell as the adafruit_debouncer.mpy and adafruit_ticks.mpy files into the lib folder on the RubberDucky.
8. 
