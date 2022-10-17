#! /usr/bin/env python3

import os
import requests

path_data = "/data/feedback/"
for file in  os.listdir(path_data):
    format = ["title","name","date","feedback"]
    feedback = {}
    with open(path_data + file) as text_file:
        count = 0
        for line in text_file:
            feedback[format[count]] = line.strip()
            count += 1
    res = requests.post("http://34.123.97.147/feedback/",
    json=feedback)
print("Feedback uploaded to Web Server")