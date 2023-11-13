import os
import csv

#Define csv file path
pybankcsv = os.path.join('Resources','budget_data.csv')

#Initialize variables
profit_loss = 0
total_months = 0
net_total_amount = 0
previous = 0
changes=[]
dates=[]
average_of_changes = 0
greatest_increase_amount = 0
greatest_decrease_amount = 0

#Read the csv file
with open(pybankcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the csv header
    csv_header = next(csvreader)

    #Iterate through all the rows in the csv file
    for row in csvreader:
        date = row[0]
        #Calculate Total Months
        total_months += 1
    
        profit_loss = int(row[1])

        #Calculate net total amount of Profit/Losses
        net_total_amount += profit_loss

        #Change in profit/loss each time
        if total_months > 1:
            change = profit_loss - previous
            changes.append(change)
            dates.append(date)

        previous = profit_loss

    #Average change
    average_of_changes = sum(changes) / len(changes)

    #Greatest increase in profits (Date and Amount)
    greatest_increase_amount = max(changes)
    increase_date_index = changes.index(greatest_increase_amount)
    greatest_increase_date = dates[increase_date_index]

    #Greatest decrease in profits (Date and Amount)
    greatest_decrease_amount = min(changes)
    decrease_date_index = changes.index(greatest_decrease_amount)
    greatest_decrease_date = dates[decrease_date_index]

    #Display results in the terminal
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_total_amount}')
    print(f'Average Change: $ {round(average_of_changes,2)}')
    print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})')

    #Export a text file with the results
    output_file = os.path.join('analysis','financial_anaysis.txt')
    with open(output_file, 'w') as textfile:
        textfile.write('Financial Analysis\n')
        textfile.write('----------------------------\n')
        textfile.write(f'Total Months: {total_months}\n')
        textfile.write(f'Total: ${net_total_amount}\n')
        textfile.write(f'Average Change: $ {round(average_of_changes,2)}\n')
        textfile.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n')
        textfile.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n')
