import keypad
import myfile


class Keypad_pass_checker:

    def compare(input, pass):
        return pass.compare(input.getInput)

    class Input:
        def __init__(self):
            self.keypad = Keypad()

        def read(self):
            self.trial = ""
            while(self.keypad.read != "#"):
                self.trial += keypad.read()
            return self.trial

        def get_input(self):
            return self.trial

    class Checker:
        def __init__(self):
            self.solution = myfile.readfile("test")

        def compare(self, input):
            return self.solution == input.get_input()


input = Input()
checker = Check()

input.read()
if checker.compare(input):
    print("access granted")
else:
    print("sorry no")
