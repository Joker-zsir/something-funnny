import RPi.GPIO as GPIO
import time

class BodyMonitor(object):
    def __init__(self, channel):
        self.channel = channel
        self.gpio_obj = GPIO
        self.init()

    def init(self):
        self.gpio_obj.setmode(GPIO.BOARD)
        self.gpio_obj.setup(self.channel, GPIO.IN)

    def rasing_callback_register(self, callback):
        if callable(callback):
            self.gpio_obj.add_event_detect(self.channel, GPIO.RISING, callback=callback)

    def falling_callback_register(self, callback):
        if callable(callback):
            self.gpio_obj.add_event_detect(self.channel, GPIO.FALLING, callback=callback)

    def exit():
        self.gpio_obj.cleanup()


def test():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.IN)
    while True:
        print 'The channel 12 ttl is %d'%GPIO.input(12)
        time.sleep(1)

if __name__ == '__main__':
    test()
