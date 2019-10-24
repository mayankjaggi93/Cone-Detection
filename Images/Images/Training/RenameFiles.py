import os, sys
import random 
from shutil import copyfile

files = os.listdir()
files.remove("RenameFiles.py")
files.remove("PrintNames.py")
print(files)

i = 0
for fileName in files: 
        newFileName = str(random.randint(0,90000) + 10000) + ".jpg"
        os.rename(fileName, newFileName) 
        i = i + 1