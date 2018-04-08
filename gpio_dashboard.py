import tkinter as tk
from tkinter import *
import PIN_class as PIN
import MY_GPIO as MYGPIO

# --------------
# Constant definitions
# --------------

NUM_PINS        = 26    # Number of pins to be shown in dashboard
P_NM_COL_W      = 10    # Pin name column width
P_RB_COL_W      = 6     # Radiobutton column width
CB_COL_W        = 6     # Chkbox column width
COL_PAD         = 5     # Column padding

P_NM_COL        = 0     # Column number for pin name 
DIR_I_COL       = 1     # Column number for input RB
DIR_O_COL       = 2     # Column number for output RB
OUT_HIGH_COL    = 3

DB_WINDOW_TITLE = "GPIO Dashboard"
# --------------
# Function to build dashboard header
#---------------
def create_DB_Header():
        root.title(DB_WINDOW_TITLE)

        # Add labels to header frame
        tk.Label(root,text = "PIN Name", fg='blue',padx=COL_PAD,width=P_NM_COL_W).grid(row=0,column=P_NM_COL)
        tk.Label(root,text = "INPUT",    fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=DIR_I_COL)
        tk.Label(root,text = "OUTPUT",   fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=DIR_O_COL)
        tk.Label(root,text = "OUT-HIGH", fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=OUT_HIGH_COL)

        



# --------------
# Main line of program
#---------------

gpio = MYGPIO.myGPIO()  # My class to initialize GPIO

root = tk.Tk()          # Initialize gui

create_DB_Header()

# for each pin (start numbering at 1)
for i in range(2,NUM_PINS+2):
        pin = PIN.PIN(i)                # Create pin object

        vRB = tk.IntVar()               # Create pin specific var to hold value of rb clicked
        vRB.set(pin.INPUT)              # Set default value of RBs to value to INPUT
        pin.set_dir_var(vRB)            # Set the RB to INPUT

        vOH = tk.IntVar()               # Create variable for output-high button
        vOH.set(pin.LOW)                # Set default value to LOW
        pin.set_OH_var(vOH)             # Set pin to LOW

        # Add lbl(pin name) and other controls for each button
        lbl = tk.Label(root,padx=COL_PAD,width=P_NM_COL_W,text = "PIN-"+str(i))
        but_input   = tk.Radiobutton(root,padx=COL_PAD,width=P_RB_COL_W,variable=vRB,value=pin.INPUT,command=pin.pin_selected)
        but_output  = tk.Radiobutton(root,padx=COL_PAD,width=P_RB_COL_W,variable=vRB,value=pin.OUTPUT,command=pin.pin_selected)
        cbox_high   = tk.Checkbutton(root,padx=COL_PAD,width=P_RB_COL_W,variable=vOH,onvalue=1,offvalue=0,command=pin.out_high_selected)

        # Position GUI elements

        lbl.grid(row=i-1,column=P_NM_COL)
        but_input.grid(row=i-1,column=DIR_I_COL)
        but_output.grid(row=i-1,column=DIR_O_COL)
        cbox_high.grid(row=i-1,column=OUT_HIGH_COL)

        # More GUI initializtio stuff
        if pin.get_direction != pin.OUTPUT:             # If direction is not output, 
                cbox_high.config(state=DISABLED)        # disable checkbox
        pin.set_OH_cBox(cbox_high)                      # Store linkto checkbox object in pin instance
        pin.set_RB_inp(but_input)
        pin.set_RB_out(but_output)
root.mainloop()

gpio.cleanup()

# End program
