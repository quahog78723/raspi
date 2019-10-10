# Switch counter
# Bart Jacob
#
# This program counts the number of times a switch is pressed and
# displays the count(mod 16) via 4 LEDS.


import RPi.GPIO as GPIO
import time

BRD_PIN = 15    # PIN number used based on board numbering
BCM_PIN = 4     # PIN number used based on Broadcom numbering

BCM_LED8 = 26   # BCM pin numbers used for LEDs
BCM_LED4 = 13
BCM_LED2 = 6
BCM_LED1 = 5

def LEDsetup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BCM_LED8,GPIO.OUT)   # Init pins for output
    GPIO.setup(BCM_LED4,GPIO.OUT)
    GPIO.setup(BCM_LED2,GPIO.OUT)
    GPIO.setup(BCM_LED1,GPIO.OUT)
    GPIO.output(BCM_LED8,False)     # Set LEDs off
    GPIO.output(BCM_LED4,False)
    GPIO.output(BCM_LED2,False)
    GPIO.output(BCM_LED1,False)
    
    
def dispCount(ct):
    ct = ct % 16     # Set count mod 16
    if ct // 8 != 0:
        GPIO.output(BCM_LED8,True)
    else:
        GPIO.output(BCM_LED8,False)
    ct = ct % 8     # Set count mod 16
    if ct // 4 != 0:
        GPIO.output(BCM_LED4,True)
    else:
        GPIO.output(BCM_LED4,False)
    ct = ct % 4     # Set count mod 16
    if ct // 2 != 0:
        GPIO.output(BCM_LED2,True)
    else:
        GPIO.output(BCM_LED2,False)

    ct = ct % 2     # Set count mod 16
    if ct != 0:
        GPIO.output(BCM_LED1,True)
    else:
        GPIO.output(BCM_LED1,False)


valid_type = False  # Used to indicate valid input entered

while not valid_type:   # While no valid input
    type = input('Enter 1 for Board, 2 for BCM : ')
    if type == "1":     # Board input selected
        GPIO.setmode(GPIO.BOARD)    # Set mode to board numbering
        pin = BRD_PIN               # Set pin number to use
        valid_type = True           # Valid input indicator
        print("Using Board Pin : ",pin) 
    elif type == "2":   # Broadcom numbering chosen
        GPIO.setmode(GPIO.BCM)      # Set mode to BCM numbering
        pin = BCM_PIN               # Set pin number to use
        valid_type = True           # Valid input indicator
        print("Using BCM Pin : ",pin)
    else:                           # Invalid input
        print("Invalid type, try again.\n")

GPIO.setup(pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)             # Initialize pin for input
LEDsetup()

try:
    switch_state = 0                # Track state of switch
    counter = 0                     # Initialize counter
    print("Open", end='')
    loopCtr = 0
    while True:                     # Loop until interrupted (Ctl-C)
        loopCtr += 1
        loopCtr = loopCtr % 10000
        if loopCtr == 0:
            print('.',end='')
        if GPIO.input(pin)==0:      # If switch open
            if switch_state == 1:   
                switch_state = 0    # Set switch state
                print("\nOpen",end='')       # Print state
                time.sleep(.1)
           # print("0", end='')      # Print a 0
        else:   
            if switch_state == 0:   # If switch was open, and is now closed.
                switch_state = 1    # Change switch state
                counter += 1        # Increment counter
                dispCount(counter)
                print("\nClosed",end='')     # Print state
                time.sleep(.1)
           # print("1",end="")       # Print 1
            
except KeyboardInterrupt:           # When Ctl-C ...break out of program
    print("\n\nProgram ending.")
    print("Switch pressed",counter,"times.")    # Print switch counter
                  
finally:
    print("Cleaning up GPIO.")      
    GPIO.cleanup()                  # Reset GPIO
