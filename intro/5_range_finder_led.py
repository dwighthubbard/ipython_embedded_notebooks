#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import sys


# Set our pin to output mode
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

# Set the PWM frequency in Hz (cycles per second)
p = GPIO.PWM(12, 60)  # channel=12 frequency=60Hz

# Start doing PWM
p.start(0)


class RangeFinder(object):
    model = 'HC_SR04'
    GPIO_TRIGGER = 23
    GPIO_ECHO = 24
    MAX_INCH = 180


    def __init__(self, samples=3):
        # Use BCM instead of physical pin numbering:
        self.samples = samples

        GPIO.setmode(GPIO.BCM)

        # Set trigger and echo pins as output and input
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

        # Initialize trigger to low:
        GPIO.output(self.GPIO_TRIGGER, False)

    @property
    def distance_cm(self):
        """
        Measure a single distance, in cemtimeters.
        """
        GPIO.output(self.GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)
        start = time.time()
        stop = time.time()

        while GPIO.input(self.GPIO_ECHO) == 0:
            start = time.time()

        while GPIO.input(self.GPIO_ECHO) == 1:
            stop = time.time()

        # Convert to inches:
        return ((stop - start) * 34300)/2

    @property
    def distance_inch(self):
        """Measure a single distance, in inches.
        """
        GPIO.output(self.GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)
        start = time.time()
        stop = time.time()

        while GPIO.input(self.GPIO_ECHO) == 0:
            start = time.time()

        while GPIO.input(self.GPIO_ECHO) == 1:
            stop = time.time()

        # Convert to inches:
        return (((stop - start) * 34300)/2)*0.393701

    @property
    def average_distance_feet(self):
        return self.average_distance(unit='feet')

    @property
    def average_distance_inch(self):
        return self.average_distance(unit='inch')

    @property
    def average_distance_cm(self):
        return self.average_distance(unit='cm')

    @property
    def average_distance_percent(self):
        return self.average_distance(unit='percent')

    def average_distance(self, unit='inch'):
        tot = 0.0
        for i in range(self.samples):
            if unit == 'cm':
                tot += self.distance_cm
            elif unit == 'inch':
                tot += self.distance_inch
            elif unit == 'percent':
                percent = self.MAX_INCH * (self.distance_inch/self.MAX_INCH)
                if percent > 100:
                    percent = 100
                tot += percent
            else:
                tot += self.distance_inch/12.0
            time.sleep(0.1)
        return tot / self.samples



if __name__ == '__main__':
    sensor = RangeFinder()

    print('Running main')
    while True:
        percent = sensor.average_distance_percent
        print(100-percent)
        if percent == 100:
            p.ChangeDutyCycle(1)
        elif percent < 100:
            p.ChangeDutyCycle(100-percent)

        time.sleep(.1)