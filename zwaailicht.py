#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
RELAIS = 16
RELAIS2 = 26 # naar led
GPIO.setup(RELAIS, GPIO.OUT)
GPIO.setup(RELAIS2, GPIO.OUT)

GPIO.output(RELAIS, 0)
GPIO.output(RELAIS2, 0)
sleep(1)

while True:
    if (os.path.isfile('/tmp/zwaailicht')):
        os.remove("/tmp/zwaailicht")
        GPIO.output(RELAIS, 0)
        GPIO.output(RELAIS2, 0)
        sleep(3)
    GPIO.output(RELAIS, 1)
    GPIO.output(RELAIS2, 1)
    sleep(0.2)
