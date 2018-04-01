# Test script for showing how a call back function can be called based on a GPIO pin event
# Also, shows how to block execution until an event occurs.

import RPi.GPIO as GPIO						# Import RPI.GPIO module

INPUT_PIN = 15								# Set a constant to the pin to be used in this test

def gpio_callback(channel):					# Define function (this function name will be passed when setting up call back)
											# On callback, the channel (pin # ) causing the call back will be passed as a param
	print("Call back channel", channel)		# Simple print statement showing the channel/pin

GPIO.setmode(GPIO.BOARD)					# Set mode to use the BOARD numbering scheme 
GPIO.setup(INPUT_PIN,GPIO.IN)				# Set the PIN as an inout pin

# Uncomment the following to test the call back capability
# GPIO.add_event_detect(INPUT_PIN,GPIO.FALLING,callback=gpio_callback)

# The followingwas added as a test for the 'blocking' function of wait_for_edge. This call
# will pause the mainline of the program until th event is detected and then the main line will continue.

cont = True
while cont:
	print("Starting wait")                  
	GPIO.wait_for_edge(INPUT_PIN,GPIO.BOTH)	# Call that blocks execution until an edge (falling or rising) is detected.
	print("Post wait")
       
