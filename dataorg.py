#!~/MySoft/.virtualenvs/mlenv/bin
#!~/.virtualenvs/mlenv/bin
# Author: Anton Sadovoy
# This module work with data files.

import numpy as np
import os


def FileNameList (DirPath, Mask):
# Get files from a folder with specific mask '.asc'
    FinalNameList = []
    NameList = os.listdir(DirPath)
    for name in NameList:
        if name.find(Mask) != -1: 
            FinalNameList.append(name)
    return FinalNameList