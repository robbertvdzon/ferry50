import time
from adafruit_servokit import ServoKit
import os

kit = ServoKit(channels=16)
middle = 75
reach = 27 #35
reachShort = 15
reachBottom = 40
lower = 20
delay = 0.3
longdelay = 6.0
numberOfTypeMovements = 8
numberOfTypeLargeMovements = 4
numberOfTypeHitMovements = 3
while(True):

    if (os.path.isfile('/tmp/armen')):
        os.remove("/tmp/armen")
        for x in range(numberOfTypeMovements):
            kit.servo[0].angle = middle - reachShort - lower
            kit.servo[15].angle = middle - reachShort + lower
            time.sleep(delay)
            kit.servo[0].angle = middle + reachShort - lower
            kit.servo[15].angle = middle + reachShort + lower
            time.sleep(delay)

        for x in range(numberOfTypeLargeMovements):
            kit.servo[0].angle = middle - reach
            kit.servo[15].angle = middle - reach
            time.sleep(delay)
            kit.servo[0].angle = middle + reach
            kit.servo[15].angle = middle + reach
            time.sleep(delay)

        for x in range(numberOfTypeHitMovements):
            kit.servo[0].angle = middle - reach
            kit.servo[15].angle = middle + reach
            time.sleep(delay)
            kit.servo[0].angle = middle + reach
            kit.servo[15].angle = middle - reach
            time.sleep(delay)

        kit.servo[0].angle = middle - reachBottom
        kit.servo[15].angle = middle + reachBottom


    time.sleep(0.2)
