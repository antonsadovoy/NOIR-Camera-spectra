# Author: Anton Sadovoy

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
from  time import time, ctime
import cv2
import os

# Set working directories
cwd = os.getcwd()
cdd = os.path.join(cwd,'data/bf filter')

# Create/open a log file
log = open(os.path.join(cdd, 'log.txt'), 'a+')

# Create a new image file name
timestamp = time()
filename = str(timestamp) + '.jpg'

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# allow the camera to warmup
time.sleep(0.1)

# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

# Save image
cv2.imwrite(filename,image)

# Record log
log.write('{} - {}\n'.format(ctime(timestamp), filename))


