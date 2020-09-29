import os #Import os module 
import csv #Read CSV files

csv_path = os.path.join('Resources','budget_data.csv') # Set path for file 

#Open the file budget_data.csv
with open(csv_path) as budget_file:

    budgetreader = csv.reader(budget_file, delimiter = ',')
    
    #Skip reading the top row/header 
    budget_header = next(budgetreader)

    #Create empty lists to store data 
    month = [ ]
    profitloss = [ ] 

    for row in budgetreader:
        #Add the first column to the month list 
        month.append(row[0])
        #Count the number of months/rows
        month_count = len(month)
        #Add the second column to the profit/loss list 
        profitloss.append(int(row[1]))
        #Sum all the values in 2nd column to get total budget 
        total_budget = sum(profitloss)

    #Create new change list to hold differences in consecutive profit/loss values
    change = [ ] 

    #Since we are calculating the average difference in the data,
    #first we need to find the difference between two consecutive data in profitloss
    #and then add each value to the change list. The loop will run each difference in profitloss
    #less 1 row since the position after the last profit/loss value is empty  
    for row in range(len(profitloss)-1):
        data = profitloss[row+1] - profitloss[row]
        change.append(int(data))

    #Calculate for the average differences 
    average_change = sum(change)/(len(profitloss)-1)


    #Function finds greatest increase between consecutive months in profit/loss
    greatest_change = max(change) 
    #Find the index/position of the month with greatest increase in change list 
    great_index=change.index(int(max(change)))+1
    #Assign the index to the month list with associated month
    greatest_month = month[great_index]

    #Function finds greatest decrease between consecutive months in profit/loss
    smallest_change = min(change)
    #Find the associated index/position in the change list 
    smallest_index=change.index(int(min(change)))+1
    #Assign the index to the month list with associated month
    smallest_month = month[smallest_index]

    #Printing results within file 
    print('Financial Analysis')
    print('-------------------------------')
    print(f'Total Months: {month_count}')
    print(f'Total: ${total_budget} ')
    #Print the average change to 2 decimal places 
    print(f'Average Change: ${"%.2f" %average_change}')
    print(f'Greatest Increase in Profits: {greatest_month} (${greatest_change})')
    print(f'Greatest Decrease in Profits: {smallest_month} (${smallest_change})')


#Path for output file
output_file = os.path.join('analysis','budget_analysis.txt')

#Open and writes to file 
with open(output_file, "w", newline="") as budget:
    budget_writer = csv.writer(budget)
    budget_writer.writerow(['Financial Analysis'])
    budget_writer.writerow(['-------------------------------'])
    budget_writer.writerow(['Total Months: ' + str(month_count)])
    budget_writer.writerow(['Total: $' + str(total_budget)])
    budget_writer.writerow(['Average Change: $' + str("%.2f" %average_change)])
    budget_writer.writerow(['Greatest Increase in Profits: ' + str(greatest_month) + ' ($' + str(greatest_change) + ')'])
    budget_writer.writerow(['Greatest Decrease in Profits: ' + str(smallest_month) + ' ($' + str(smallest_change) + ')'])
