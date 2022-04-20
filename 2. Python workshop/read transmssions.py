import csv
from pprint import pprint

transmissions = [0]
with open('transmissions.csv') as csvfile:
    csvreader = csv.reader(csvfile, quotechar='|')
    for line in csvreader:
        transmissions.append(line)
pprint(transmissions)