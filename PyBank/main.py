import os
import csv

# initialize variables to be used in output
num_months = 0
profit_loss_total = 0
average_change = 0
greatest_increase_date = ''
greatest_increase_value = 0
greatest_decrease_date = ''
greatest_decrease_value = 0

# open CSV file in the same directory as code
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # store the CSV header
    csv_header = next(csvreader)
    
    for row in csvreader:
        my_date = row[0]
        # if there is a date in the new row, add 1 to num_months
        if (my_date):
            num_months = num_months + 1
        
        profit_loss = int(row[1])
        # if there is an int in the new row, add it to the total
        if (profit_loss):
            profit_loss_total = profit_loss_total + profit_loss

            # check if the current row could contain the greatest increase/decrease
            if (profit_loss > greatest_increase_value):
                greatest_increase_date = my_date
                greatest_increase_value = profit_loss
            elif (profit_loss < greatest_decrease_value):
                greatest_decrease_date = my_date
                greatest_decrease_value = profit_loss
        
    # calculate the average change if the num_months is > 0 to avoid divide by 0 error
    if (num_months > 0):
        average_change = round(profit_loss_total / num_months, 2)

# print the results
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {num_months}')
print(f'Total: ${profit_loss_total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})')

# write results out to output file
output_file = 'output.txt'

with open(output_file, 'w') as text:
    # add line break at the end of each line so that each write writes to a new line
    text.write('Financial Analysis\n')
    text.write('----------------------------\n')
    text.write(f'Total Months: {num_months}\n')
    text.write(f'Total: ${profit_loss_total}\n')
    text.write(f'Average Change: ${average_change}\n')
    text.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value})\n')
    text.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})')