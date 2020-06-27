
# Script to analyze bank data
import os
import csv

BUDGET_PATH = os.path.join('c:/Users/User/Desktop/DataViz/Repos/bank-electionAnalysis/data/budget_data.csv')
#print(BUDGET_PATH)
# open and read budget data set
with open(BUDGET_PATH, newline='') as budget_path:
    budgetreader = csv.reader(budget_path, delimiter=',')
    #print(budget_df) # for testing
    header = next(budget_path, None) # skips header row 
    month = 0
    total = 0
    prof_loss = 0
    dPL = [] # array of values for difference in profit/loss
    dates = []
    for row in budgetreader: # read through each row of data after the header 
        month += 1
        total += int(row[1])
        prof_loss = row[1]
        dPL.append(prof_loss) # appends values in profit/loss column
        dates.append(row[0])
# print("Total Months:", month)
# print("Total:", total)

dPL = list(map(int, dPL)) # changing list of strings to list of integers
# print(dPL)

# loop to determine average change in profits/losses
diff_dPL = []
for i in range(0,month-1): # loops through the difference between rows
    diff_dPL.append(dPL[i+1]-dPL[i])
sum_dPL = sum(diff_dPL)
avg_dPL = sum_dPL / (month - 1)
print("Average Change in Profit/Loss:", avg_dPL)
# print(diff_dPL)

# Joining 2 lists to perform max/min calculations
import os 
import csv

new_budget = zip(dates, diff_dPL) # zips lists together into tuples
new_budget_output = os.path.join("new_budget.csv")

with open(new_budget_output, "w", newline="") as new_budget_file:
    new_budgetwriter = csv.writer(new_budget_file)
    new_budgetwriter.writerows(["Date", "Profit/Losses"])
    new_budgetwriter.writerows(new_budget)

max_dPL = diff_dPL[0] # initial value 
min_dPL = diff_dPL[0] # initial value
for i in range(0,len(diff_dPL),1): # loops through array of differential values
    if max_dPL < diff_dPL[i]:
        max_dPL = diff_dPL[i]
    max_dPL = max(max_dPL,diff_dPL[i]) # finds maximum value 
    min_dPL = min(min_dPL,diff_dPL[i]) # finds minimum value

# Finding indexes for greatest increase and decrease of profits and losses
print("Greatest Increase in Profits:", max_dPL)
print("Greatest Increase Index:", diff_dPL.index(max_dPL)) # index for greatest increase in profits 
print("Greatest Decrease In Losses:", min_dPL)
print("Greatest Decrease Index:", diff_dPL.index(min_dPL)) # index for greatest decrease in losses

# Outputs final data analysis
print(
    f"""
    Financial Analysis
    --------------------------------
    Total Months: {month}
    Total: {total}
    Average Change in Profit/Loss: ${round(avg_dPL, 2)}
    Greatest Increase in Profits: {dates[25]}, ${round(max_dPL, 2)}
    Greatest Decrease in Profits: {dates[44]}, ${round(min_dPL, 2)}
    """)
