#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
CYCLE_COUNT = 40
LED_1 = 13
LED_2 = 19
GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)

pi_pwm = GPIO.PWM(LED_1,1000)
pi_pwm.start(0)
pi_pwm2 = GPIO.PWM(LED_2,1000)
pi_pwm2.start(0)


while True:
    if (os.path.isfile('/tmp/lampen')):
        os.remove("/tmp/lampen")
        for cycles in range(0,CYCLE_COUNT):
            for duty in range(0,101,5):
                pi_pwm.ChangeDutyCycle(duty)
                pi_pwm2.ChangeDutyCycle(100-duty)
                sleep(0.01)
            sleep(0.5)
            for duty in range(100,-1,-5):
                pi_pwm.ChangeDutyCycle(duty)
                pi_pwm2.ChangeDutyCycle(100-duty)
                sleep(0.01)
            sleep(0.5)

        pi_pwm.ChangeDutyCycle(0)
        pi_pwm2.ChangeDutyCycle(0)

