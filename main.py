from keypad.KeypadPassChecker import Keypad_pass_checker
from door.Door import Door
import time

checker = Keypad_pass_checker()
door = Door()
while True:
    if checker.auth():
        break
#if access:
door.open_door()
door.close_door()