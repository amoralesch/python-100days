# Tip Calculator

# Learn about numeric data types, casting, math operations and rounding.

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

total = round(bill * (100 + percentage) / 100 / people, 2)
total_formatted = "{:.2f}".format(total)

print(f"Each person should pay: ${total_formatted}")
