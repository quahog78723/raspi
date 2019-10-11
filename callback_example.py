# Test script for showing how a call back function can be called based on a GPIO pin event
# Also, shows how to block execution until an event occurs.

import RPi.GPIO as GPIO					# Import RPI.GPIO module

INPUT_PIN = 15						# Set a constant to the pin to be used in this test

#
# Define function gpio_callback
#
def gpio_callback(channel):				# Define function (this function name will be passed when setting up call back)
							# On callback, the channel (pin # ) causing the call back will be passed as a param
	print("\nIn gpio_callback function", channel)		# Simple print statement showing the channel/pin
	
#
# Main line of program
#

GPIO.setmode(GPIO.BOARD)			# Set mode to use the BOARD numbering scheme
GPIO.setup(INPUT_PIN,GPIO.IN)			# Set the PIN as an inout pin

print("Test program to demonstrate callbacks and waits")

quit = False
waiting_for_callback = True

while not quit:
	opt = input("Enter option to demonstrate callback (c) or block (b). Quit (q) exits program : ")
	if opt == 'c':
		GPIO.add_event_detect(INPUT_PIN,GPIO.FALLING,callback=gpio_callback,bouncetime=200) # Add detection that will call gpio_callback when the pin is in falling state
		print("Main line will print '.' 500 times waiting for call back")
		for i in range(500):
			print('.',end = '')
		print("\nMain line complete")
		GPIO.remove_event_detect(INPUT_PIN)
	elif opt == 'b':             
		print("Program is paused waiting for button push")
		GPIO.wait_for_edge(INPUT_PIN,GPIO.BOTH)	# Call that blocks execution until an edge (falling or rising) is detected.
		GPIO.remove_event_detect(INPUT_PIN)
		print("Button has been pushed so program can contiue.")
	elif opt == 'q':
		quit = True

	else:
		print("Invalid input, try again.")





