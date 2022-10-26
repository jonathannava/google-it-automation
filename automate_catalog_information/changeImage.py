#!/usr/bin/env python3
from PIL import Image
import os

images = [file for file in os.listdir('images') if file.endswith(('tiff'))]

for image in images:
    file_name = image.split('.')[0]
    img = Image.open('images/'+image).convert('RGB')
    img.resize((600,400)).save('images/{}.jpeg'.format(file_name))
  