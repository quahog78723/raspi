import  tkinter         as tk
from    tkinter         import ttk as ttk 
from    tkinter         import *   
from    tkinter.ttk     import *   # Enhanced widgets????
import  PIN_class       as PIN
import  MyScrollFrame_class as MSF
import  MY_GPIO_class   as MYGPIO

# --------------
# Constant definitions
# --------------

NO_GPIO         = False # Set to True to test program GUI with no GPIO calls
NUM_PINS        = 26    # Number of pins to be shown in dashboard
P_NM_COL_W      = 10    # Pin name column width
P_RB_COL_W      = 4     # Radiobutton column width
CB_COL_W        = 4     # Chkbox column width
COL_PAD         = 3     # Column padding

P_NM_COL        = 0     # Column number for pin name 
DIR_IO_COL      = 2     # Column number for input menu
OUT_HIGH_COL    = 3     # Column number for output high/low
FREQ_COL        = 4     # Column for frequency spinner
D_CYC_COL       = 5     # Column for frequency spinner
EDGE_COL        = 8     # Column for edge menu
BOUNCE_COL      = 9     # Column number for bounce slider

DIR_MENU_OPTS   = ["IN","OUT","PWM"]
EDGE_OPTS       = ["NONE","FALLING","RISING","BOTH"]
BOUNCE_OPTS     = ["0","100","200"]

I2C_COLOR       = 'blue'
SPI_COLOR       = 'magenta'
PCM_COLOR       = 'green'
UART_COLOR      = 'yellow'

DB_WINDOW_TITLE = "Bart's GPIO Dashboard"

PIN_LIST        = [[2,'I2C'],   \
                  [3,'I2C'],    \
                  [4,''],       \
                  [5,''],       \
                  [6,''],       \
                  [7,'SPI'],    \
                  [8,'SPI'],    \
                  [9,'SPI'],    \
                  [10,'SPI'],   \
                  [11,'SPI'],   \
                  [12,''],      \
                  [13,''],      \
                  [14,'UART'],  \
                  [15,'UART'],  \
                  [16,''],      \
                  [17,''],      \
                  [18,'PCM'],   \
                  [19,'PCM'],   \
                  [20,'PCM'],   \
                  [21,'PCM'],   \
                  [22,''],      \
                  [23,''],      \
                  [24,''],      \
                  [25,''],      \
                  [26,''],      \
                  [27,'']]

# --------------
# Function to build dashboard header
#---------------

def create_DB_Header():
    root.title(DB_WINDOW_TITLE)

    # Add labels to header frame
    tk.Label(scr_body,text = "PIN ID",  fg='blue',padx=COL_PAD,width=P_NM_COL_W).grid(row=0,column=P_NM_COL)
    tk.Label(scr_body,text = " ",       fg='blue',padx=COL_PAD,width=COL_PAD).grid(row=0,column=1)
    tk.Label(scr_body,text = "IN/OUT",  fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=DIR_IO_COL)
    tk.Label(scr_body,text = "HIGH",    fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=OUT_HIGH_COL)
    tk.Label(scr_body,text = "FREQ",    fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=FREQ_COL)
    tk.Label(scr_body,text = "D_CYC",   fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=D_CYC_COL)
    tk.Label(scr_body,text = " ",       fg='blue',padx=COL_PAD,width=COL_PAD).grid(row=0,column=7)
    tk.Label(scr_body,text = "EDGE",    fg='blue',padx=COL_PAD,width=10).grid(row=0,column=EDGE_COL)
    tk.Label(scr_body,text = "BOUNCE",  fg='blue',padx=COL_PAD,width=10).grid(row=0,column=BOUNCE_COL)

# --------------
# Function to initialize variables related to pin GUI items
#---------------

def init_pin_vars(pin):

    vDir = tk.StringVar("")           # Direction variable
    vDir.set(DIR_MENU_OPTS[0])      # Set to (IN)
    pin.set_DIR_var(vDir)           # Set reference to this varable in the pin object

    vCB_out = tk.IntVar(pin.LOW)    # Create variable for output-high checkbox and set to LOW (0)
    pin.set_OUT_var(vCB_out)        # Set reference to this varable in the pin object

    vSB_freq = tk.StringVar("")     # Create variable for frequency         
    pin.set_FREQ_var(vSB_freq)      # Set reference to this varable in the pin object     

    vSB_dcyc = tk.StringVar("")     # Create variable for duty-cycle         
    pin.set_DCYC_var(vSB_dcyc)      # Set reference to this varable in the pin object     

    vEdge = tk.StringVar("")        # Create variable for Edge
    vEdge.set(EDGE_OPTS[0])         # Det to "NONE"
    pin.set_EDGE_var(vEdge)         # Set reference to this varable in the pin object

    vBounce = tk.StringVar("")      # Create variable for Bounce
    pin.set_BOUNCE_var(vBounce)     # Set reference to this varable in the pin object
        
