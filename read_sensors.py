#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
INPUT_PIN = 12
INPUT_PIN2 = 20

while True:

    pin1 = GPIO.input(INPUT_PIN) == False
    pin2 = GPIO.input(INPUT_PIN2) == True

    if (pin1 or pin2):
        with open('/tmp/lampen', 'w') as f:
            f.write('')
        with open('/tmp/armen', 'w') as f:
            f.write('')
        with open('/tmp/zwaailicht', 'w') as f:
            f.write('')

    sleep(0.2);