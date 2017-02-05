"""
    - Motion detect
    - Start camera and roll for 10 seconds
    - Store footage according to date
    - Delete old data on startup
"""
import time
import datetime
import subprocess
import os
import RPi.GPIO as GPIO

from picamera import PiCamera
from time import sleep

camera = PiCamera()

"""Datetime"""
def getTime():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

"""Camera"""
def capture():
    camera.start_recording("/home/pi/spibox/capture/video/" + getTime() + ".h264")
    sleep(7)
    camera.stop_recording()

PIR = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN, GPIO.PUD_DOWN)

try:
    print "Turning on motion sensor..."
 
    # Loop until PIR indicates nothing is happening
    while GPIO.input(PIR)==1:
        Current_State  = 0
 
    print "  Sensor ready"
 
    while True:
        print('Waiting for movement')
        GPIO.wait_for_edge(PIR,GPIO.RISING)
        capture()

        
