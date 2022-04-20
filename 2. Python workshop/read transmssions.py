import csv

with open('transmissions.csv', 'r') as myfile:
    csvreader = csv.reader(myfile)
    for row in csvreader:
        print(row)