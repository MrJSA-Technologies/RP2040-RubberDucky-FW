from board import *
import board
import digitalio
import storage

#  Switch set to Stealth = GND to GP15 = RubberDucky not showing as mass storage

noStorage = False
noStoragePin = digitalio.DigitalInOut(GP15)
noStoragePin.switch_to_input(pull=digitalio.Pull.UP)
noStorageStatus = noStoragePin.value
noStorage = not noStorageStatus

#  If Switch set to stealth don't show USB drive to host PC
if(noStorage == True):
    storage.disable_usb_drive()
    print("Disabling USB drive")
#  Else normal boot and show to host PC
else:
    print("USB drive enabled")
