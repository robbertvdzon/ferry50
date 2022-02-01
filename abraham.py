import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
while(True):
        kit.servo[0].angle = 40
        kit.servo[15].angle = 40
        time.sleep(1)
        kit.servo[0].angle = 0
        kit.servo[15].angle = 0
        time.sleep(1)
