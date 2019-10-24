import os, sys
from random import shuffle
from shutil import copyfile

files = os.listdir()
files.remove("RenameFiles.py")
files.remove("PrintNames.py")
for file in files:
	print(file)