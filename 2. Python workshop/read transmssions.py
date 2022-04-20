import csv
from pprint import pprint

transmissions = [0]
with open('transmissions.csv') as csvfile:
    csvreader = csv.reader(csvfile, quotechar='|')
    for line in csvreader:
        transmissions.append(line)
pprint(transmissions)

with open('transmissionseggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])