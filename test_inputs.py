#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
INPUT_PIN = 12
INPUT_PIN2 = 20

GPIO.setup(INPUT_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:

    pin1 = GPIO.input(INPUT_PIN) == False
    pin2 = GPIO.input(INPUT_PIN2) == True

    print('pin1: ', pin1)
    print('pin2: ', pin2)

    sleep(1);