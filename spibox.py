import time
import datetime
import re

import subprocess
import os
import RPi.GPIO as GPIO

#Custom files
import absoluteTime

PIR = 4
"""Probably won't be used, delete later
def get_file_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
"""

#Search through photo/video archives and delete files past a certain date
#def walkThroughFiles():
    

#Takes photo
def photo():
    for i in range(1,2):
        capturename = str(absoluteTime.absoluteTime())
        print('Motion detected! Taking snapshot')
        cmd="raspistill -w 640 -h 480 -n -t 10 -q 10 -e jpg -th none -o /home/pi/spibox/capture/photos/alert" + capturename
        camerapid = subprocess.call(cmd,shell=True)

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
        photo()

except KeyboardInterrupt:
  print "  Bye for now"
  # Reset GPIO
  GPIO.cleanup()
