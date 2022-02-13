#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LED_1 = 13 # naar relais
LED_2 = 19 #ok
GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)

pi_pwm = GPIO.PWM(LED_1,1000)		#create PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle
pi_pwm2 = GPIO.PWM(LED_2,1000)		#create PWM instance with frequency
pi_pwm2.start(0)				#start PWM of required Duty Cycle


while True:
    if (os.path.isfile('/tmp/lampen')):

        for cycles in range(0,5,1):
            for duty in range(0,101,5):
                pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
                pi_pwm2.ChangeDutyCycle(100-duty) #provide duty cycle in the range 0-100
                sleep(0.01)
            sleep(0.5)
            for duty in range(100,-1,-5):
                pi_pwm.ChangeDutyCycle(duty)
                pi_pwm2.ChangeDutyCycle(100-duty)
                sleep(0.01)
            sleep(0.5)

        pi_pwm.ChangeDutyCycle(0)
        pi_pwm2.ChangeDutyCycle(0)
        os.remove("/tmp/lampen")

