# Test program for using PWM to modify Frequency and DutyCycle to see
# effect on LED.

import RPi.GPIO as GPIO     # Import RPi.GPIO module as GPIO
import time

GPIO.setmode(GPIO.BCM)      # Initialize mode to use BCM numbering

OUTPORT = 5                 # Port to use for test
GPIO.setup(OUTPORT,GPIO.OUT) # Configure pin for output
dc = 0                      # Initial value of duty cycle
freq = 50                   # Initial value of frequency
try:
    p = GPIO.PWM(OUTPORT,freq)    # Initialize PWM at a frequency of 50
    p.start(dc)                  # Start with DutyCycle of 0


    cont = True
    while cont:
        print("Current settings: DC = ", dc,"Frequency = ",freq)
        print("Change:\n d - Dutycycle\n f - Fade\n q - FreQ\n x - eXit:\n ==> ", end='')
        opt = input().lower()   # Convert input to lower case
        if opt=='d':            # Change duty cycle
            dc = int(input("Enter DC value(0-100): "))
            p.ChangeDutyCycle(dc)
        elif opt=='f':          # Change duty cycle with fade
            newdc = int(input("Enter DC value(0-100): "))
            inc = int(input("Enter increment: "))
            step_delay = int(input("Enter delay between steps(ms): "))
        
            if newdc > dc:
                while dc < newdc:
                    time.sleep(step_delay/1000)
                    dc += inc
                    dc = min(dc,100)
                    p.ChangeDutyCycle(dc)
                    print(dc, newdc)
            else:
                while dc > newdc:
                    time.sleep(step_delay/1000)
                    dc -= inc
                    dc = max(dc,0)
                    p.ChangeDutyCycle(dc)
                    print(dc, newdc)            
        elif opt=='q':
            freq = int(input("Enter frequency value: "))
            p.ChangeFrequency(freq)
        elif opt =='x':
            cont = False
        else:
            print("Invalid input, try again")
except ValueError:
    print("Invalid input...exiting")
except KeyboardInterrupt:
    print("Ctl-C entered")

finally:
    p.stop()
    GPIO.cleanup()
    print("Exiting")
