import RPi.GPIO as GPIO
import time


class Door:
    def __init__(self):
        self.port_led_red = 38
        self.port_door = 40
        self.port_led_yes = 36

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

    def open(self, door_port, light_port_yea, light_port_no):
        toogle(light_port_no, False)
        toogle(door_port, True)
        toogle(light_port_yes, True)

    def close(self, door_port, light_port):
        toogle(light_port_no, True)
        toogle(door_port, False)
        toogle(light_port, False)

    def toogle(self, port, on):
        GPIO.setup(port, GPIO.OUT)
        # LEDs
        print "LED on"
        if on:
            GPIO.output(port, GPIO.HIGH)
        else:
            GPIO.output(port, GPIO.LOW)

    def open(self):
        open(self.port_door, self.port_led_yes, self.port_led_no)

    def close(self):
        close(self.port_door, self.port_led_yes, self.port_led_no)


def test():
    open()
    time.sleep(3)
    close()
