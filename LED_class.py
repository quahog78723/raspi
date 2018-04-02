# LEDclass provides a simple way to interface with individual LEDs
# Simple class for creating LED instances. The LEDs associated with these 
# instances can be set_on or set_off.

# Planned enhancements: 
# 		- Add PWM capabilities and appropriate methods

import RPi.GPIO as GPIO			# Use RPi.GPIO module and reference as GPIO

class LED:                              # Define LED class	
	def __init__(self,pin):         # Instance constructor, takes a PIN ID as a parameter
                                        # Assumes calling program has set GPIO mode (BOARD or BCM)
		self.port = pin                  # Store pin ID as hidden attribute
		GPIO.setup(self.port,GPIO.OUT)   # Set pin as output
		GPIO.output(self.port, False)    # Default...LED is off (PIN is low)

	def set_on(self):                       # set_on method - Sets pin high (Turns on LED)
		GPIO.output(self.port,True)

	def set_off(self):                      # set_off method - Sets pin low (Turns off LED)
		GPIO.output(self.port, False)

	def set(self,on_off):		# Pass boolean vaue to indicate whether to turn on (True) or off (False)
		GPIO.output(self.port,on_off)

	def get_port(self):
                return (self.port)
# End of LED class
