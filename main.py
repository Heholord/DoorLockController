from keypad import KeypadPassChecker

checker = Keypad_pass_checker()
door = Door()
if checker.auth():
    door.open()
    sleep()
    door.close()
