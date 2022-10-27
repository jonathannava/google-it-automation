#!/usr/bin/env python3

import requests
import os
import json

def upload(url,descriptions_path):
    images_path = 'images/'
    descriptions = os.listdir(descriptions_path)

    images = [file for file in os.listdir(images_path) if file.endswith(('jpeg'))]
    #print(images)
    #print(descriptions)
    data = {}
    for file in descriptions:
        with open(descriptions_path + file, 'r') as f:
            file_data = f.read()
            lines = file_data.split('\n')
            data["name"]=lines[0]
            data["weight"]=int(lines[1].strip('lbs'))
            data["description"]=lines[2]
            data["image_name"]=(file.strip('.txt'))+'.jpeg'
            try:
                res = requests.post(url, json=data)
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
            
        
if __name__=='__main__':
    url = 'http://localhost/fruits/'
    user = os.getenv('USER')
    descriptions_path = '/home/{}/supplier-data/descriptions/'.format(user)
    upload(url,descriptions_path)



