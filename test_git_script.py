
import RPi.GPIO as GPIO
from threading import Timer
import time
import glob

last_sensor_event = 0
stop_timer_running = False

SENSOR_PIN = 18
GREEN_LED = 8

W = 1296
H = 972
FPS = 18

def start_recording():

	print('start')

def stop_recording():

	print('stop')


def timer_stop():
	global stop_timer_running
	stop_timer_running = False
	stop_recording()


def sensor_change(pin):
	global last_sensor_event
	global stop_timer
	global stop_timer_running

	now = time.time()

	if abs(last_sensor_event - now) > 0.5:
		start_recording()

	last_sensor_event = now

	if stop_timer_running:
		stop_timer.cancel()

	stop_timer = Timer(0.5, timer_stop)
	stop_timer.start()
	stop_timer_running = True


GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.add_event_detect(SENSOR_PIN, GPIO.BOTH, sensor_change)

# Make a file-like object out of the connection
try:

	while True:
		time.sleep(1)
	#camera.wait_recording(60)
finally:
	
	GPIO.cleanup()
	pass