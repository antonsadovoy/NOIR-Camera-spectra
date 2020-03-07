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


# for name in sorted(filelist):
#     print(name)
#     filepath = os.path.join(cdd, name)
#     print(filepath)



