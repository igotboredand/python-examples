import csv
 
def readCSV(filename):
    dates = []
    scores = []
 
    with open(filename) as csvData:
        csvReader = csv.reader(csvData)
        for row in csvReader:
            dates.append(row[0])
            scores.append(row[1])
 
    return dates, scores
 
 
dates,scores = readCSV('example.csv')
 
print(dates)
print(scores)