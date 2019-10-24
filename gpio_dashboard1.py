import  tkinter         as tk
from    tkinter         import *
from    tkinter.ttk     import *   # Enhanced widgets????
import  PIN_class       as PIN
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
PWM_COL         = 4     # Column for PWM chkkbox
FREQ_COL        = 5     # Column for frequency spinner
D_CYC_COL       = 6     # Column for frequency spinner
EDGE_COL        = 8     # Column for edge menu
BOUNCE_COL      = 9     # Column number for bounce slider

DIR_MENU_OPTS   = ["IN","OUT"]
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
        master.title(DB_WINDOW_TITLE)

        # Add labels to header frame
        tk.Label(root,text = "PIN ID",  fg='blue',padx=COL_PAD,width=P_NM_COL_W).grid(row=0,column=P_NM_COL)
        tk.Label(root,text = " ",       fg='blue',padx=COL_PAD,width=COL_PAD).grid(row=0,column=1)
        tk.Label(root,text = "IN/OUT",  fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=DIR_IO_COL)
        tk.Label(root,text = "HIGH",    fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=OUT_HIGH_COL)
        tk.Label(root,text = "PWM",     fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=PWM_COL)
        tk.Label(root,text = "FREQ",    fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=FREQ_COL)
        tk.Label(root,text = "D_CYC",   fg='blue',padx=COL_PAD,width=P_RB_COL_W).grid(row=0,column=D_CYC_COL)
        tk.Label(root,text = " ",       fg='blue',padx=COL_PAD,width=COL_PAD).grid(row=0,column=7)
        tk.Label(root,text = "EDGE",    fg='blue',padx=COL_PAD,width=10).grid(row=0,column=EDGE_COL)
        tk.Label(root,text = "BOUNCE",  fg='blue',padx=COL_PAD,width=10).grid(row=0,column=BOUNCE_COL)

# --------------
# Function to create vars used to transfer widget changes and set pointer in PIN objects
#---------------

def set_widget_vars(pin):
        vDir = tk.StringVar()                   # Variable for pin direction
        pin.set_DIR_var(vDir)

        vCB_out = tk.IntVar(pin.LOW)            # Create variable for output-high button
        pin.set_OUT_var(vCB_out)                

        vCB_pwm = tk.IntVar(pin.PWM_OFF)        # Create variable for PWM chkbox
        pin.set_PWM_var(vCB_pwm)                

        vSB_freq = tk.StringVar("")             # Frequency 
        pin.set_FREQ_var(vSB_freq)           

        vSB_dcyc = tk.StringVar("")             # Duty cycle 
        pin.set_DCYC_var(vSB_dcyc)           

        vEdge = tk.StringVar("")                # Edge (Falling, rising, or both)
        pin.set_EDGE_var(vEdge)

        vBounce = tk.StringVar("")              # Bounce value
        pin.set_BOUNCE_var(vBounce)
        
# --------------
# Main line of program
#---------------

if not NO_GPIO:
        gpio = MYGPIO.myGPIO()  # My class to initialize GPIO

master = tk.Tk()          # Initialize gui
root = Canvas(master,width=600,height=100)
root.pack()
#vsb = Scrollbar(root,orient="vertical")
#vsb.pack(side="right")
create_DB_Header()

# Initialize pins
for p in PIN_LIST:
        pin_num=p[0]
        pin = PIN.PIN(pin_num)  # Create pin object

        vDir = tk.StringVar()
        vDir.set(DIR_MENU_OPTS[1])
        pin.set_DIR_var(vDir) 

        vCB_out = tk.IntVar(pin.LOW)    # Create variable for output-high button
        pin.set_OUT_var(vCB_out)        # Set pin to LOW#

        vCB_pwm = tk.IntVar(pin.PWM_OFF)# Create variable for PWM chkbox
        pin.set_PWM_var(vCB_pwm)        # Set pin to LOW

        vSB_freq = tk.StringVar("")              
        pin.set_FREQ_var(vSB_freq)           

        vSB_dcyc = tk.StringVar("")              
        pin.set_DCYC_var(vSB_dcyc)           

        vEdge = tk.StringVar("")
