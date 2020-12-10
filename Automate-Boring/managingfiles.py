#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:53:28 2020

@author: patrickburke
"""

import shutil, os
os.chdir('/Users/patrickburke/documents/Learning-Content/Automate-Boring')

#os.unlink(path) will delete the file at path
#os.rmdir(path) will delete the folder at path
#shutil.rmtree(path) will remove the folder at path, all files and folders
#above irreplaceably deletes files and folders

import send2trash
baconFile = open('bacon.txt', 'a') #creates file
baconFile.write('Bacon is not a vegetable')
baconFile.close()

send2trash.send2trash(bacon.txt)
