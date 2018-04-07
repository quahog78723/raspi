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

                self.__id = pin                 # Set ID to pin number
                self.__direction = self.INPUT   # set default direction
                self.__OH_var = self.LOW        # Initialize variable that will contain variable for output high status
                self.__status = self.UNDEFINED  # Variable indicating high/low pin status
                self.__OH_cBox = self.UNDEFINED # Variable will contain referenece to gui checkbox object 
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
                elif dir == self.OUTPUT:        # if output
                        self.__direction = dir  # Set __direction variable
                        GPIO.setup(self.__id,GPIO.OUT)  # Set pin for output
                        if self.__OH_cBox !=self.UNDEFINED:     # If gui chkbox exists, enable chkbox
                                self.__OH_cBox.config(state="normal")
                else:
                        print("Error ...shold not get here.")

        # --------------
        # Method to set tkinter variable associated with direction radio buttons
        # --------------
        def set_dir_var(self,var):
                self.__dir_var = var

        # --------------
        # Method to set tkinter variable associated with output high chkbox
        # --------------
        def set_OH_var(self,var):
                self.__OH_var = var

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
        def set_OH_cBox(self,cBox):
                self.__OH_cBox = cBox

        # --------------
        # Method called when a direction radio button is clicked
        # --------------
        def pin_selected(self):
                selected_mode = self.__dir_var.get()
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

# End of PIN class
