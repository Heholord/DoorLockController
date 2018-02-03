import RPi.GPIO as GPIO
import time


class Door:
    def __init__(self):
        self.port_led_no = 38
        self.port_door = 36
        self.port_led_yes = 40

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

    def openn(self, door_port, light_port_yes, light_port_no):
        toogle(light_port_no, False)
        toogle(door_port, True)
        toogle(light_port_yes, True)

    def closee(self, door_port, light_port_yes, light_port_no):
        toogle(light_port_no, True)
        toogle(door_port, False)
        toogle(light_port_yes, False)

    def toogle(self, port, on):
        GPIO.setup(port, GPIO.OUT)
        # LEDs
        print "LED on"
        if on:
            GPIO.output(port, GPIO.HIGH)
        else:
            GPIO.output(port, GPIO.LOW)

    def openn(self):
        openn(self.port_door, self.port_led_yes, self.port_led_no)

    def closee(self):
        closee(self.port_door, self.port_led_yes, self.port_led_no)


def test():
    open()
    time.sleep(3)
    close()
