from keypad.KeypadPassChecker import Keypad_pass_checker
from door.Door import Door
import time

checker = Keypad_pass_checker()
door = Door()
if checker.auth():
    door.open_door()
    time.sleep(3)
    door.close_door()
