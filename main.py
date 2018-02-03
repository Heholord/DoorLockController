from keypad.KeypadPassChecker import Keypad_pass_checker
from door.Door import Door
import time

checker = Keypad_pass_checker()
door = Door()
if checker.auth():
    for i in [0, 100]:
        door.open_door()
        time.sleep(0.2)
        door.close_door()
