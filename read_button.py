#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
INPUT_PIN = 12

GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:

    pin1 = GPIO.input(INPUT_PIN) == False

    if (pin1):
        with open('/tmp/lampen', 'w') as f:
            f.write('')
        with open('/tmp/armen', 'w') as f:
            f.write('')
        with open('/tmp/zwaailicht', 'w') as f:
            f.write('')

    sleep(0.2);