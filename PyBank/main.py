import os
import csv

# Is it ok to get the file from the same directory that the python file is in?
csvpath = os.path.join('budget_data.csv')

num_months = 0
profit_loss_total = 0
greatest_increase_date = ''
greatest_increase_value = 0
greatest_decrease_date = ''
greatest_decrease_value = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    for row in csvreader:
        my_date = row[0]
        # Do we ever need to worry about duplicate or missing dates?
        if (my_date):
            num_months = num_months + 1
        
        # Do we ever need to worry about missing profit/loss?
        profit_loss = int(row[1])
        if (profit_loss):
            profit_loss_total = profit_loss_total + profit_loss

            if (profit_loss > greatest_increase_value):
                greatest_increase_date = my_date
                greatest_increase_value = profit_loss
            elif (profit_loss < greatest_decrease_value):
                greatest_decrease_date = my_date
                greatest_decrease_value = profit_loss
        
    if (num_months > 0):
        average_change = round(profit_loss_total / num_months, 2)
    else:
        average_change = 0

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {num_months}')
print(f'Total: ${profit_loss_total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})')

output_file = 'output.txt'

with open(output_file, 'w') as text:
    text.write('Financial Analysis\n')
    text.write('----------------------------\n')
    text.write(f'Total Months: {num_months}\n')
    text.write(f'Total: ${profit_loss_total}\n')
    text.write(f'Average Change: ${average_change}\n')
    text.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value})\n')
    text.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})')