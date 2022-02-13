#!/usr/bin/env python

from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
INPUT_PIN2 = 20

GPIO.setup(INPUT_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:

    pin2 = GPIO.input(INPUT_PIN2) == True

    if (pin2):
        print('aan ', datetime.now().time())

        with open('/tmp/lampen', 'w') as f:
            f.write('')
        with open('/tmp/armen', 'w') as f:
            f.write('')
        with open('/tmp/zwaailicht', 'w') as f:
            f.write('')

#          wait until move sensor is off
        while GPIO.input(INPUT_PIN2) == True:
            sleep(0.2);
        print('uit ', datetime.now().time())

    sleep(0.2);