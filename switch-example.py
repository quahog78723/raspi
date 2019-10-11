# Switch test program - switch-example.py
# Bart Jacob
#
# Program to sense the state of a pushbutton switch

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # Set mode to BCM numbering

BCM_PIN = 4             # PIN number used based on Broadcom numbering
pin = BCM_PIN           # Set pin number to use
print("Using BCM Pin : ",pin)

GPIO.setup(pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)             # Initialize pin for input

try:
    while True:                     # Loop until interrupted (Ctl-C)
        if GPIO.input(pin)==0:      # If switch open
            print("0", end='')      # Print a 0
        else:   
            print("1",end='')       # Print 1
except KeyboardInterrupt:           # When Ctl-C ...break out of program
    print("\n\nProgram ending.")
                  
finally:
    print("Cleaning up GPIO.")      
    GPIO.cleanup()                  # Reset GPIO
