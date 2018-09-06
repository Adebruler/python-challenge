import os
import csv


with open('budget_data.csv', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    months = 1
    total = 0
    run_avg = 0

    # Read the header row first
    csv_header = next(csvreader)

    # initialize data with first month
    first_row = next(csvreader)
    last_month = int(first_row[1])
    most_profit = last_month
    least_profit = last_month
    when_most = first_row[0]
    when_least = when_most
    months = 1



    # Begin Calculations with the remaining data
    total = 0
    run_avg = 0
    total_delta = 0
    for row in csvreader:
        this_month = int(row[1])
        # Caluclate monthly change in profits
        total = total + this_month
        month_delta = this_month - last_month
        total_delta += month_delta
        last_month = this_month
        # check for superlatives
        if (month_delta > most_profit):
            most_profit = month_delta
            when_most = row[0]
        elif (month_delta < least_profit):
            least_profit = month_delta
            when_least = row[0]
        months+=1

delta_avg = total_delta/(months-1)
# Print data into text file
file=open('BankResults.txt',"w")
file.write("Financial Analysis")
file.write('\n'+"----------------------------")
file.write('\n'+f"Total Months: {months}")
file.write('\n'+f"Total: {total}")
file.write('\n'+f"Average Change: ${delta_avg:.2f}")
file.write('\n'+f"Greatest Increase in Profits: {when_most} (${most_profit})")
file.write('\n'+f"Greatest Decrease in Profits: {when_least} (${least_profit})")
# Print Text File into Terminal
file=open('BankResults.txt',"r")
print(file.read())
