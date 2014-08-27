# Blink an LED on pin 18.
# Connect a low-ohm (like 360 ohm) resistor in series with the LED.

import RPi.GPIO as GPIO
import time

# A variable so we can change the PIN number for this script in once place
# if we move the LED to a different pin.
PIN = 7

# Set the pin to do output
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)


# Loop forever turning our power outlet off and on
# WARNING: A relay is a physical device which can wear out if cycled
# many times quickly.  So short sleep times (less than a few seconds)
# in this loop are probably not a good idea.
while True:
    # Switch the pin off for half of a second
    GPIO.output(PIN, 0)
    time.sleep(5)

    # Now turn it back on
    GPIO.output(PIN, 1)
    time.sleep(5)

GPIO.cleanup()