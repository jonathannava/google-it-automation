#!/usr/bin/env python3
from PIL import Image
import os

images = [file for file in os.listdir() if file.startswith(('ic'))]

for image in images:
    file_name = image.split('.')[0]
    img = Image.open(image).convert('RGB')
    img.rotate(270).resize((128,128)).save('/opt/icons/{}.jpeg'.format(file_name))


