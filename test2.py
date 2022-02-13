#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
INPUT_PIN = 12
INPUT_PIN2 = 20
LED_1 = 13 # naar relais
LED_2 = 19 #ok
RELAIS = 16
RELAIS2 = 26 # naar led
GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(INPUT_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)
GPIO.setup(RELAIS, GPIO.OUT)
GPIO.setup(RELAIS2, GPIO.OUT)

pi_pwm = GPIO.PWM(LED_1,1000)		#create PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle
pi_pwm2 = GPIO.PWM(LED_2,1000)		#create PWM instance with frequency
pi_pwm2.start(0)				#start PWM of required Duty Cycle

while True:

    pin1 = GPIO.input(INPUT_PIN) == True
    pin2 = GPIO.input(INPUT_PIN2) == True

    print('pin1')
    print(pin1)
    print('pin2')
    print(pin2)


    if (pin1 or pin2):
        GPIO.output(RELAIS, 0)
        GPIO.output(RELAIS2, 0)

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
    else:
        GPIO.output(RELAIS, 1)
        GPIO.output(RELAIS2, 1)
        pi_pwm.ChangeDutyCycle(0)
        pi_pwm2.ChangeDutyCycle(0)

    sleep(0.3);