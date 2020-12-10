#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 19:23:33 2020

@author: patrickburke
"""

import os
os.chdir('/Users/patrickburke/documents/Learning-Content/Automate-Boring')

#os.path.abspath(path) will return a string of the absolute path of the argument.
#os.path.isabs(path) will return true if the argument is an abs path, false if relative
#os.path.relpath(path, start) will return a string of a relative path from start path to path

#os.path.exists(path) will return true if folder/file exists
#os.path.isfile(path) will return true if the path argument exists
#os.path.isdir(path) will return True if the path argument exists and is a folder and will return false otherwise

helloFile = open('/Users/patrickburke/Documents/Learning-Content/Automate-Boring/hello.txt')

helloContent = helloFile.read()

baconFile = open ('bacon.txt', 'w')
baconFile.write('Hello world!\n')
baconFile.close()
baconFile= open ('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()

baconFile.close()
print(content)

#Shelve Module

import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
type(shelfFile)
shelfFile.close()

import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

