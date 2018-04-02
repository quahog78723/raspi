# A simple GUI based on Tkinter used to turn LEDs on or off.

import tkinter				# Import tkinter for GUI stuff
import RPi.GPIO as GPIO			# Import RPi.GPIO as GPIO
import LED_class			# Import our LED_class fiel that includes our LED class

LED_PORT_LIST = [5,6,13,19]                # Ports for LED1, LED2,...
NUM_LEDS = len(LED_PORT_LIST)
# --------------
# Function to turn on/off LEDs when button clicked
# --------------
def setLEDs():                          # Function to be called whenever the user selects a new LED to be turned on
        but = v.get()                   # Get the LED number associated with the radio button clicked	
        print("Button: ",but, "LED: ",but + 1)   	# Shows a text messge in console containing the button that has been clicked     	
        for i in range(0,len(LED_PORT_LIST)):   # For each LED, set on/off based on
            led_list[i].set(i==but)             # if the LED matches the button clicked

# ---------------
# Main line of program
# ---------------

# Set up GUI

root = tkinter.Tk()                 # Initialize GUI
root.title("LED Selector")          # Add title for window

v = tkinter.IntVar()                # define tinker integer varialbe that will hold ID of button clicked
v.set(-1)                           # Initially no LED will be on... -1 indicates a non-existant LED identifier

prompt = tkinter.Label(text="Select LED",fg="blue") # Add prompt to GUI
prompt.pack()                       # Displays prompt defined above in GUI

rb_list = [0] * NUM_LEDS            # Initialize readio button list
for i in range(0,NUM_LEDS):         # Create a button for each LED
	rb_list[i] = tkinter.Radiobutton(text="LED"+str(i+1),value=i,variable=v,command=setLEDs) # Add Radiobuttons to GUI
	rb_list[i].pack()

# Set up GPIO

GPIO.setmode(GPIO.BCM)              # Set mode to use BCM convention for pins

# Create LED objects
led_list = [0] * NUM_LEDS           # Initialize list
for i in range(NUM_LEDS):           # For each LED
    led_list[i] = LED_class.LED(LED_PORT_LIST[i])     # Create LED objects (and initialize)

# Enter GUI main loop
root.mainloop()                     # Enter GUI main loop

# Clean up after exiting GUI
print("Cleaning up GPIO.")          # When exiting GUI...print message, and
GPIO.cleanup()                      # Reset GPIO

# End of program
