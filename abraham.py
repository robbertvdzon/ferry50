import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
middle = 75
reach = 35
delay = 1.0
longdelay = 4.0
numberOfTypeMovements = 6
while(True):
    for x in range(numberOfTypeMovements):
        kit.servo[0].angle = middle - reach
        kit.servo[15].angle = middle - reach
        time.sleep(delay)
        kit.servo[0].angle = middle + reach
        kit.servo[15].angle = middle + reach
        time.sleep(delay)
    time.sleep(longdelay)
