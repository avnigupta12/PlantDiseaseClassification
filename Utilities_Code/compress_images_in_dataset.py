import os
import sys
from PIL import Image
  

def compress_file(fileNameWithPath):      
    picture = Image.open(fileNameWithPath)
    l = picture.size[0]
    b = picture.size[1]
    # picture = picture.resize((int(l/4),int(b/4)),Image.ANTIALIAS)
    print(picture.mode)
    if picture.mode in ('RGBA', 'LA') or (picture.mode == 'P' and 'transparency' in picture.info):
        picture = picture.convert('RGB')
    picture.save(fileNameWithPath, "JPEG", optimize = True, quality = 70)

# compress_file('./testscompress/apricot_d003.JPG')
root = 'D:\Concordia Study-Anant\COMP 6721-Capstone\Datasets\PlantDoc-Dataset'
pattern = "*.JPG"
from fnmatch import fnmatch

for path, subdirs, files in os.walk(root):
    for name in files:
        print(name)
        if fnmatch(name, pattern):
            fileNameWithPath = os.path.join(path, name)
            compress_file(fileNameWithPath)