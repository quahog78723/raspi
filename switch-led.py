# Switch test 

# Simple sxcript testing whether or not a switch is open or closed.

import RPi.GPIO as GPIO     # Import RPI.GPIO module as GPIO
import LED_class            # Import our LED_class file that includes the LED class

BCM_PIN = 22    # Input pin for switch - PIN number used based on Broadcom numbering

BCM_LED8 = 5    # Output GPIO for LED8
BCM_LED4 = 6    # Output GPIO for LED4
BCM_LED2 = 13   # Output GPIO for LED2
BCM_LED1 = 19   # Output GPIO for LED1

# Function to set LEDs based on value of count

def dispCount(ct):
    ct = ct % 16                        # Set count mod 16
    binrep = bin(int(ct))[2:].zfill(4)  # Strips 0b from string and pads with 0s...to create a 4 character string
                                        # representing the binary value of the counter

    print("\n\n",binrep)                # Print the string in the console
    
    if binrep[0] == '1':                # Turn on the appropriate LEDs (where binrep contains 1 in designated position
        led8.set_on()
    else:
        led8.set_off()
        
    if binrep[1] == '1':    
        led4.set_on()
    else:
        led4.set_off()

    if binrep[2] == '1':
        led2.set_on()
    else:
        led2.set_off()

    if binrep[3] == '1':
        led1.set_on()
    else:
        led1.set_off()

# Beging main program        
        
GPIO.setmode(GPIO.BCM)      # Set mode to BCM numbering
pin = BCM_PIN               # set pin variable to the pin number to be used
GPIO.setup(pin,GPIO.IN)     # Initialize pin for input

led1 = LED_class.LED(BCM_LED1)      # Create LED objects (and initialize)
led2 = LED_class.LED(BCM_LED2)
led4 = LED_class.LED(BCM_LED4)
led8 = LED_class.LED(BCM_LED8)    

try:
    switch_state = 0                # Track state of switch
    counter = 0                     # Initialize counter
    while True:                     # Loop until interrupted (Ctl-C)
        if GPIO.input(pin)==0:      # If switch open
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
