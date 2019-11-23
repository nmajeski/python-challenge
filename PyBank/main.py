import os
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    months = []
    for row in csvreader:
        my_date = row[0]
        if (my_date):
            months.append(my_date)

    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {len(months)}')
