import reports
import os 
import datetime



images_path = 'images/'
descriptions_path = 'descriptions/'

descriptions = os.listdir(descriptions_path)

data = []
report = []
for file in descriptions:
    with open(descriptions_path + file, 'r') as f:
        file_data = f.read()
        data.append(file_data.split('\n'))
        f.close()


    
