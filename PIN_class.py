# The PIN class provides a simple way to interface with individual GPIO PINs and will maintain
# various attributes associated with the PIN.

#import RPi.GPIO as GPIO                                        # Use RPi.GPIO module and reference as GPIO

class PIN:                                                              # Define PIN class
        UNDEFINED       = -1
        INPUT           = 1
        OUTPUT          = 0
        LOW             = 0
        HIGH            = 1

        def __init__(self,pin):
		self.UNDEFINED = -1
		self.INPUT = 1
		self.OUTPUT = 0
		self.LOW = 0
		self.HIGH = 1
		self.__id = str(pin)
		self.__direction = self.UNDEFINED
		self.__status = self.UNDEFINED

	def set_direction(self,dir):
		if dir == self.INPUT:
			self.__direction = dir
			#GPIO.setup(self.port,GPIO.IN)
		elif dir == self.OUTPUT:
			self.__direction = dir
			#GPIO.setup(self.port,GPIO.OUT)
		else:
			print("Error ...shold not get here.")

        def set_output(self,b_on):              # Pass boolean vaue to indicate whether to turn on (True) or off (False)
                self.__status = b_on
                #GPIO.output(self.port,on_off)

        def __str__(self):
                return "PIN ID: " + str(self.__id) + "\tDirection: " + str(self.__direction) +  "\tStatus: " + str(self.__status)

        def set_var(self,var):
                self.__var = var

        def get_id(self):
                return (self.__id)

        def get_status(self):
                returrn (self.__status)

        def pin_selected(self):
                selected_mode = self.__var.get()
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
                        print(" Pin: ",self.get_id(),"set to", sel_text)
# End of PIN class
