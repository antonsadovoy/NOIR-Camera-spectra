#!~/.virtualenv/project01/bin/python
# Author: Anton Sadovoy

import os
import dataorg as do

cwd = os.getcwd()
cdd = os.path.join(cwd,'raspicamv2_cal')
filemask = '.jpg'

filelist = do.FileNameList(cdd, filemask)

for name in sorted(filelist):
    print(name)
    filepath = os.path.join(cdd, name)
    with open(filepath) as file:
        


