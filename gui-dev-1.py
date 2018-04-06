import tkinter as tk
from tkinter import *
import PIN_class as PIN

NUM_PINS    = 10

# --------------
# Main line of program
#---------------

root = tk.Tk()          # Initialize gui
root.title("GPIO Dashboard")

pins=[]               # Create an empty list of pins
#frames = []             # Create an empty list of individual gui frames

fhdr = tk.Frame(root,relief=RIDGE)  # Create header frame
fhdr.grid(row=0,column=0)           # add header frame to grid

# Add 4 labels to header frame
tk.Label(fhdr,text = "PIN Name", relief=RIDGE,padx=10,width=10).grid(row=0,column=0)
tk.Label(fhdr,text = "RESET", relief=RIDGE,padx=10,width=10).grid(row=0,column=1)
tk.Label(fhdr,text = "INPUT", relief=RIDGE,padx=10,width=10).grid(row=0,column=2)
tk.Label(fhdr,text = "OUTPUT", relief=RIDGE,padx=10,width=10).grid(row=0,column=3)
         
# for each pin (start numbering at 1)
for i in range(1,NUM_PINS+1):
	f = tk.Frame(root,relief=RIDGE) # Create a new frame for each pin
	f.grid(row=i,column=0)

	pin = PIN.PIN(i)
	v = tk.IntVar()           # Create pin specific string var
	v.set(pin.UNDEFINED)         # Set value to UNDEFINED
	pin.set_var(v)

	# Add lbl(pin name) and three radio buttons to each frame
	lbl = tk.Label(f,padx=10,width=10,text = "PIN"+str(i), relief=RIDGE)
	but_reset   = tk.Radiobutton(f,padx=10,width=10,variable=v,value=pin.UNDEFINED,command=pin.pin_selected)
	but_input   = tk.Radiobutton(f,padx=10,width=10,variable=v,value=pin.INPUT,command=pin.pin_selected)
	but_output  = tk.Radiobutton(f,padx=10,width=10,variable=v,value=pin.OUTPUT,command=pin.pin_selected)

	lbl.grid(row=i,column=0)
	but_reset.grid(row=i,column=1)
	but_input.grid(row=i,column=2)
	but_output.grid(row=i,column=3)
	
	pins.append([lbl,pin])  # Is this needed?
	
root.mainloop()

# End program
