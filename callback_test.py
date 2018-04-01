import RPi.GPIO as GPIO


def gpio_callback(channel):
    print("Call back channel", channel)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.IN)

#GPIO.add_event_detect(15,GPIO.FALLING,callback=gpio_callback)


cont = True
while cont:
    #if GPIO.event_detected(15):
    print("Starting wait")
    GPIO.wait_for_edge(15,GPIO.BOTH)
    print("Post wait")
        
        

        
