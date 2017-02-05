from picamera import PiCamera
from time import sleep

import time
import datetime

camera = PiCamera()

"""Datetime"""
def getTime():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

camera.start_recording("/home/pi/spibox/capture/video/" + getTime() + ".h264")
sleep(3)
camera.stop_recording()
