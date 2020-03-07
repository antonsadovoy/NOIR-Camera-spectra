#!~/.virtualenv/project01/bin/python
# Author: Anton Sadovoy

import os
import dataorg as do
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Set working directories
cwd = os.getcwd()
cdd = os.path.join(cwd,'data')
filemask = '.jpg'

# Set file names
filelist = do.FileNameList(cdd, filemask)
name = filelist[2]
print(name)

# Get information from filename. Example'pH(.+?).asc'
pattern = 'Ref_(.+?)nm.jpg' 
wavelength = do.getfromname(name, pattern)
print(wavelength)

filepath = os.path.join(cdd, name)

# Open image
image = cv.imread(filepath,1)

# Crop image
roi = image[730:960, 1000:1330]
# plt.imshow(roi, interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()

# Get mean of each channel (RGB)
mean_roi = np.mean(roi, axis=(0,1))
print(mean_roi)

wavelength=[]
red=[]
green=[]
blue=[]
# Move over all files
for name in sorted(filelist):
    filepath = os.path.join(cdd, name)
    image = cv.imread(filepath,1)
    roi = image[730:960, 1000:1330]
    [redmean, greenmean, bluemean] = np.mean(roi, axis=(0,1))
    red.append(redmean)
    green.append(greenmean)
    blue.append(bluemean)
    wavelength.append(do.getfromname(name, pattern))
    
 # Plot camera spectral response
plt.plot(wavelength, red, '-r', label='red channel')
plt.plot(wavelength, green, '-g', label='green channel')
plt.plot(wavelength, blue, '-b',label='blue channel')
plt.legend()
plt.show()



