# Test program for using PWM to modify Frequency and DutyCycle to see
# effect on LED.

import RPi.GPIO as GPIO     # Import RPi.GPIO module as GPIO

GPIO.setmode(GPIO.BCM)      # Initialize mode to use BCM numbering

OUTPORT = 5                 # Port to use for test
GPIO.setup(OUTPORT,GPIO.OUT) # Configure pin for output

try:
    p = GPIO.PWM(OUTPORT,50)    # Initialize PWM at a frequency of 50
    p.start(0)                  # Start with DutyCycle of 0


    cont = True
    while cont:
        print("Change DC(d) or Freq(f) or Quit(q): ", end='')
        opt = input()
        if opt=='d':
            dc = int(input("Enter DC value(0-100): "))
            p.ChangeDutyCycle(dc)
        elif opt=='f':
            freq = int(input("Enter frequency value: "))
            p.ChangeFrequency(freq)
        elif opt =='q':
            cont = False
        else:
            print("Invalid input, try again")

finally:
    p.stop()
    GPIO.cleanup()
    print("Exiting")
