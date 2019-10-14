# The PIN class provides a simple way to interface with individual GPIO PINs and will maintain
# various attributes associated with the PIN.

import RPi.GPIO as GPIO                                        # Use RPi.GPIO module and reference as GPIO

class PIN:              # Define PIN class
        # --------------
        # class variables (constants)
        # --------------
        NO_GPIO = False         # Used for debugging GUI without calling GPIO

        UNDEFINED = -1     # Used for direction or high/low status
        INPUT = 1          # Input direction indicator
        OUTPUT = 0         # Output direction indicator
        INPUT_TXT = "IN"
        OUTPUT_TXT = "OUT"
        LOW = 0            # Pin low indicator
        HIGH = 1           # Pin high indicator
        PWM_ON = 1
        PWM_OFF = 0
        ED_ON = 1
        ED_OFF = 0
        
        # --------------
        # Constructor method...called when instance is created
        # --------------        
        def __init__(self,pin):         # pin is an integer identifying the pin number (assume BOARD mode numbering

              # Instance variables
              
                self.__id = pin                         # Set ID to pin number
                self.__direction = PIN.INPUT_TXT        # Variable indicating current direction
                self.__status   = PIN.LOW               # Variable indicating high/low pin status       
                self.__pwm      = PIN.PWM_OFF           # Variable to point to pwm object if initialized
                self.__event_det = PIN.ED_OFF           # Indicates if event detection is on or off for this pin

                # Variables used to access GUI controls
                
                self.__OM_dir   = PIN.UNDEFINED
                self.__CB_outH  = PIN.UNDEFINED  
                self.__SB_freq  = PIN.UNDEFINED
                self.__SB_dcyc  = PIN.UNDEFINED

                # Variables used by GUI controls to pass new value of changed widget
                
                self.__DIR_var  = PIN.UNDEFINED
                self.__OH_var   = PIN.UNDEFINED        
                self.__PWM_var  = PIN.UNDEFINED
                self.__FREQ_var = PIN.UNDEFINED             
                self.__DCYC_var = PIN.UNDEFINED             
                self.__EDGE_var = PIN.UNDEFINED             
                self.__BOUNCE_var = PIN.UNDEFINED           

                # Reset output
                
                self.set_direction(PIN.OUTPUT_TXT)      # Initialize direction to output
                self.set_output(False)                  # Set output to False (low) - Needed because of 'sticky' behavior of RPi
