# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
net_change_sum = 0
greatest_decrease = ["",0]
greatest_increase = ["", 0]

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months = 1
    total_net = int(first_row[1])
    prev_net = int(first_row[1])

    # Track the total and net change
   
    # Process each row of data
    for row in reader:
        date = row[0]
        current_net = int(row[1])
        # Track the total
        total_months = total_months + 1
        total_net = total_net + current_net

        # Track the net change
        net_change = current_net - prev_net
        net_change_sum = net_change_sum + net_change
        

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase = [date, net_change]

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease = [date, net_change]

        prev_net = current_net

# Calculate the average net change across the months
    avg_net_change = net_change_sum / (total_months - 1)

# Generate the output summary
output = (
    f'Financial Analysis \n'
    f'---------------------------- \n'
    f'Total Months: {total_months}\n'
    f'Total: ${total_net}\n'
    f'Average Change: ${avg_net_change:.2f}\n'
    f'Greatest Increase in Profits: ${greatest_increase[0]} (${greatest_increase[1]})\n'
    f'Greatest Decrease in Profits: ${greatest_decrease[0]} (${greatest_decrease[1]})\n'

)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)