import tkinter as tk
from tkinter import *
import PIN_class as PIN

# --------------
# Constant definitions
# --------------

NUM_PINS        = 10    # Number of pins to be shown in dashboard
P_NM_COL_W      = 10    # Pin name column width
P_RB_COL_W      = 6     # Radiobutton column width
COL_PAD         = 5    # Column padding
P_NM_COL        = 0     # Column number for pin name 
INPUT_COL       = 1     # Column number for input RB
OUTPUT_COL      = 2     # Column number for output RB

# --------------
# Main line of program
#---------------
pins=[]                 # Create an empty list of pins

root = tk.Tk()          # Initialize gui
root.title("GPIO Dashboard")

# Add labels to header frame
tk.Label(root,text = "PIN Name", fg='blue',padx=COL_PAD,width=P_NM_COL_W).grid(row=0,column=P_NM_COL)
tk.Label(root,text = "INPUT",    fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=INPUT_COL)
tk.Label(root,text = "OUTPUT",   fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=OUTPUT_COL)
         
# for each pin (start numbering at 1)
for i in range(1,NUM_PINS+1):
	pin = PIN.PIN(i)                # Create pin object
	v = tk.IntVar()                 # Create pin specific var to hold value of rb clicked
	v.set(pin.UNDEFINED)            # Set default value of RBs to value to UNDEFINED
	pin.set_var(v)                  # Set the initial mode of pin to UNDEFINED

	# Add lbl(pin name) and three radio buttons to each frame
	lbl = tk.Label(root,padx=COL_PAD,width=P_NM_COL_W,text = "PIN-"+str(i))
	but_input   = tk.Radiobutton(root,padx=COL_PAD,width=P_RB_COL_W,variable=v,value=pin.INPUT,command=pin.pin_selected)
	but_output  = tk.Radiobutton(root,padx=COL_PAD,width=P_RB_COL_W,variable=v,value=pin.OUTPUT,command=pin.pin_selected)

	lbl.grid(row=i,column=P_NM_COL)
	but_input.grid(row=i,column=INPUT_COL)
	but_output.grid(row=i,column=OUTPUT_COL)
	
	pins.append([lbl,pin])  # Is this needed/useful?
	
root.mainloop()

# End program
