# Simple script testing whether or not a switch is open or closed. It also counts the number of
# times the switch is toggled and displays that count as a binary number using LEDs.

import RPi.GPIO as GPIO     # Import RPI.GPIO module as GPIO
import LED_class            # Import our LED_class file that includes the LED class

BCM_PORT    = 22    # Input port for switch - port number used based on Broadcom numbering

BCM_LEDS    = [5,6,13,19]   # For LED to be used, list of ports used
NUM_LEDS    = len(BCM_LEDS) # Number of EDs based on number of ports
led_list    = []            # Initialize a list for the LEDs

#-------------
# Function to set LEDs based on value of count
#-------------

def dispCount(ct):
	ct = ct % (2**NUM_LEDS)             # Set count mod max value able to be displayed
	binrep = bin(int(ct))[2:].zfill(NUM_LEDS)  # Str# Simple script testing whether or not a switch is open or closed. It also counts the number of
# times the switch is toggled and displays that count as a binary number using LEDs.

import RPi.GPIO as GPIO     # Import RPI.GPIO module as GPIO
import LED_class            # Import our LED_class file that includes the LED class

BCM_PORT    = 22    # Input port for switch - port number used based on Broadcom numbering

BCM_LEDS    = [5,6,13,19]   # For LED to be used, list of ports used
NUM_LEDS    = len(BCM_LEDS) # Number of EDs based on number of ports
led_list    = []            # Initialize a list for the LEDs

#-------------
# Function to set LEDs based on value of count
#-------------

def dispCount(ct):
	ct = ct % (2**NUM_LEDS)             # Set count mod max value able to be displayed
	binrep = bin(int(ct))[2:].zfill(NUM_LEDS)  # Strips 0b from string and pads with 0s...
                                        # representing the binary value of the counter
	print("\n\n",binrep)            # Print the string in the console

	for i in range(len(binrep)):    # For LED in list
		led_list[i].set(binrep[i] == '1') # Set on/off based on binary digit in count

#-------------
# Beging main program        
#-------------

GPIO.setmode(GPIO.BCM)      # Set mode to BCM numbering
GPIO.setup(BCM_PORT,GPIO.IN)     # Initialize pin for input

for i in range(NUM_LEDS):   # For each port defined above,
	led_list.append(LED_class.LED(BCM_LEDS[i])) # Create an LED object based on the port number

try:
	switch_state = 0                # Track state of switch
	counter = 0                     # Initialize counter
	while True:                     # Loop until interrupted (Ctl-C)
		if GPIO.input(BCM_PORT)==0:      # If switch open
			switch_state = 0        # Set switch state
			print("0", end='')      # Print a 0
		else:   
			if switch_state == 0:   # If switch was open, and is now closed.
				switch_state = 1    # Change switch state
				counter += 1        # Increment counter
				dispCount(counter)
			print("1",end="")       # Print 1
            
except KeyboardInterrupt:           # When Ctl-C ...break out of program
	print("\n\nProgram ending.")
	print("Switch pressed",counter,"times.")    # Print switch counter
                  
finally:
	print("Cleaning up GPIO.")      
	GPIO.cleanup()                  # Reset GPIO
# End of program
