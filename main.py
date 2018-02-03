from keypad.KeypadPassChecker import Keypad_pass_checker
from door import Door

checker = Keypad_pass_checker()
door = Door()
if checker.auth():
    door.open()
    sleep()
    door.close()
