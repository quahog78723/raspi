# Simple class for creating LED instances. The LEDs associated with these 
# instances can be set_on or set_off. 
# The constructor method takes a pin number as a parameter, identifying the pin that the 
# LED is associated with.
# There is also a generic set method where
# the parameter can be True or False for turning the LED on or off.
# get_pin method returns the pin associated with the LED.

# Planned enhancements: 
# 		- Add PWM capabilities and appropriate methods

import RPi.GPIO as GPIO			# Use RPi.GPIO module and reference as GPIO

class LED:                              # Define LED class	
	def __init__(self,pin):         # Instance constructor, takes a PIN ID as a parameter
                                        # Assumes calling program has set GPIO mode (BOARD or BCM)
		self.__pin = pin                  # Store pin ID as hidden attribute
		GPIO.setup(self.__pin,GPIO.OUT)   # Set pin as output
		GPIO.output(self.__pin, False)    # Default...LED is off (PIN is low)

	def set_on(self):                       # set_on method - Sets pin high (Turns on LED)
		GPIO.output(self.__pin,True)

	def set_off(self):                      # set_off method - Sets pin low (Turns off LED)
		GPIO.output(self.__pin, False)

	def set(self,on_off):		# Pass boolean vaue to indicate whether to turn on (True) or off (False)
		GPIO.output(self.__pin,on_off)

	def get_pin(self):
                return (self.__pin)
# End of LED class
