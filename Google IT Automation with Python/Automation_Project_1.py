#!/usr/bin/env python3
# calling pillow module for image
from PIL import Image
# module glob is to retrieve pathways/filenames
import glob
# The glob. glob returns the list of files with their full path (unlike os. listdir()) and is more powerful than os.
# In addition, glob contains the os, sys and re modules.
# Iterate through each file in the folder
''' For each file:
Rotate the image 90° clockwise
Resize the image from 192x192 to 128x128
Save the image to a new folder in .jpeg format 
'''
for img in glob.glob('*'):
    if img.endswith(".py"): continue
    # this has to be done in order to convert extension to jpg.
    im = Image.open(img).convert('RGB')
    # make sure to save it in images folder
    new_im = im.rotate(270).resize((128,128)).save("/opt/icons/" + str(img) + ".jpg")

