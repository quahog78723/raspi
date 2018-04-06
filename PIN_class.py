# The PIN class provides a simple way to interface with individual GPIO PINs and will maintain
# various attributes associated with the PIN.

#import RPi.GPIO as GPIO					# Use RPi.GPIO module and reference as GPIO

class PIN:								# Define PIN class	
	UNDEFINED 	= 0
	INPUT		= 1
	OUTPUT		= 2
	LOW		= 1
	HIGH		= 2
	
	
	
	def __init__(self,pin):         	# Instance constructor, takes a PIN ID as a parameter
                self.UNDEFINED  = 0
                self.INPUT      = 1
                self.OUTPUT     = 2
                self.LOW        = 1
                self.HIGH       = 2
                self.__id 	= str(pin)
                self.__mode     = self.UNDEFINED
                self.__status	= self.UNDEFINED
                self.__gui_obj  = ""

	def setup(self,mode):
		self.__mode = mode
		if mode == self.INPUT:
                    pass
		    #GPIO.setup(self.port,GPIO.IN)
		elif mode == self.OUTPUT:
                    pass
		    #GPIO.setup(self.port,GPIO.OUT)
	
	def set(self,on_off):		# Pass boolean vaue to indicate whether to turn on (True) or off (False)
		self.__status = on_off	
		#GPIO.output(self.port,on_off)

	def __str__(self):
		if self.__gui_obj=="":
			gui_txt = "{null}"
		else:
			gui_txt = str(self.__gui.obj)
		return "PIN ID: " + str(self.__id) + "\tMode: " + str(self.__mode) +  "\tStatus: " + str(self.__status) +"\tGUI Obj: " + gui_txt

	def set_rb1(self,rb):
		self.__rb1 = rb
		
	def set_rb2(self,rb):
		self.__rb2 = rb
		
	def set_var(self,var):
		self.__var = var

	def get_port(self):
		return (self.__id)

	def get_mode(self):
		return (self.__mode)

	def get_status(self):
		returrn (self.__status)

	def get_gui_obj(self):
		return (self.__gui_obj)

	def pin_selected(self):
		selected_mode = self.__var.get()
		if selected_mode == self.get_mode():
			print("Button already selected")
		else:
			self.setup(selected_mode)
			if selected_mode == self.UNDEFINED:
				sel_text = "RESET"
			elif selected_mode == self.INPUT:
				sel_text = "INPUT"
			elif selected_mode == self.OUTPUT:
				sel_text = "OUTPUT"
			else:
				print("Invalid ... selected mode = ",selected_mode)
			print(" Pin: ",self.get_port(),"set to", sel_text)
# End of PIN class
