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
                self.LOW = 0            # Pin low indicator
                self.HIGH = 1           # Pin high indicator
                self.PWM_ON = 1
                self.PWM_OFF = 0
                
                self.__id = pin                 # Set ID to pin number
                self.__direction = self.INPUT   # set default direction
                self.__status = self.UNDEFINED  # Variable indicating high/low pin status
                
                self.__DIR_var = self.INPUT
                self.__OH_var = self.LOW        # Initialize variable that will contain variable for output high status
                self.__PWM_var = self.PWM_OFF
                self.__FREQ_var = 0
                self.__DCYC_var = 0

                self.__RB_inp = self.UNDEFINED
                self.__RB_out = self.UNDEFINED
                self.__OH_cBox = self.UNDEFINED # Variable will contain referenece to gui checkbox object 
                self.__SB_freq = self.UNDEFINED
                self.__SB_dcyc = self.UNDEFINED
                
                self.__p = 0

                # Reset output
                
                self.set_direction(self.OUTPUT) # Initialize direction to output
                self.set_output(False)          # Set output to False (low) - Needed because of 'sticky' behavior of RPi
                self.set_direction(self.INPUT)  # Set direction to input

        # --------------
        # Method to return pin id
        # --------------
        def get_id(self):
                return self.__id

        # --------------
        # Method to get crrent direction of pin
        # --------------
        def get_direction(self):
                return self.__direction

        # --------------
        # Method to return status (high/low)
        # --------------
        def get_status(self):
                return (self.__status)

        # --------------
        # Method to set direction (input or output) of pin
        # --------------
        def set_direction(self,dir):
                if dir == self.INPUT:           # If input
                        self.__direction = dir  # Set __direction variable
                        GPIO.setup(self.__id,GPIO.IN) # Set pin for input
                        if self.__OH_cBox !=self.UNDEFINED: # If gui chkbox exists, disable chkbox
                                self.__OH_cBox.config(state="disabled")
                        if self.__id != 19:
                                GPIO.add_event_detect(self.__id,GPIO.BOTH,callback=self.callback_pin_state_change,bouncetime=200)
                elif dir == self.OUTPUT:        # if output
                        self.__direction = dir  # Set __direction variable
                        #GPIO.remove_event_detect(self.__id)
                        GPIO.setup(self.__id,GPIO.OUT)  # Set pin for output
                        if self.__OH_cBox !=self.UNDEFINED:     # If gui chkbox exists, enable chkbox
                                self.__OH_cBox.config(state="normal")
                else:
                        print("Error ...shold not get here.")

        # --------------
        # Method to set tkinter variable associated with direction radio buttons
        # --------------
        def set_DIR_var(self,var):
                self.__DIR_var = var

        # --------------
        # Method to set tkinter variable associated with output high chkbox
        # --------------
        def set_OUT_var(self,var):
                self.__OH_var = var

        # --------------
        # Method to set tkinter variable associated with PWM high chkbox
        # --------------
        def set_PWM_var(self,var):
                self.__PWM_var = var
        # --------------
        # Method to set tkinter variable associated with PWM high chkbox
        # --------------
        def set_FREQ_var(self,var):
                self.__FREQ_var = var
        # --------------
        # Method to set tkinter variable associated with PWM high chkbox
        # --------------
        def set_DCYC_var(self,var):
                self.__DCYC_var = var

        # --------------
        # Method to set output pin to high or low
        # --------------
        def set_output(self,val):              # Pass boolean vaue to indicate whether to turn on (True) or off (False)
                if self.get_direction()==self.OUTPUT:   # Only if pin is configured for output
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
        # Method to store reference to GUI checkBox
        # --------------
        def set_OH_CBX(self,cBox):
                self.__OH_cBox = cBox

        def set_INP_RB(self,rb):
                self.__RB_inp = rb

        def set_OUT_RB(self,rb):
                self.__RB_out = rb

        def set_PWM_CBX(self,cBox):
                self.__PWM_cBox = cBox                
        # --------------
        # Method called when a direction radio button is clicked
        # --------------
        def pin_selected(self):
                selected_mode = self.__DIR_var.get()
                if selected_mode == self.get_direction():
                        print("Button already selected")
                else:
                        self.set_direction(selected_mode)

                        if selected_mode == self.INPUT:
                                sel_text = "INPUT"
                        elif selected_mode == self.OUTPUT:
                                sel_text = "OUTPUT"
                        else:
                                print("Invalid ... selected direction = ",selected_mode)
                        print(" Pin: ",self.get_id(),"direction", sel_text)
        # --------------
        # Method called when the set high chkbox is clicked
        # --------------
        def out_high_selected(self):
                if self.__OH_var.get() == self.HIGH:
                        print(" Pin: ",self.get_id(),"set HIGH")
                else:
                        print(" Pin: ",self.get_id(),"set LOW")
                self.set_output(self.__OH_var.get())
        # --------------
        # Method called when the pwm chk box is clicked
        # --------------
        def pwm_selected(self):
                if self.__PWM_var.get() == self.PWM_ON:
                        print(" Pin: ",self.get_id(),"turn PWM on (not implement yet)")
                        if self.get_direction() == self.OUTPUT:
                                self.__p = GPIO.PWM(self.__id,2)
                                self.__p.start(50)
                else:
                        print(" Pin: ",self.get_id(),"turn PWM off (not implement yet)")
                        if self.__p != 0:
                                self.__p.stop()
                                self.__p = 0
                                        
                # !!!!!!!!!!!!!!!!!!!!!!
                # Need logic to set PWM
                # !!!!!!!!!!!!!!!!!!!!!!

        # --------------
        # Method called when the Freq SB is changed
        # --------------
        def freq_selected(self):
                print(" Pin: " , self.get_id() , "frequency changed to ",self.__FREQ_var.get())


        # --------------
        # Method called when the Freq SB is changed
        # --------------
        def dcyc_selected(self):
                print(" Pin: " , self.get_id(), "duty cycle changed to ",self.__DCYC_var.get())


                
        # --------------
        # Call back for input pin
        # --------------
        def callback_pin_state_change(self,channel):
                print(" Pin ",self.get_id(),"has changed")
                if GPIO.input(self.__id)==self.HIGH:
                        self.__RB_inp.configure(fg='red')
                else:
                        self.__RB_inp.configure(fg='black')
                        
                
 
# End of PIN class
