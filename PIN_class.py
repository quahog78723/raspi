# The PIN class provides a simple way to interface with individual GPIO PINs and will maintain
# various attributes associated with the PIN.

import RPi.GPIO as GPIO                                        # Use RPi.GPIO module and reference as GPIO

class PIN:                                                              # Define PIN class

        def __init__(self,pin):
                self.UNDEFINED = -1
                self.INPUT = 1
                self.OUTPUT = 0
                self.LOW = 0
                self.HIGH = 1

                self.__id = pin
                self.__direction = self.INPUT
                self.__OH_var = self.LOW
                self.__status = self.UNDEFINED
                self.__OH_cBox = self.UNDEFINED
                self.set_direction(self.OUTPUT)
                self.set_output(False)
                self.set_direction(self.INPUT)
                
        def get_id(self):
                return (self.__id)

        def set_direction(self,dir):
                if dir == self.INPUT:
                        self.__direction = dir
                        GPIO.setup(self.__id,GPIO.IN)
                        if self.__OH_cBox !=self.UNDEFINED:
                                self.__OH_cBox.config(state="disabled")
                elif dir == self.OUTPUT:
                        self.__direction = dir
                        GPIO.setup(self.__id,GPIO.OUT)
                        if self.__OH_cBox !=self.UNDEFINED:
                                self.__OH_cBox.config(state="normal")
                else:
                        print("Error ...shold not get here.")

        def get_direction(self):
                return (self.__direction)


        def set_dir_var(self,var):
                self.__dir_var = var

        def set_OH_var(self,var):
                self.__OH_var = var

        def set_output(self,val):              # Pass boolean vaue to indicate whether to turn on (True) or off (False)
                if self.get_direction()==self.OUTPUT:
                        self.__status = val
                        GPIO.output(self.__id,val)
                else:
                        print("PIN is not set for output")

        def __str__(self):
                return "PIN ID: " + str(self.__id) + "\tDirection: " + str(self.__direction) +  "\tStatus: " + str(self.__status)

        

        def get_status(self):
                return (self.__status)

        def set_OH_cBox(self,var):
                self.__OH_cBox = var

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

        def out_high_selected(self):
                if self.__OH_var.get() == self.HIGH:
                        print(" Pin: ",self.get_id(),"set HIGH")
                else:
                        print(" Pin: ",self.get_id(),"set LOW")
                self.set_output(self.__OH_var.get())

# End of PIN class
