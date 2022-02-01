import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
middle = 75
reach = 35
reachShort = 15
lower = 20
delay = 0.3
longdelay = 6.0
numberOfTypeMovements = 16
numberOfTypeLargeMovements = 4
numberOfTypeHitMovements = 3
while(True):
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

    kit.servo[0].angle = middle - reach
    kit.servo[15].angle = middle + reach


    time.sleep(longdelay)
