#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO

def addLog(text):
    logfile = open('/home/pi/ferry50/log.txt', 'a')
    logfile.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+': '+text)
    logfile.close()


GPIO.setmode(GPIO.BCM)
INPUT_PIN = 12
addLog('Start read_button.py')

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
        addLog('button pressed')

    sleep(0.2);