from keypad.KeypadPassChecker import Keypad_pass_checker
from door.Door import Door

checker = Keypad_pass_checker()
door = Door()
if checker.auth():
    door.open_door()
    sleep()
    door.close_door()