# --------------
# Main line of program
#---------------

if not NO_GPIO:
    gpio = MYGPIO.myGPIO()  # My class to initialize GPIO

root            = tk.Tk()          # Initialize gui
root.geometry('700x600')

body            = ttk.Frame(root) 
body.pack(fill=tk.BOTH,expand=True)

scr_body        = MSF.MyScrollFrame(body, width=16) 

create_DB_Header()

# Initialize pins
for p in PIN_LIST:
    pin = PIN.PIN(p[0])  # Create pin object based on pin number (p[0])

    init_pin_vars(pin)

    # Add lbl(pin name) and color coding based on pin attribute pin

    pin_name    = tk.Label(scr_body,padx=COL_PAD,width=P_NM_COL_W,text = "PIN-"+str(p[0])+" "+p[1])
    if p[1] == "PCM":
        pin_name.config(bg=PCM_COLOR)
    elif p[1] == "I2C":
        pin_name.config(bg=I2C_COLOR,fg='white')
    elif p[1] == "UART":
        pin_name.config(bg=UART_COLOR)
    elif p[1] == "SPI":
        pin_name.config(bg=SPI_COLOR)
    else:
        pass
    pin_name.grid(row=p[0]-1,column=P_NM_COL)
        
    # Add In/Out/PWM selection option menu
    oMenu_dir   = tk.OptionMenu(scr_body,pin.get_DIR_var(),*DIR_MENU_OPTS,command = pin.dir_selected)
    oMenu_dir.config(width=5,height=1)
    pin.set_OM_DIR(oMenu_dir)
    oMenu_dir.grid(row=p[0]-1,column=DIR_IO_COL)
        
    # Add output chxbox to set output to high, or to show high for input)
    cbox_high   = tk.Checkbutton(scr_body,padx=COL_PAD,width=P_RB_COL_W,height=1,variable=pin.get_OUT_var(),onvalue=1,offvalue=0,command=pin.out_high_selected)
    cbox_high.config(state='disabled')
    pin.set_CB_OH(cbox_high)                        # Store linkto checkbox object in pin instance
    cbox_high.grid(row=p[0]-1,column=OUT_HIGH_COL)
        
    # Add spin boxes for frequency selection and Duty cycle (for PWM)
    sbox_freq   = tk.Spinbox(scr_body,bd=1,width=5,from_=0,to=100,increment=5,textvariable=pin.get_FREQ_var(),command=pin.freq_selected)
    sbox_freq.config(state='disabled')
    pin.set_SB_FREQ(sbox_freq)
    sbox_freq.grid(row=p[0]-1,column=FREQ_COL)

    sbox_dcyc   = tk.Spinbox(scr_body,bd=1,width=5,from_=0,to=100,increment=5,textvariable=pin.get_DCYC_var(),command=pin.dcyc_selected)
    sbox_dcyc.config(state='disabled')
    pin.set_SB_DCYC(sbox_dcyc)
    sbox_dcyc.grid(row=p[0]-1,column=D_CYC_COL)
        
    # Add option menu for edge selection (for event detection)
    oMenu_edge  = tk.OptionMenu(scr_body,pin.get_EDGE_var(),*EDGE_OPTS)
    oMenu_edge.config(width=9,height=1)
    oMenu_edge.config(state='disabled')
    pin.set_OM_EDGE(oMenu_edge)
    oMenu_edge.grid(row=p[0]-1,column=EDGE_COL)
        
    # Add slider/scale for bounce selection (for event detection)
    scale_bounce = tk.Scale(scr_body,variable=pin.get_BOUNCE_var(),from_=1,to=200,orient=HORIZONTAL,command=pin.bounce_selected,bigincrement=10)
    scale_bounce.config(state='disabled')
    pin.set_SL_BOUNCE(scale_bounce)
    scale_bounce.grid(row=p[0]-1,column=BOUNCE_COL)
        

scr_body.update()
root.mainloop()

if not NO_GPIO:
    gpio.cleanup()

# End program
