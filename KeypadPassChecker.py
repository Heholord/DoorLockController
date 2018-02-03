import keypad
import myfile


class Keypad_pass_checker:
    def auth(self):
        inputt = Input()
        checker = Checker()

        inputt.read()
        if checker.compare(inputt):
            print("access granted")
        else:
            print("sorry no")


class Input:
    def __init__(self):
        self.keypad = keypad.Keypad()

    def read(self):
        self.trial = ""
        char = self.keypad.read()
        while(char != "#"):
            self.trial += keypad.read()
            print(self.trial)
            char = self.keypad.read()
        return self.trial

    def get_input(self):
        return self.trial


class Checker:
    def __init__(self):
        self.solution = myfile.readfile("test")

    def compare(self, input):
        return self.solution == input.get_input()

checker = Keypad_pass_checker()
checker.auth()
