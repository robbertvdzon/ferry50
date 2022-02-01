import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
middle = 75
reach = 35
delay = 1.0
while(True):
        kit.servo[0].angle = middle - reach
        kit.servo[15].angle = middle + reach
        time.sleep(delay)
        kit.servo[0].angle = middle + reach
        kit.servo[15].angle = middle - reach
        time.sleep(delay)
