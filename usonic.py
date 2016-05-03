#!/usr/bin/env python
# -*- coding: utf-8 -*-
# GPIO output (17pin) = "Trig" on the sensor
# GPIO input (27pin) = "Echo" on the sensor

import time
import RPi.GPIO as GPIO

TRIG = 17
ECHO = 27

# Disable any warning message such as GPIO pins in use
GPIO.setwarnings(False)
# to refer to the pins by the "Broadcom SOC channel" number
GPIO.setmode(GPIO.BCM)

def read_usonic(sensor):
    if sensor == 0:
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG, GPIO.LOW)

        time.sleep(0.5)

        # send a 10us pulse to Trigger
        # It might be 180uS or longer in fact.
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)

        while GPIO.input(ECHO) == 0:
          signaloff = time.time()
        while GPIO.input(ECHO) == 1:      # echo detected
          signalon = time.time()
        timepassed = signalon - signaloff

        distance = timepassed * 17000     # 340 m/s / 2 in cm
        return distance

    else:
        print "Incorrect read_usonic() function variable."


try:
    while True:
        print "\t distance = ", round(read_usonic(0),1), "[cm]"
#        time.sleep(0.5)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
