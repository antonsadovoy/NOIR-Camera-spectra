#!~/.virtualenv/project01/bin/python
# Author: Anton Sadovoy

import os
import dataorg as do

cwd = os.getcwd()
cdd = os.path.join(cwd,'raspicamv2_cal')
filemask = '.jpg'

filelist = do.FileNameList(cdd, filemask)

for name in sorted(filelist):
    if (len(name)<14):
        oldname = os.path.join(cdd, name)
        newname = os.path.join(cdd, name[:4]+'0'+name[4:])
        os.rename(oldname,newname)
    print(name, len(name))
