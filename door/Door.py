import RPi.GPIO as GPIO
import time


class Door:
    def __init__(self):
        self.port_led = 20
        self.port_door = 21
        self.door = 16

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def open(self, door_port, light_port):
        toogle(door_port, True)
        toogle(light_port, True)

    def close(self, door_port, light_port):
        toogle(door_port, False)
        toogle(light_port, False)

    def toogle(self, port, on):
        GPIO.setup(port, GPIO.OUT)
        # LEDs
        print "LED on"
        if on GPIO.output(port, GPIO.HIGH)
        else GPIO.output(port, GPIO.LOW)

    def open(self):
        open(port_door, port_led)

    def close(self):
        close(port_door, port_led)


def test():
    open()
    time.sleep(3)
    close()
