# Blink an LED on pin 18.
# Connect a low-ohm (like 360 ohm) resistor in series with the LED.

import RPi.GPIO as GPIO
import time

# A variable so we can change the PIN number for this script in once place
# if we move the LED to a different pin.
PIN = 18

# Set the pin to do output
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)


# Loop forever blinking our led
while True:
    # Switch the pin off for half of a second
    GPIO.output(PIN, 0)
    time.sleep(.5)

    # Now turn it back on
    GPIO.output(PIN, 1)
    time.sleep(.5)

GPIO.cleanup()