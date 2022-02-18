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

GPIO.setup(INPUT_PIN2, GPIO.IN)

addLog('Start read_sensors.py')
lastStatus = False

pin2 = GPIO.input(INPUT_PIN2) == True
print("Initial state is ", pin2)

while True:

    pin2 = GPIO.input(INPUT_PIN2) == True
    if (pin2 != lastStatus):
        print("change state to ", pin2)

    if (pin2):
        # lampen aan laten zolng er beweging is
        with open('/tmp/lampen', 'w') as f:
            f.write('')

        # armen en zwaailicht alleen als er een nieuw iemand langsloopt
        if (not lastStatus):
            addLog('movement detected')
            with open('/tmp/armen', 'w') as f:
                f.write('')
            with open('/tmp/zwaailicht', 'w') as f:
                f.write('')
    else:
        if (lastStatus):
            addLog('movement stopped')


    lastStatus = pin2

    sleep(0.2);


