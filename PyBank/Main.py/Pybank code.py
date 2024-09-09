import csv 
total_months = 0
net_total = 0 
changes = [] 
previous_profit_loss = None 
greatest_increase = ["", 0] 
greatest_decrease = ["", 0] 
file_path = 'C:/Users/DonJa/Documents/Module 3 Challenge/PyBank/Resources/budget_data.csv' 
output_file_path = 'C:/Users/DonJa/Documents/Module 3 Challenge/PyBank/Resources/financial_analysis.txt'
with open(file_path, mode='r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)

            header = next(csvreader) 

            for row in csvreader:
                date = row[0]
                profit_loss = int(row[1])

                total_months += 1
                net_total += profit_loss

                if previous_profit_loss is not None:
                    change = profit_loss - previous_profit_loss
                    changes.append(change)

                    if change > greatest_increase[1]:
                        greatest_increase = [date, change]
                    if change < greatest_decrease[1]:
                        greatest_decrease = [date, change]

                previous_profit_loss = profit_loss
            average_change = sum(changes) / len(changes) if changes else 0 
results = [
    f"Total Months: {total_months}",
    f"Total: ${net_total}",
    f"Average Change: ${round(average_change, 2)}",
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})",
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
]

# Print results to the terminal
for result in results:
    print(result)

# Write results to a text file
with open(output_file_path, mode='w') as outfile:
    outfile.write("\n".join(results))

print(f"Results have been written to {output_file_path}")
