# Author: Anton Sadovoy

# import the necessary packages
from picamera import PiCamera
from  time import time, ctime, sleep
import os

# Set working directories
cwd = os.getcwd()
cdd = os.path.join(cwd,'data')

# Create/open a log file
log = open(os.path.join(cdd, 'log.txt'), 'a+')

# Create a new image file name
timestamp = time()
filename = str(timestamp) + '.jpg'
filepath = os.path.join(cdd, filename)

camera = PiCamera()
camera.start_preview()

# Camera warm-up time
sleep(2)
camera.capture(filepath)

# Record log
log.write('{} - {}\n'.format(ctime(timestamp), filename))


