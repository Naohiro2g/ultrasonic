#!/usr/bin/env python

# GPIO output (17pin) = "Trig" on the sensor
# GPIO input (27pin) = "Echo" on the sensor

TRIG = 17
ECHO = 27

def read_usonic(sensor):
    import time
    import RPi.GPIO as GPIO

    # Disable any warning message such as GPIO pins in use

    GPIO.setwarnings(False)

    # to refer to the pins by the "Broadcom SOC channel" number

    GPIO.setmode(GPIO.BCM)

    if sensor == 0:

        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG, GPIO.LOW)

        # found that the sensor can crash if there isn't a delay here
        # no idea why. If you have odd crashing issues, increase delay

        time.sleep(0.8)

        # sensor manual says a pulse enough of 10us will trigger the
        # sensor to transmit 8 cycles of ultrasonic burst at 40kHz and
        # wait for the reflected ultrasonic burst to be received

        # start the pulse
        # wait 10 micro seconds (this is 0.00001 seconds)
        # stop the pulse after the time above has passed

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
          signaloff = time.time()
        while GPIO.input(ECHO) == 1:      # echo detected
          signalon = time.time()
        timepassed = signalon - signaloff

        distance = timepassed * 34000 / 2     # 340 m/s
        return distance

    else:
        print "Incorrect read_usonic() function variable."


try:
    while True:
        print "\t distance to obstacle = ", round(read_usonic(0),1), "[cm]"
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
