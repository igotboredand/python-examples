#!/usr/bin/python3

import json

# Open the file in read mode, load the file.
with open("example.json", "r") as read_file:
    data = json.load(read_file)
    
# data is now a 'dict', and can be referenced by refering to the data by name
print(data['researcher']['name'])