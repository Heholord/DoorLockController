from keypad.KeypadPassChecker import Keypad_pass_checker

checker = Keypad_pass_checker()
door = Door()
if checker.auth():
    door.open()
    sleep()
    door.close()
