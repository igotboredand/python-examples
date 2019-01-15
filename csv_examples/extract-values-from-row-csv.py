#!/usr/bin/python3

import csv

# Declare arrays used in the for loop
dates = []
scores = []

# Open file, for each row print the row. 
with open('example.csv') as csvData:
    csvReader = csv.reader(csvData)
    for row in csvReader:
    	# Row contains an array of the values for each columnb in the row.
        dates.append(row[0])
        scores.append(row[1])

# Do what you with with dates / scores here. 
# Positiion in the array corresponds to each row.
# dates[1] corresponds with scores [1]
print(dates)
print(scores)