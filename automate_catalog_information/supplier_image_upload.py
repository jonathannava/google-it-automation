#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"

path = 'images/'

images = [file for file in os.listdir(path) if file.endswith(('jpeg'))]

for image in images:
    with open(path+image, 'rb') as upload_img:
        res = requests.post(url, files={'file': upload_img})

