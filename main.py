# * Your task is to create a Python script that analyzes the records to calculate each of the following:
#   * The total number of months included in the dataset 
#   * The net total amount of "Profit/Losses" over the entire period 
#   * The average of the changes in "Profit/Losses" over the entire period 
#   * The greatest increase in profits (date and amount) over the entire period 
#   * The greatest decrease in losses (date and amount) over the entire period 

import os
import csv
csvpath = "./PyBank/Resources/budget_data.csv"

with open(csvpath, newline='') as statement:
    csvreader = csv.reader(statement, delimiter = ",")
    csvheader = next(csvreader)
    data = list(csvreader)

clean_profits = [int(row[1]) for row in data]
months = len(clean_profits)    
changes = []
total = 0  
month_change = 0

## TOTAL OF PROFITS/LOSSES ENTIRE PERIOD 
for i in clean_profits:
    total += i

## CREATING LIST OF PROFITS & LOSSES PER MONTH 
for e, i in enumerate(clean_profits):
    if e >= 1:
        month_change = clean_profits[e] - clean_profits[e-1]
        changes.append(month_change)
avgchange =sum(changes)/len(changes)
maxchange = max(changes)
minchange = min(changes)

## FINDING INDEXES OF MAX AND MIN PROFITS/LOSSES
for e, i in enumerate(changes):
    if i == maxchange:
        max_index = e 
    if i == minchange:
        min_index = e
max_month = data[max_index + 1]
min_month = data[min_index + 1]

## WRITING RESULTS INTO NEW TEXT FILE
results = open("results.txt", "w+")
results.write("Financial Analysis" + "\n")
results.write("----------------------------" + "\n")
results.write("Total Months: " + str(months) + "\n")
results.write("Total: $" + str(total) + "\n")
results.write("Average Change: $" + str(avgchange) + "\n")
results.write("Greatest Increase In Profits: $" + str(max_month) + ", increase of $" + str(maxchange) + "\n")
results.write("Greatest Decrease In Profits: $" + str(min_month) + ", decrease of $" + str(minchange) + "\n")
results.close

## EXAMPLE FORMATING FOR FINAL EXPORT 
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)