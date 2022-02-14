#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
INPUT_PIN = 21
INPUT_PIN2 = 20

GPIO.setup(INPUT_PIN, GPIO.IN)
GPIO.setup(INPUT_PIN2, GPIO.IN)

RELAIS = 16
RELAIS2 = 26 # naar led
GPIO.setup(RELAIS, GPIO.OUT)
GPIO.setup(RELAIS2, GPIO.OUT)


while True:

    pin1 = GPIO.input(INPUT_PIN) == True
    pin2 = GPIO.input(INPUT_PIN2) == True

    if (pin1):
        GPIO.output(RELAIS, 0)
    else:
        GPIO.output(RELAIS, 1)

    if (pin2):
        GPIO.output(RELAIS2, 0)
    else:
        GPIO.output(RELAIS2, 1)

    print('pin1: ', pin1)
    print('pin2: ', pin2)

    sleep(1);