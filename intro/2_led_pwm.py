import time
import RPi.GPIO as GPIO

# Set our pin to output mode
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

# Set the PWM frequency in Hz (cycles per second)
p = GPIO.PWM(12, 60)  # channel=12 frequency=60Hz

# Start doing PWM
p.start(0)

try:
    # Loop forever
    while True:
        # Increase the duty cycle (percentage of time the pin is on) from
        # 1% to 100%.  This will cause the LED to get brighter
        for dc in range(0, 101, 1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)

        # Now decrease the duty cycle (time the pin is on) back to 1.  This will
        # cause the LED to dim
        for dc in range(100, -1, -1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)
except KeyboardInterrupt:
    # Cleanup and put the pins into a good state
    p.stop()
    GPIO.cleanup()
