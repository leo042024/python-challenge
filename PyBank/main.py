import csv
import os
csvpath = "PyBank/Resources /budget_data.csv"

month_count = 0
profit_loss = 0
total_profit_loss = 0

months = []
profit_loss_l = []
profit_loss_change = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)
        month_count += 1
        profit_loss = int(row[1])
        profit_loss_l.append(profit_loss)
        print(profit_loss_l)

        months.append(row[0])

        

        total_profit_loss += profit_loss

for i in range(len(profit_loss_l)-1):
    difference = (profit_loss_l[i+1] - profit_loss_l[i])
    print(difference)
    profit_loss_change.append(difference)
    
print("")
average = sum(profit_loss_change)/len(profit_loss_change)


Greatest_Increase = max(profit_loss_change)
Greatest_Decrease = min(profit_loss_change)

Highest_month_index = profit_loss_change.index(Greatest_Increase)
Lowest_month_index = profit_loss_change.index(Greatest_Decrease)




print("Financial Analysis")
print("________________________________________________________")
print("Total Months: ", month_count)
print("Total Profit/Loss: $",total_profit_loss)
print("Average Change: ", average)
print("Greatest Increase in Profits: ", months[Highest_month_index+1],Greatest_Increase)
print("Greatest Decrease in Profits: ", months[Lowest_month_index+1],Greatest_Decrease)

    

PyModASSMT = os.path.join("PyBank/analysis/new.csv")

with open(PyModASSMT, 'w') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')
   
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["________________________________________________________"])
    csvwriter.writerow(["Total Profit/Loss: $",total_profit_loss])
    csvwriter.writerow(["Average Change: ", average])
    csvwriter.writerow(["Greatest Increase in Profits: ", months[Highest_month_index+1],Greatest_Increase])
    csvwriter.writerow(["Greatest Decrease in Profits: ", months[Lowest_month_index+1],Greatest_Decrease])







   



