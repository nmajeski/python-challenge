import os
import csv

csvpath = os.path.join('election_data.csv')

total_votes = 0
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1

print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
    