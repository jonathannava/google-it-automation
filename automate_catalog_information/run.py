#!/usr/bin/env python3

import requests
import os
import json

url = "http://localhost/upload/"

images_path = 'images/'
descriptions_path = 'descriptions/'

descriptions = os.listdir(descriptions_path)

images = [file for file in os.listdir(images_path) if file.endswith(('jpeg'))]
#print(images)
#print(descriptions)

for file in descriptions:
    with open(descriptions_path + file, 'r') as f:
        line = f.readlines()
        




#print(type(descriptions))

#json_object = json.dumps(descriptions)

#print(type(json_object))
#print((json_object))

#TODO:Write a Python script named run.py to process the text files (001.txt, 003.txt ...) from the supplier-data/descriptions directory. The script should turn the data into a JSON dictionary by adding all the required fields


# for image in images:
#     with open(path+image, 'rb') as upload_img:
#         res = requests.post(url, files={'file': upload_img})

