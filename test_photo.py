from gpiozero import LightSensor
import RPi.GPIO as GPIO
import time 

ldr = LightSensor(18)
GREEN_LED = 8


GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_LED, GPIO.OUT)

try:
        GPIO.output(GREEN_LED, GPIO.HIGH)

        queue = []
        i = 0

        while True:

            if ldr.value > 0:
                queue.append(True)

            else:
                queue.append(False)

            if len(queue) > 50:
                queue.pop(0)


            if (queue.count(False) != len(queue) and queue) and (queue.count(True) != len(queue) and queue):
                print(i)
                i += 1

        
            

finally:
    GPIO.cleanup()
    pass
