# Simple test script for the initial testing of the LED class and turning an LED on or off

import RPi.GPIO as GPIO
import LED_class

GPIO.setmode(GPIO.BCM)

led = LED_class.LED(5)

input()   # Wait for user to hit the enter key

led.set_on()

input()   # Wait for user to hit the enter key
led.set_off()

GPIO.cleanup()
