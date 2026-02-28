# Barry Levy
# February 27, 2026
# Travel Budget Formatter
# This program calculates travel expenses and displays them in a formatted table

print ("This program calculates and displays travel expenses\n")

# Step 1: Get user input and convert money values values to floats
budget = float(input("Enter Budget"))
dest = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("last, how much do you need for food? "))

# Step 2: Calculate remaining balance
total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

# Step 3: Display the formatted output
print("\n-----------Travel Expenses------------")

# We use a width of 20 for the labels to ensure the values line up perfectly
print(f"{'Location:':<20}{dest}")
print(f"{'Initial Budget:':<20}${budget:,.2f}")
print(f"{'Fuel:':<20}${gas:,.2f}")
print(f"{'Accommodation:':<20}${hotel:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")

print("------------------------------------------")

print(f"{'Remaining Balances:':<20}${remaining_balance:,.2f}")

