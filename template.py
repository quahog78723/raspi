# Python template for GPIO programs
# Bart Jacob

# ********
# Import modules to be used
# ********
import RPi.GPIO as GPIO     # Standard GPIO library for Raspberry Pi
#import time                 # Optional library with time fnctions..useful for sleep time

# ********
# Initialize GPIO enviornment - Select only one of the following statements
# ********
GPIO.setmode(GPIO.BCM)      # Set mode to BCM numbering
#GPIO.setmode(GPIO.BOARD)   # Set mode to board numbering

# Option to disable warnings
GPIO.setwarnings(False)     # Set to Tue or False to see warnings about conflicting pin setup etc

# ********
# Setup pins in this section
# ********
# For instance:
# GPIO.setup(pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)  # Initialize pin for input

# ********
# Example try/except/finally structure
# ********
try:
    print("Main try logic")
#    while True:                     # Loop until interrupted (Ctl-C)
#        if GPIO.input(pin)==0:      # If switch open
#            print("0", end='')      # Print a 0
#        else:   
#            print("1",end="")       # Print 1
except KeyboardInterrupt:           # When Ctl-C ...break out of program
    print("\n\nProgram ending.")

# Executed on program exit...cleanup GPIO
                  
finally:
    print("Cleaning up GPIO.")      
    GPIO.cleanup()                  # Reset GPIO

