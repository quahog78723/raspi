# The PIN class provides a simple way to interface with individual GPIO PINs and will maintain
# various attributes associated with the PIN.

import RPi.GPIO as GPIO                                        # Use RPi.GPIO module and reference as GPIO

class PIN:                                                              # Define PIN class
        # --------------
        # Constructor method...called when instance is created
        # --------------        
        def __init__(self,pin):         # pin is an integer identifying the pin number (assume BOARD mode numbering
                self.UNDEFINED = -1     # Used for direction or high/low status
                self.INPUT = 1          # Input direction indicator
                self.OUTPUT = 0         # Output direction indicator
                self.INPUT_TXT = "IN"
                self.OUTPUT_TXT = "OUT"
                self.LOW = 0            # Pin low indicator
                self.HIGH = 1           # Pin high indicator
                self.PWM_ON = 1
                self.PWM_OFF = 0

              # Instance variables  
                self.__id = pin         # Set ID to pin number
                self.__direction = self.INPUT_TXT    # Variable indicating current direction
                self.__status = 0       # Variable indicating high/low pin status
                self.__pwm = 0          # Variable to point to pwm object if initialized
                self.__event_det = 0    # Indicates if event detection is on or off for this pin

                # Variables used to access GUI controls
#                self.__RB_inp = self.UNDEFINED
#                self.__RB_out = self.UNDEFINED
                self.__OM_DIR = self.UNDEFINED
                self.__OH_cBox = self.UNDEFINED  
                self.__SB_freq = self.UNDEFINED
                self.__SB_dcyc = self.UNDEFINED

                # Variables used by GUI controls to pass 
                self.__DIR_var = self.INPUT
                self.__OH_var = self.LOW        # Initialize variable that will contain variable for output high status
                self.__PWM_var = self.PWM_OFF
                self.__FREQ_var = 0
                self.__DCYC_var = 0
                self.__EDGE_var = 0
                self.__BOUNCE_var = 0

                # Reset output
                
                self.set_direction(self.OUTPUT_TXT) #self.OUTPUT) # Initialize direction to output
                self.set_output(False)          # Set output to False (low) - Needed because of 'sticky' behavior of RPi
                self.set_direction(self.INPUT_TXT) #self.INPUT)  # Set direction to input

                GPIO.setwarnings(False)

        # --------------
        # Method to return pin id
        # --------------
        def get_id(self):
                return self.__id

        # --------------
        # Method to get current direction of pin
        # --------------
        def get_direction(self):
                return self.__direction

        # --------------
        # Method to return status (high/low)
        # --------------
        def get_status(self):
                return (self.__status)

        # --------------
        # Method to return pwm object
        # --------------
        def get_pwm(self):
                return (self.__pwm)

        # --------------
        # Method to return state of event detection
        # --------------

        def get_event_det(self):
                return self.__event_det

        # --------------
        # Method to add event detection for a pin
        # --------------
        def set_eventDet(self, edge):
                if (self.__id != 19) and (self.__id != 21) :  # pin 19 and 21 seem to constantly switch state
                        GPIO.add_event_detect(self.__id,GPIO.BOTH,callback=self.callback_pin_state_change,bouncetime=200)
                        self.__event_det = 1
        # --------------
        # Method to set direction (input or output) of pin
        # --------------
        def set_direction(self,dir):
                print("In set_direction")
                if dir == self.INPUT_TXT: #self.INPUT:          # If input
                        self.__direction = dir                  # Set __direction variable
                        GPIO.setup(self.__id,GPIO.IN)           # Set pin for input
                        if self.__OH_cBox != self.UNDEFINED:    # If gui chkbox exists, disable chkbox
                                self.__OH_cBox.config(state="disabled")
                        self.set_eventDet(GPIO.BOTH)
                elif dir == self.OUTPUT_TXT: #self.OUTPUT:      # if output
                        self.__direction = dir #dir             # Set __direction variable
                        try:
                                if self.__event_det == 1:
                                        self.__event_det = 0
                                        GPIO.remove_event_detect(self.__id)        
                        except Exception as err:
                                print("***",end=" ")
                                print(err)
                        GPIO.setup(self.__id,GPIO.OUT)          # Set pin for output
                        if self.__OH_cBox !=self.UNDEFINED:     # If gui chkbox exists... 
                                self.__OH_cBox.config(state="normal") #  enable chkbox
                else:
                        print("Error ...shold not get here.")


        # --------------
        # Method to set tkinter variable associated with direction radio buttons
        # --------------
        def set_DIR_var(self,var):
                self.__DIR_var = var

        def get_DIR_var(self):
                return self.__DIR_var

        # --------------
        # Method to set tkinter variable associated with output high chkbox
        # --------------
        def set_OUT_var(self,var):
                self.__OH_var = var

        def get_OUT_var(self):
                return self.__OH_var
        
        # --------------
        # Method to set tkinter variable associated with PWM high chkbox
        # --------------
        def set_PWM_var(self,var):
                self.__PWM_var = var

        def get_PWM_var(self):
                return self.__PWM_var
        # --------------
        # Method to set tkinter variable associated with Frequency spinbox
        # --------------
        def set_FREQ_var(self,var):
                self.__FREQ_var = var

        def get_FREQ_var(self):
                return self.__FREQ_var
                
        # --------------
        # Method to set tkinter variable associated with DutyCycle spinbox
        # --------------
        def set_DCYC_var(self,var):
                self.__DCYC_var = var

        def get_DCYC_var(self):
                return self.__DCYC_var

        # --------------
        # Method to set tkinter variable associated with edge widget
        # --------------
        def set_EDGE_var(self,var):
                self.__EDGE_var = var

        def get_EDGE_var(self):
                return self.__EDGE_var
        

        # --------------
        # Method to set tkinter variable associated with bounce widget
        # --------------
        def set_BOUNCE_var(self,var):
                self.__BOUNCE_var = var

        def get_BOUNCE_var(self):
                return self.__BOUNCE_var

        # --------------
        # Method to set output pin to high or low
        # --------------
        def set_output(self,val):              # Pass boolean vaue to indicate whether to turn on (True) or off (False)
                if self.get_direction()=="OUT": #self.OUTPUT:   # Only if pin is configured for output
                        self.__status = val             # Set status to val
                        GPIO.output(self.__id,val)      # Set pin to high/low
                else:
                        print("PIN is not set for output")

        # --------------
        # Method to self describe instanxce info...called by print function
        # --------------
        def __str__(self):
                return "PIN ID: " + str(self.__id) + "\tDirection: " + str(self.__direction) +  "\tStatus: " + str(self.__status)

        # --------------
        # Method to store references to GUI widgets
        # --------------
        def set_OH_CBX(self,widget):
                self.__OH_cBox = widget

        def set_OM_dir(self,widget):
                self.__OM_DIR = widget
                
        def set_PWM_CBX(self,widget):
                self.__PWM_cBox = widget

        def set_SB_FREQ(self,widget):
                self.__SB_freq = widget

        def set_SB_DCYC(self,widget):
                self.__SB_dcyc = widget

        def set_OM_EDGE(self,widget):
                self.__OM_edge = widget

        def set_OM_BOUNCE(self,widget):
                self.__OM_bounce = widget
                
        # --------------
        # Method called when a direction oMenu option is selected
        # --------------
        def dir_selected(self,dir):
                selected_mode = dir # self.__DIR_var.get()
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
                if GPIO.input(self.__id)==self.HIGH:
                        print("Pin",self.__id," is HIGH")
                        
                        #self.__RB_inp.configure(fg='red')
                else:
                        #self.__RB_inp.configure(fg='black')
                        print("Pin",self.__id," is LOW")
                
 
# End of PIN class
