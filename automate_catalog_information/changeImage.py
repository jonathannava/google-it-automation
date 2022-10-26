#!/usr/bin/env python3
from PIL import Image
import os
path = 'images/'
images = [file for file in os.listdir(path) if file.endswith(('tiff'))]

for image in images:
    file_name = image.split('.')[0]
    img = Image.open(path+image).convert('RGB')
    img.resize((600,400)).save(path+'{}.jpeg'.format(file_name))
  