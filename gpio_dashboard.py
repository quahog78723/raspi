import tkinter as tk
from tkinter import *
import PIN_class as PIN
import MY_GPIO_class as MYGPIO

# --------------
# Constant definitions
# --------------

NUM_PINS        = 26    # Number of pins to be shown in dashboard
P_NM_COL_W      = 10     # Pin name column width
P_RB_COL_W      = 4     # Radiobutton column width
CB_COL_W        = 4     # Chkbox column width
COL_PAD         = 3     # Column padding

P_NM_COL        = 0     # Column number for pin name 
DIR_I_COL       = 1     # Column number for input RB
DIR_O_COL       = 2     # Column number for output RB
OUT_HIGH_COL    = 3     # Column number for output high/low
PWM_COL         = 4     # Column for PWM chkkbox
FREQ_COL        = 5     # Column for frequency spinner
D_CYC_COL       = 6     # Column for frequency spinner
EDGE_COL        = 7
BOUNCE_COL      = 8

I2C_COLOR='blue'
SPI_COLOR='magenta'
PCM_COLOR='green'
UART_COLOR='yellow'

DB_WINDOW_TITLE = "GPIO Dashboard"
PIN_FUNC=[[2,'I2C'], \
          [3,'I2C'], \
          [4,''], \
          [5,''], \
          [6,''], \
          [7,'SPI'], \
          [8,'SPI'], \
          [9,'SPI'], \
          [10,'SPI'], \
          [11,'SPI'], \
          [12,''], \
          [13,''], \
          [14,'UART'], \
          [15,'UART'], \
          [16,''], \
          [17,''], \
          [18,'PCM'], \
          [19,'PCM'], \
          [20,'PCM'], \
          [21,'PCM'], \
          [22,''], \
          [23,''], \
          [24,''], \
          [25,''], \
          [26,''], \
          [27,'']]


# --------------
# Function to build dashboard header
#---------------
def create_DB_Header():
        root.title(DB_WINDOW_TITLE)

        # Add labels to header frame
        tk.Label(root,text = "PIN ID", fg='blue',padx=COL_PAD,width=P_NM_COL_W).grid(row=0,column=P_NM_COL)
        tk.Label(root,text = "IN",     fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=DIR_I_COL)
        tk.Label(root,text = "OUT",    fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=DIR_O_COL)
        tk.Label(root,text = "HIGH",   fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=OUT_HIGH_COL)
        tk.Label(root,text = "PWM",    fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=PWM_COL)
        tk.Label(root,text = "FREQ",   fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=FREQ_COL)
        tk.Label(root,text = "D_CYC",  fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=D_CYC_COL)
        tk.Label(root,text = "EDGE",   fg='blue',padx=COL_PAD,width=10).grid(row=0,column=EDGE_COL)
        tk.Label(root,text = "BOUNCE", fg='blue',padx=COL_PAD,width=10).grid(row=0,column=BOUNCE_COL)


# --------------
# Main line of program
#---------------

gpio = MYGPIO.myGPIO()  # My class to initialize GPIO

root = tk.Tk()          # Initialize gui

create_DB_Header()

# for each pin (start numbering at 1)
#for i in range(2,NUM_PINS+2):
for x in PIN_FUNC:
        pin_num=x[0]
        pin = PIN.PIN(pin_num)                # Create pin object

        vRB_dir = tk.IntVar()     # Create pin specific var to hold value of rb clicked
        vRB_dir.set(pin.INPUT)
        pin.set_DIR_var(vRB_dir)            # Set the RB to INPUT

        vCB_out = tk.IntVar(pin.LOW)    # Create variable for output-high button
        pin.set_OUT_var(vCB_out)             # Set pin to LOW

        vCB_pwm = tk.IntVar(pin.PWM_OFF)              # Create variable for PWM chkbox
        pin.set_PWM_var(vCB_pwm)           # Set pin to LOW

        vSB_freq = tk.StringVar("")              
        pin.set_FREQ_var(vSB_freq)           

        vSB_dcyc = tk.StringVar("")              
        pin.set_DCYC_var(vSB_dcyc)           


        # Add lbl(pin name) and other controls for each button
        pin_name    = tk.Label(root,padx=COL_PAD,width=P_NM_COL_W,text = "PIN-"+str(pin_num)+" "+x[1])
        if x[1] == "PCM":
                pin_name.config(bg=PCM_COLOR)
        elif x[1] == "I2C":
                pin_name.config(bg=I2C_COLOR,fg='white')
        elif x[1] == "UART":
                pin_name.config(bg=UART_COLOR)
        elif x[1] == "SPI":
                pin_name.config(bg=SPI_COLOR)
        else:
                pass
        
        myframe = tk.Frame(root,relief=GROOVE,borderwidth=1,bg='black')
        myframe.grid(row=pin_num-1,column=DIR_I_COL,columnspan=2)
        but_input   = tk.Radiobutton(myframe,padx=COL_PAD,width=P_RB_COL_W,variable=vRB_dir,value=pin.INPUT,command=pin.pin_selected)
        but_output  = tk.Radiobutton(myframe,padx=COL_PAD,width=P_RB_COL_W,variable=vRB_dir,value=pin.OUTPUT,command=pin.pin_selected)
        cbox_high   = tk.Checkbutton(root,padx=COL_PAD,width=P_RB_COL_W,variable=vCB_out,onvalue=1,offvalue=0,command=pin.out_high_selected)
        cbox_pwm    = tk.Checkbutton(root,padx=COL_PAD,width=P_RB_COL_W,variable=vCB_pwm,onvalue=1,offvalue=0,command=pin.pwm_selected)
        sbox_freq   = tk.Spinbox(root,bd=3,width=P_RB_COL_W,from_=1,to=100,textvariable=vSB_freq,command=pin.freq_selected)
        sbox_dcyc   = tk.Spinbox(root,bd=3,width=P_RB_COL_W,from_=0,to=100,textvariable=vSB_dcyc,command=pin.dcyc_selected)
        vLB_edge = tk.StringVar("")
        oMenu_edge   = tk.OptionMenu(root,vLB_edge,"RISING","FALLING","BOTH")
        oMenu_edge.config(width=9)

        # Position GUI elements

        pin_name.grid(row=pin_num-1,column=P_NM_COL)
        but_input.grid(row=pin_num-1,column=0)
        but_output.grid(row=pin_num-1,column=1)
        cbox_high.grid(row=pin_num-1,column=OUT_HIGH_COL)
        cbox_pwm.grid(row=pin_num-1,column=PWM_COL)
        sbox_freq.grid(row=pin_num-1,column=FREQ_COL)
        sbox_dcyc.grid(row=pin_num-1,column=D_CYC_COL)
        oMenu_edge.grid(row=pin_num-1,column=EDGE_COL)
        # More GUI initializtio stuff
        if pin.get_direction != pin.OUTPUT:             # If direction is not output, 
                cbox_high.config(state=DISABLED)        # disable checkbox
        pin.set_OH_CBX(cbox_high)                      # Store linkto checkbox object in pin instance
        pin.set_INP_RB(but_input)
        pin.set_OUT_RB(but_output)
        pin.set_PWM_CBX(cbox_pwm)
root.mainloop()

gpio.cleanup()

# End program
