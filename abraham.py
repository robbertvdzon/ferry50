import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=8)
while(True):
        kit.servo[0].angle = 40
        time.sleep(0.3)
        kit.servo[0].angle = 0
        time.sleep(0.3)
