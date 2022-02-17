#!/usr/bin/env python

from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

def addLog(text):
    logfile = open('/home/pi/log.txt', 'a')
    logfile.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+': '+text+"\n")
    logfile.close()

GPIO.setmode(GPIO.BCM)
INPUT_PIN2 = 20

GPIO.setup(INPUT_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

addLog('Start read_sensors.py')
lastStatus = False

pin2 = GPIO.input(INPUT_PIN2) == True
print("Initial state is ", pin2)

while True:

    pin2 = GPIO.input(INPUT_PIN2) == True
    if (pin2 != lastStatus):
        print("change state to ", pin2)

    if (pin2):
        if (not lastStatus):
            addLog('movement detected')
            with open('/tmp/lampen', 'w') as f:
                f.write('')
            with open('/tmp/armen', 'w') as f:
                f.write('')
            with open('/tmp/zwaailicht', 'w') as f:
                f.write('')

        #          wait until move sensor is off
        #         while GPIO.input(INPUT_PIN2) == True:
        #             sleep(0.2);
        #         print('uit ', datetime.now().time())
        # sleep(90); # sleep 60 sec
    else:
        if (lastStatus):
            addLog('movement stopped')


    lastStatus = pin2

    sleep(0.2);