#        vEdge.set(EDGE_OPTS[0])
        pin.set_EDGE_var(vEdge)
#
        vBounce = tk.StringVar("")
#        vBounce.set(BOUNCE_OPTS[0])
        pin.set_BOUNCE_var(vBounce)
        
        
        # Add lbl(pin name) and other controls for each button
        pin_name    = tk.Label(root,padx=COL_PAD,width=P_NM_COL_W,text = "PIN-"+str(pin_num)+" "+p[1])
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
        

# Add colunm for In/Out selection
        oMenu_dir   = tk.OptionMenu(root,pin.get_DIR_var(),*DIR_MENU_OPTS,command = pin.dir_selected)
        oMenu_dir.config(width=5)
       
# Add column for forcing output to high
        cbox_high   = tk.Checkbutton(root,padx=COL_PAD,width=P_RB_COL_W,variable=pin.get_OUT_var(),onvalue=1,offvalue=0,command=pin.out_high_selected)

#Add columns for PWM
        pwmFrame = tk.Frame(root,relief=GROOVE,borderwidth=1,bg='black',height=3)
        pwmFrame.grid(row=pin_num-1,column=PWM_COL,columnspan=3)
        
        cbox_pwm        = tk.Checkbutton(pwmFrame,width=3,variable=pin.get_PWM_var(),onvalue=1,offvalue=0,command=pin.pwm_selected)
        sbox_freq       = tk.Spinbox(pwmFrame,bd=1,width=5,from_=1,to=100,textvariable=pin.get_FREQ_var(),command=pin.freq_selected)
        sbox_dcyc       = tk.Spinbox(pwmFrame,bd=1,width=5,from_=0,to=100,textvariable=pin.get_DCYC_var(),command=pin.dcyc_selected)
        sbox_freq.config(state='disabled')
        sbox_dcyc.config(state='disabled')

# Add columns for edge and bouce
        oMenu_edge      = tk.OptionMenu(root,pin.get_EDGE_var(),*EDGE_OPTS)
        oMenu_edge.config(width=9)

    #    oMenu_bounce   = tk.OptionMenu(root,vBounce,"0","100","200")
    #    oMenu_bounce.config(width=9)

#        scale_bounce = tk.Scale(root,vBounce,from_=1,to=100)
        scale_bounce    = tk.Scale(root,variable=pin.get_BOUNCE_var(),from_=1,to=200,orient=HORIZONTAL,command=pin.bounce_selected,bigincrement=10)
        
        # Position GUI elements

        pin_name.grid(row=pin_num-1,column=P_NM_COL)
        oMenu_dir.grid(row=pin_num-1,column=DIR_IO_COL)
        cbox_high.grid(row=pin_num-1,column=OUT_HIGH_COL)
        cbox_pwm.grid(row=pin_num-1,column=0)   # Column within PWM frame?
        sbox_freq.grid(row=pin_num-1,column=1)  # Column within PWM frame?
        sbox_dcyc.grid(row=pin_num-1,column=2)  # Column within PWM frame?
        oMenu_edge.grid(row=pin_num-1,column=EDGE_COL)
        
     #   oMenu_bounce.grid(row=pin_num-1,column=BOUNCE_COL)
        scale_bounce.grid(row=pin_num-1,column=BOUNCE_COL)


        # More GUI initializtion stuff

        if pin.get_direction() != pin.OUTPUT_TXT:# If direction is not output, 
                cbox_high.config(state=DISABLED)        # disable checkbox
        pin.set_CB_OH(cbox_high)                      # Store linkto checkbox object in pin instance
        pin.set_CB_PWM(cbox_pwm)
        pin.set_SB_FREQ(sbox_freq)
        pin.set_SB_DCYC(sbox_dcyc)
        pin.set_OM_EDGE(oMenu_edge)
      #  pin.set_OM_BOUNCE(oMenu_bounce)
        pin.set_OM_BOUNCE(scale_bounce) 
root.mainloop()

if not NO_GPIO:
        gpio.cleanup()

# End program
