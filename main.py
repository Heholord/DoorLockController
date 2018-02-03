from keypad.KeypadPassChecker import Keypad_pass_checker
from door.Door import Door
import time

checker = Keypad_pass_checker()
door = Door()
access = checker.auth()
while not access:
    in = checker.auth()
if access:
    door.open_door()
