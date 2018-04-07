import RPi.GPIO as GPIO

class myGPIO:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        print("GPIO mode set to BCM")


    
    def cleanup(self):
        print("Exiting ...resetting GPIO.")
        GPIO.cleanup()
