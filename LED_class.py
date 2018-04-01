# LEDclass provides a simple way to interface with individual LEDs

import RPi.GPIO as GPIO

class LED:
    def __init__(self,pin):
        self.__pin__ = pin
        GPIO.setup(self.__pin__,GPIO.OUT)
        GPIO.output(self.__pin__, False)

    def set_on(self):
        GPIO.output(self.__pin__,True)

    def set_off(self):
        GPIO.output(self.__pin__, False)

        
