import RPi.GPIO as GPIO
import LED_class

GPIO.setmode(GPIO.BCM)

led = LED_class.LED(5)

input()

led.set_on()

input()
led.set_off()

GPIO.cleanup()
