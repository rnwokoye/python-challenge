## BudgetData Analysis
import os
import csv


csvpath = os.path.join('Resources', 'budget_data.csv')
csvwritepath = os.path.join('analysis', 'analysis_file.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    # We are able to read the header row: csvheader
    
    
    # Remove header row:
    csvheader = next(csvreader)
    
    # print header row
    # print(csvheader)
    

    # create array to hold count of months
    total_months = []
    total_profit_Or_Loss = []
    total_profits_only = []
    total_losses_only = []
    maxAmt = 0
    minAmt = 0
    max_date = ''
    min_date = ''
    
    
    # months == 1st item in each row
    # iterate over each row, and append count of months to array
    for row in csvreader:
        months = row[0]
        profit_loss = int(row[1])
        # print(months)
        total_months.append(months)
        total_profit_Or_Loss.append(profit_loss)
        
        if profit_loss < 0:
            total_losses_only.append(profit_loss)
        else:
            total_profits_only.append(profit_loss)
             
        
        if int(row[1]) > maxAmt:
            maxAmt = int(row[1])
            max_date = row[0]
            
        
        if int(row[1]) < minAmt:
            minAmt = int(row[1])
            min_date = row[0]
        
        
        
    
    # Print length of our months array
    print(f'Total months: {len(total_months)} months')
    
    # Print Net Total Amount
    print(f'Total: ${sum(total_profit_Or_Loss):,d}')
    
    
    # Print Greatest Increase
    print(f'Greatest increase in Profits: {max_date} (${maxAmt:,d})')
    
    # Print Greates Decrease in Profits
    print(f'Greatest Decrease in Profits: {min_date} (${minAmt:,d})')
    
    
    # Print Average Change
    average_change = round((maxAmt + minAmt)/ len(total_months), 2)
    print(f'Average Change: ${average_change}')


with open(csvwritepath, mode='w') as analysis_file:
    financials = csv.writer(analysis_file)
    financials.writerow(['Total Months: {} Months'.format(len(total_months))])
    financials.writerow(['Greatest increase in Profit: {} ({})'.format(max_date, maxAmt)])
    financials.writerow(['Greatest Decrease in Profits: {} ({})'.format(min_date, minAmt)]) 
    financials.writerow(['Average Change: ${}'.format(average_change)])
