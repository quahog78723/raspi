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
