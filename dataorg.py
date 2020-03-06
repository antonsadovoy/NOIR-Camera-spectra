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

def rename(workingdir,namelist, length, position, insert):
#This module rename files
    for name in sorted(filelist):
        if (len(name)<length):
            oldname = os.path.join(workingdir, name)
            newname = os.path.join(workingdir, name[:position]+insert+name[position:])
            os.rename(oldname,newname)
    return 0