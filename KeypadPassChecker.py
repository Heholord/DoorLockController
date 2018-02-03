import keypad
import myfile


class Keypad_pass_checker:

    class Input:
        def __init__(self):
            self.keypad = Keypad()

        def read(self):
            self.trial = ""
            while(self.keypad.read != "#"):
                self.trial += keypad.read()
                print(self.trial)
            return self.trial

        def get_input(self):
            return self.trial

    class Checker:
        def __init__(self):
            self.solution = myfile.readfile("test")

        def compare(self, input):
            return self.solution == input.get_input()

    def auth(self):
        inputt = Input()
        checker = Check()

        inputt.read()
        if checker.compare(inputt):
            print("access granted")
        else:
            print("sorry no")

checker = Keypad_pass_checker()
checker.auth()
