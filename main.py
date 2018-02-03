from keypad.KeypadPassChecker import Keypad_pass_checker
from door.Door import Door
import time

checker = Keypad_pass_checker()
door = Door()
access = checker.auth()
while true:
    access = checker.auth()
    if access:
        break
#if access:
door.open_door()
door.close_door()
