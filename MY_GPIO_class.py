# MY_GPIO_class defines myGPIO class and provides 
# initialization logic and clean up logic.
#
# Written by Bart Jacob
#
# Planned enhancements:
# Provide initialization parameters (such as BOARD vs BCM etc)

import RPi.GPIO as GPIO

class myGPIO:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        print("GPIO mode set to BCM")

        GPIO.setwarnings(False)
        print("GPIO warnings disabled")

   
    def cleanup(self):
        print("Exiting ...resetting GPIO.")
        GPIO.cleanup()
