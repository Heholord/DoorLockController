from keypad.KeypadPassChecker import Keypad_pass_checker
from door.Door import Door
import time

checker = Keypad_pass_checker()
door = Door()
in = checker.auth()
while not in:
    in = checker.auth()
if in:
    door.open_door()