#                self.set_direction(PIN.INPUT_TXT)       # Set direction to input

                if not PIN.NO_GPIO:
                        GPIO.setwarnings(False)

        # --------------
        # Methods to return instance variables
        # --------------
        def get_id(self):               # PIN id
                return self.__id

        def get_direction(self):        # PIN dirrection
                return self.__direction

        def get_status(self):           # Output high/low
                return (self.__status)

        def get_pwm(self):              # PWM off/on
                return (self.__pwm)

        def get_event_det(self):        # Event detection off/on
                return self.__event_det

        # --------------
        # Methods to set/get tkinter variable associated with direction option menu
        # --------------
        def set_DIR_var(self,var):
                self.__DIR_var = var

        def get_DIR_var(self):
                return self.__DIR_var

        # --------------
        # Methods to set/get tkinter variable associated with output high chkbox
        # --------------
        def set_OUT_var(self,var):
                self.__OH_var = var

        def get_OUT_var(self):
                return self.__OH_var
        
        # --------------
        # Methods to set/get tkinter variable associated with PWM high chkbox
        # --------------
        def set_PWM_var(self,var):
                self.__PWM_var = var

        def get_PWM_var(self):
                return self.__PWM_var
        
        # --------------
        # Methods to set/get tkinter variable associated with Frequency spinbox
        # --------------
        def set_FREQ_var(self,var):
                self.__FREQ_var = var

        def get_FREQ_var(self):
                return self.__FREQ_var
                
        # --------------
        # Methods to set/get tkinter variable associated with DutyCycle spinbox
        # --------------
        def set_DCYC_var(self,var):
                self.__DCYC_var = var

        def get_DCYC_var(self):
                return self.__DCYC_var

        # --------------
        # Methods to set/get tkinter variable associated with edge widget
        # --------------
        def set_EDGE_var(self,var):
                self.__EDGE_var = var

        def get_EDGE_var(self):
                return self.__EDGE_var      

        # --------------
        # Methods to set/get tkinter variable associated with bounce widget
        # --------------
        def set_BOUNCE_var(self,var):
                self.__BOUNCE_var = var

        def get_BOUNCE_var(self):
                return self.__BOUNCE_var

        # --------------
        # Methods to set/get references to GUI widgets
        # --------------
        def set_OM_DIR(self,widget):
                self.__OM_dir = widget

        def get_OM_DIR(self):
                return self.__OM_DIR

        def set_CB_OH(self,widget):
                self.__CB_outH = widget

        def get_CB_OH(self):
                return self.__CB_outH

        def set_CB_PWM(self,widget):
                self.__PWM_cBox = widget

        def get_CB_PWM(self):
                return __PWM_cBox

        def set_SB_FREQ(self,widget):
                self.__SB_freq = widget

        def get_SB_FREQ(self):
                return __SB_freq

        def set_SB_DCYC(self,widget):
                self.__SB_dcyc = widget

        def get_SB_DCYC(self):
                return __SB_dcyc
        
        def set_OM_EDGE(self,widget):
                self.__OM_edge = widget

        def get_OM_EDGE(self):
                return self.__OM_edge
        
        def set_OM_BOUNCE(self,widget):
                self.__OM_bounce = widget

        def get_OM_BOUNCE(self):
                return __OM_bounce
        
        # --------------
        # Method to set direction (input or output) of pin
        # --------------
        def set_direction(self, dir):
                if dir == PIN.INPUT_TXT:                        # If input
                        self.__direction = dir                  # Set __direction variable
                        if not PIN.NO_GPIO:
                                GPIO.setup(self.get_id(),GPIO.IN) # Set pin for input
                        if self.get_CB_OH() != self.UNDEFINED:    # If gui chkbox exists, disable chkbox
                                self.__CB_outH.deselect()
                                self.__CB_outH.config(state="disabled")
                                self.unset_eventDet()
                                #
                                # Need to add logic to change OM_EDGE to NONE
                                #
                elif dir == PIN.OUTPUT_TXT:                     # if output
                        self.__direction = dir                  # Set __direction variable
                        try:
                                if self.__event_det == PIN.ED_ON:
                                        self.__event_det = PIN.ED_OFF
                                        if not PIN.NO_GPIO:
                                                GPIO.remove_event_detect(self.get_id())        
                        except Exception as err:
                                print("***",end=" ")
                                print(err)
                        if not PIN.NO_GPIO:
                                GPIO.setup(self.get_id(),GPIO.OUT)          # Set pin for output
                        if self.__CB_outH != self.UNDEFINED:     # If gui chkbox exists... 
                                self.__CB_outH.config(state="normal") #  enable chkbox
                                if self.get_status():
                                        self.__CB_outH.select()
                                else:
                                        self.__CB_outH.deselect()
                else:
                        print("Error ...shold not get here.")

        # --------------
        # Methods to add/remove event detection for a pin
        # --------------
        def set_eventDet(self, edge):          
                if (self.__id != 19) and (self.__id != 21) :  # pin 19 and 21 seem to constantly switch state
                        if not PIN.NO_GPIO:
                              GPIO.add_event_detect(self.__id,edge,callback=self.callback_pin_state_change,bouncetime=200)
                        self.__event_det = PIN.ED_ON

        def unset_eventDet(self):
                GPIO.remove_event_detect(self.get_id())
                


        # --------------
        # Method to set output pin to high or low
        # --------------
        def set_output(self,val):              # Pass boolean vaue to indicate whether to turn on (True) or off (False)
                if self.get_direction() == PIN.OUTPUT_TXT:  # Only if pin is configured for output
                        self.__status = val             # Set status to val
                        if not PIN.NO_GPIO:
                                GPIO.output(self.__id,val)      # Set pin to high/low
                else:
                        print("PIN is not set for output")

        # --------------
        # Method to self describe instance info...called by print function
        # --------------
        def __str__(self):
                return "PIN ID: " + str(self.__id) + "\tDirection: " + str(self.__direction) +  "\tStatus: " + str(self.__status)

        
        # --------------
        # Method called when a direction oMenu option is selected
        # --------------
        def dir_selected(self,dir):
                selected_mode = dir
                print("Direction selected:", dir)
                if selected_mode == self.get_direction():
                        print("Button already selected")
                else:
                        self.set_direction(selected_mode)
                        
        # --------------
        # Method called when the set high chkbox is clicked
        # --------------
        def out_high_selected(self):
                if self.__OH_var.get() == self.HIGH:
                        print(" Pin: ",self.get_id()," set HIGH")
                else:
                        print(" Pin: ",self.get_id()," set LOW")
                self.set_output(self.__OH_var.get())
                
        # --------------
        # Method called when the pwm chk box is clicked
        # --------------
        def pwm_selected(self):
                if self.__PWM_var.get() == self.PWM_ON:
                        print(" Pin: ",self.get_id()," turn PWM on (not implement yet)")
                        self.__SB_freq.config(state='normal')
                        self.__SB_dcyc.config(state='normal')
                               
                        if self.get_direction() == self.OUTPUT_TXT:
                                if not PIN.NO_GPIO:
                                        self.__pwm = GPIO.PWM(self.__id,50)
                                        self.__pwm.start(50)                            
                else:
                        print(" Pin: ",self.get_id(),"turn PWM off (not implement yet)")
                        self.__SB_freq.config(state='disable')
                        self.__SB_dcyc.config(state='disable')
                               
                        if self.__pwm != 0:
                                self.__pwm.stop()
                                self.__pwm = 0
                                        
                # !!!!!!!!!!!!!!!!!!!!!!
                # Need logic to set PWM
                # !!!!!!!!!!!!!!!!!!!!!!

        # --------------
        # Method called when the Freq SB is changed
        # --------------
        def freq_selected(self):
                print(" Pin: " , self.get_id() , "frequency changed to ",self.__FREQ_var.get())

        # --------------
        # Method called when the DCYC SB is changed
        # --------------
        def dcyc_selected(self):
                print(" Pin: " , self.get_id(), "duty cycle changed to ",self.__DCYC_var.get())

        # --------------
        # Method called when Bounce widget is changed
        # --------------
        def bounce_selected(self,val):
                print(" Pin: " , self.get_id(), "bounce ",val)

        # --------------
        # Call back for input pin
        # --------------
        def callback_pin_state_change(self,channel):
                print(" Pin ",self.get_id()," has changed")
                if not PIN.NO_GPIO:
                        if GPIO.input(self.__id)==self.HIGH:
                                print("Pin",self.__id," is HIGH")
                        else:
                                print("Pin",self.__id," is LOW")
                
 
# End of PIN class
