from pad4pi import rpi_gpio
import time

KEYPAD = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
]

# COL_PINS = [0,5,6,13] # BCM numbering
# ROW_PINS = [19,26,20,21] # BCM numbering

ROW_PINS = [15,13,11,7] # BCM numbering
COL_PINS = [21,18,16,12] # BCM numbering

factory = rpi_gpio.KeypadFactory()

# Try factory.create_4_by_3_keypad
# and factory.create_4_by_4_keypad for reasonable defaults
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

def printKey(key):
        print(key)

# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)

time.sleep(5)
