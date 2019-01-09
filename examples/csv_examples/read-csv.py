#!/usr/bin/python3

import csv

# Open file, for each row print the row. 
with open('example.csv') as csvData:
    csvReader = csv.reader(csvData)
    for row in csvReader:
        print(row)