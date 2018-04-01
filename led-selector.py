import tkinter
import RPi.GPIO as GPIO
import LED_class


BCM_LED8 = 5    # Output GPIO for LED8
BCM_LED4 = 6    # Output GPIO for LED4
BCM_LED2 = 13   # Output GPIO for LED2
BCM_LED1 = 19   # Output GPIO for LED1

def showChoice():
    print("Button: ",v.get())
    led = v.get()
    if led == 1:
        led1.set_on()
        led2.set_off()
        led4.set_off()
        led8.set_off()
    elif led == 2:
        led1.set_off()
        led2.set_on()
        led4.set_off()
        led8.set_off()
    elif led == 4:
        led1.set_off()
        led2.set_off()
        led4.set_on()
        led8.set_off()
    elif led == 8:
        led1.set_off()
        led2.set_off()
        led4.set_off()
        led8.set_on()
    else:
        pass
        

GPIO.setmode(GPIO.BCM)
led1 = LED_class.LED(BCM_LED1)      # Create LED objects (and initialize)
led2 = LED_class.LED(BCM_LED2)
led4 = LED_class.LED(BCM_LED4)
led8 = LED_class.LED(BCM_LED8)  

root = tkinter.Tk()
root.title("LED Selector")


v = tkinter.IntVar()
v.set(0)

prompt = tkinter.Label(text="Select LED",fg="blue")

rb8 = tkinter.Radiobutton(text="LED8",value=8,variable = v,command=showChoice)
rb4 = tkinter.Radiobutton(text="LED4",value=4,variable = v,command=showChoice)
rb2 = tkinter.Radiobutton(text="LED2",value=2,variable = v,command=showChoice)
rb1 = tkinter.Radiobutton(text="LED1",value=1,variable = v,command=showChoice)

prompt.pack()
rb1.pack()
rb2.pack()
rb4.pack()
rb8.pack()

root.mainloop()

print("Cleaning up GPIO.")      
GPIO.cleanup()                  # Reset GPIO


