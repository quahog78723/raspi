# MY_GPIO_class defines myGPIO class and provides 
# initialization logic and clean up logic.
#
# Written by Bart Jacob
#
# Planned enhancements:
# Provide initialization parameters (such as BOARD vs BCM etc)

import RPi.GPIO as GPIO

class myGPIO:
    IN  = GPIO.IN
    OUT = GPIO.OUT
    
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        print("GPIO mode set to BCM")

        GPIO.setwarnings(False)
        print("GPIO warnings disabled")

   
    def cleanup(self):
        print("Exiting ...resetting GPIO.")
        GPIO.cleanup()

    def setwarnings(x):
        GPIO.setwarnings(x)

    def setup(pin,dir):
        GPIO.setup(pin,dir)

    def remove_event_detect(pin):
        GPIO.remove_event_detect(pin)

    def add_event_detect(pin,edge): # Add more variables
        GPIO.remove_event_detect(pin)

    def output(pin,val):
        GPIO.output(pin,val)

    def PWM(pin,val):
        return GPIO.PWM(pin,val)

    def input(pin):
        return GPIO.input(pin)
    
    
        
