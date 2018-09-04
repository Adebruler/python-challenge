import os
import csv


with open('budget_data.csv', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    months = 1
    total = 0
    run_avg = 0

    # Read the header row first (skip this step if there is now header)
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
    for row in csvreader:
        this_month = int(row[1])
        # Caluclate monthly change in profits
        total = total + this_month
        month_delta = this_month - last_month
        last_month = this_month
        # check for superlatives
        if (month_delta > most_profit):
            most_profit = month_delta
            when_most = row[0]
        elif (month_delta < least_profit):
            least_profit = month_delta
            when_least = row[0]
        # Use a weighted average to calculate average of monthly profit change
        run_avg=( (run_avg * (months-1) ) + month_delta) / months
        months+=1
        print(row)
print(months)
print(total)
print(run_avg)
print(when_most)
print(most_profit)
print(when_least)
print(least_profit)
