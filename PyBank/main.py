#dependencies
import csv
import os
#load files
budget = os.path.join('Resources', 'budget_data.csv')

# Open the file
data=[]
with open(budget, 'r') as file:
    # Read the file
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)
#analysis
month_count=len(data)
total=0
previous_profit=0
max=0
min=0
total_change=0
increase=['',0]
decrease=['',0]
change_list=[]
for row in data:
    Profit=int(row['Profit/Losses'])
    change = Profit-previous_profit
    if change>max:
        max=change
        increase[0]=row['Date']
        increase[1]=max
    if change<min:
        min=change
        decrease[0]=row['Date']
        decrease[1]=min
    change_list.append(change)
    previous_profit = Profit
    total += Profit
    total_change+=change
avg_change=round((sum(change_list)-int(data[0]['Profit/Losses']))/(len(change_list)-1),2)
#output
analysis=(
f'Financial Analysis\n'
f'----------------------------\n'
f'Total Months: {month_count}\n'
f'Total: ${total}\n'
f'Average Change: ${avg_change}\n'
f'Greatest Increase in Profits: {increase}\n'
f'Greatest Decrease in Profits: {decrease}\n'
)
print(analysis)
output = os.path.join("Analysis", "budget_analysis.txt")
with open(output, "w") as x:
    x.write(analysis)
