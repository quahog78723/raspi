# resetGPIO.py
# Bart Jacob
#
# Resets pins 5,6,13,26) to output and performs a GPIO.cleanuo()

import RPi.GPIO as GPIO
import LED_class as LED
import time

GPIO.setmode(GPIO.BCM)

for pin in [5,6,13,26]:
    print("Init pin", pin)
    led = LED.LED(pin)
    # The following lines are not really needed...the LED is
    # initialized to off by the constructor method. But this
    # provides feedback (on screen and through the LEDs that
    # they are being tuned on and then off.

    print("Set pin on / off")
    led.set_on()
    time.sleep(.1)  # Otherwise, the LED is turned off too quickly to see.
    led.set_off()

GPIO.cleanup()
