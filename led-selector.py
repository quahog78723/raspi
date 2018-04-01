# A simple GUI based on Tkinter used to turn LEDs on or off.

import tkinter				# Import tkinter for GUI stuff
import RPi.GPIO as GPIO		# Import RPi.GPIO as GPIO
import LED_class			# Import our LED_class fiel that includes our LED class

BCM_LED8 = 5   				# Output GPIO for LED8
BCM_LED4 = 6    			# Output GPIO for LED4
BCM_LED2 = 13   			# Output GPIO for LED2
BCM_LED1 = 19   			# Output GPIO for LED1

def showChoice():           # Functiom to be called whenever the user selects a new LED to be turned on
	print("Button: ",v.get())   # Shows a text messge in console containing the button that has been clicked
	led = v.get()           # Get the LED nuber associated with the radio button clicked
	if led == 1:            # If 1, turn on 1 and turn off others
		led1.set_on()
		led2.set_off()
		led4.set_off()
		led8.set_off()
	elif led == 2:          # IF 2, turn on 2 and turn off others
		led1.set_off()	
		led2.set_on()
		led4.set_off()
		led8.set_off()
	elif led == 4:          # If 4, turn on 4 and turn off others
		led1.set_off()
		led2.set_off()
		led4.set_on()
		led8.set_off()
	elif led == 8:          # If 8, turn on 8 and turn off others
		led1.set_off()
		led2.set_off()
		led4.set_off()
		led8.set_on()
	else:                   # Should never get to this point
		pass
        
# Main line of program

GPIO.setmode(GPIO.BCM)              # Set mode to use BCM convention for pins      
led1 = LED_class.LED(BCM_LED1)      # Create LED objects (and initialize)
led2 = LED_class.LED(BCM_LED2)
led4 = LED_class.LED(BCM_LED4)
led8 = LED_class.LED(BCM_LED8)  

root = tkinter.Tk()                 # Initialize GUI
root.title("LED Selector")          # Add title for window

v = tkinter.IntVar()                # define tinker integer varialbe that will hold ID of button clicked
v.set(0)                            # Initially no LED will be on... 0 indicates a non-existant LED identifier

prompt = tkinter.Label(text="Select LED",fg="blue") # Add prompt to GUI

rb8 = tkinter.Radiobutton(text="LED8",value=8,variable = v,command=showChoice) # Add Radiobuttons to GUI
rb4 = tkinter.Radiobutton(text="LED4",value=4,variable = v,command=showChoice)
rb2 = tkinter.Radiobutton(text="LED2",value=2,variable = v,command=showChoice)
rb1 = tkinter.Radiobutton(text="LED1",value=1,variable = v,command=showChoice)

prompt.pack()                       # Display items defined above
rb1.pack()
rb2.pack()
rb4.pack()
rb8.pack()

root.mainloop()                     # Enter GUI main loop

print("Cleaning up GPIO.")          # When exiting GUI...print message, and
GPIO.cleanup()                      # Reset GPIO

# End of program
