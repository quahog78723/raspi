# Simple test script for the initial testing of the LED class and turning an LED on or off
# Bart Jacob
#
# This program assumes 4 LEDs are wired on the (BCM) pins defined below:

pin1 = 5        # BCM pin number
pin2 = 6
pin3 = 13
pin4 = 26

import RPi.GPIO as GPIO
import LED_class            # My class 

GPIO.setmode(GPIO.BCM)      # Utilize BCM numbering
GPIO.setwarnings(True)      # See warnings of PINS are already in use
# Create LED objects for each LED

led1 = LED_class.LED(pin1)
led2 = LED_class.LED(pin2)
led3 = LED_class.LED(pin3)
led4 = LED_class.LED(pin4)

try:
    print("Hit the enter key to turn on each LED in turn.")
    # Turn on each of the four LEDs in turn
    input()         # Wait for user to hit the enter key
    led1.set_on()
    print("LED 1 (pin",led1.get_pin(),") - on",sep=' ',end="")
    input()         # Wait for user to hit the enter key
    led2.set_on()
    print("LED 2 (pin",led2.get_pin(),") - on",sep=' ',end="")
    input()         # Wait for user to hit the enter key
    led3.set_on()
    print("LED 3 (pin",led3.get_pin(),") - on",sep=' ',end="")
    input()         # Wait for user to hit the enter key    
    led4.set_on()
    print("LED 4 (pin",led4.get_pin(),") - on",sep=' ',end="")
    # Turn off each of the four LEDs in turn
    input()         # Wait for user to hit the enter key
    led1.set_off()
    print("LED 1 (pin",led1.get_pin(),") - off",sep=' ',end="")
    input()         # Wait for user to hit the enter key
    led2.set_off()
    print("LED 2 (pin",led2.get_pin(),") - off",sep=' ',end="")
    input()         # Wait for user to hit the enter key
    led3.set_off()
    print("LED 3 (pin",led3.get_pin(),") - off",sep=' ',end="")
    input()         # Wait for user to hit the enter key
    led4.set_off()
    print("LED 4 (pin",led4.get_pin(),") - off",sep=' ',end="")

except KeyboardInterrupt:           # When Ctl-C ...break out of program
    print("\n\nProgram ending.")
                  
finally:
    print("\n\nCleaning up GPIO and exiting.")      
    GPIO.cleanup()                  # Reset GPIO
