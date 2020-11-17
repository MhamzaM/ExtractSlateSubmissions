#!/usr/bin/env python

__author__ = "Muhammad Hamza"
__copyright__ = "Copyright 2020, Muhammad Hamza"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Muhammad Hamza"
__email__ = "m.hamza@nu.edu.pk"
__status__ = "Production"


"""
1. Place the script in the directory containing students submission directory (most probably it will be the downloads directory)
2. To run use the following commands in the terminal (assuming submission directory is in downloads)
    #cd Downloads
    #python3 ExtractSubmissions.py "Directory_Name"
3. The script will make another directory using the folder name and suffix "Scrapped" in the current directory
    containing directory for each students and their submissions
4. The script take cares for submissions made using .zip files and .txt files
5. The script is written on the basis of personal requirements so you may need some little tweaks to get on the road
6. For now it works well for python programming assignments
7. The code is not documented (sorry for that) due to lack of time.
8. Exceptions may occur, you are requested to report  them on my email :)
"""

import os,sys
from shutil import copy
import zipfile
from pathlib import Path


print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

directoryName = sys.argv[1]

if sys.argv[1].endswith(".zip"):
    with zipfile.ZipFile(os.path.realpath(sys.argv[1]), 'r') as zip_ref:
                    directoryName = zip_ref.namelist()[0]
                    directoryName = directoryName.split("/")[0]
                    zip_ref.extractall(os.getcwd())

destination = os.getcwd() +"/"+ directoryName+" scrapped"
print(destination)

try:
    os.mkdir(destination)
except OSError as err:
   print(err)

f = open("notFoundFiles","w")


studentDirs = os.listdir(os.getcwd() +"/"+ directoryName)

for i in studentDirs:
    try:
        os.mkdir(os.path.join(destination,i))
    except OSError as err:
        print(err)
   


for root, dirs, files in os.walk(directoryName):

    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            parent = root.split('/')
            copy(path, os.path.join(destination,parent[1]))
        
        elif file.endswith(".txt"):
            path = os.path.join(root, file)
            parent = root.split('/')
            parent = os.path.join(destination,parent[1])
            fileName = file.split(".")
            if fileName[0] != "timestamp":    
                fileName = fileName[0]+".py"       
                copy(path, os.path.join(parent,fileName))
            
        elif file.endswith(".zip"):
            path = os.path.join(root, file)
            parent = root.split('/')
            parent = os.path.join(destination,parent[1])
            
            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall(parent)
            for r, d, subfiles in os.walk(parent):
                for subfile in subfiles:
             
                    if subfile.endswith(".txt"):
                        fileName = subfile.split(".")
                        fileName = fileName[0]+".py"
                        os.rename(os.path.join(r,subfile),os.path.join(r,fileName))
                    
        else:
            pass
            f.write(root+"\n")
            

            

print("Task Completed")
f.close()
