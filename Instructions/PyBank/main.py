def show_line():
    print(f"-"*30)


import os
import csv
 
with open("budget_data.csv", "r") as file :
    data = csv.reader(file)
    header = next(data) 
    date = []
    profit_loss = []            
    variation = []
    count_line = 0 
    net_total = 0
    average_total = 0 
    count_var = 0
    var_total = 0
    for row in data:
        profit_loss.append(row[1])
        date.append(row[0])
        count_line += 1        
        net_total += int(row[1])
 
    for i in range(len(profit_loss)-1):
        variation.append(int(profit_loss[i+1]) - int(profit_loss[i]))
     
    for row in variation:    
        count_var += 1
        var_total += int(row)
    average_change = var_total/count_var
    
    max_increase = max(variation)
    max_decrease = min(variation)
    date_max_increase = (date[int(variation.index(max_increase)+1)])
    date_max_decrease = (date[int(variation.index(max_decrease)+1)])
 
    
    print("Financial Analysis")
    show_line()
    print(f"Total Months: {count_line}")
    print(f"Total Profit/Losses: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {date_max_increase}: ${max_increase}")
    print(f"Greatest Decrease in Profits: {date_max_decrease}: ${max_decrease}")
    show_line()
print("Saving results to Analysis.txt.")
with open('Analysis.txt', 'w+') as file:
    file.write("Financial Analysis \n")
    file.write(f"-"*30)
    file.write("\n")
    file.write(f"Total Months: {count_line}\n")
    file.write(f"Total Profit/Losses: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {date_max_increase}: ${max_increase}\n")
    file.write(f"Greatest Decrease in Profits: {date_max_decrease}: ${max_decrease}\n")