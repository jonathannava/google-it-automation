#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"

images_path = 'images/'
descriptions_path = 'descriptions/'

descriptions = os.listdir(descriptions_path)

images = [file for file in os.listdir(images_path) if file.endswith(('jpeg'))]
print(images)
print(descriptions)


#for image in images:
    #print(images)
    

# for image in images:
#     with open(path+image, 'rb') as upload_img:
#         res = requests.post(url, files={'file': upload_img})

