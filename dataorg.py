#!~/MySoft/.virtualenvs/mlenv/bin
#!~/.virtualenvs/mlenv/bin
# Author: Anton Sadovoy
# This module work with data files.

import os


def FileNameList (DirPath, Mask):
# Get files from a folder with specific mask '.asc'
    FinalNameList = []
    NameList = os.listdir(DirPath)
    for name in NameList:
        if name.find(Mask) != -1: 
            FinalNameList.append(name)
    return FinalNameList

def rename(workingdir,namelist, num, insert):
#This module rename files
    for name in sorted(filelist):
        if (len(name)<14):
        oldname = os.path.join(workingdir, name)
        newname = os.path.join(workingdir, name[:num]+insert+name[num:])
        os.rename(oldname,newname)
    return 0