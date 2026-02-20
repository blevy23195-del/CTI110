# Barry Levy
# February 13, 2026
# P1HW2
# This program calculates and displays travel expenses based ona user provided:

# Pseudocode:
# 1. Ask user for their initial budget
# 2. Ask user for their travel destination
# 3. Ask user for their gas, accomodation, and food costs
# 4. Add all three expenses together
# 5. Subtract the total expenses from the initial budget
# 6. Display the destination, the initial budget, and the remaining balance

print("This program calculates and displays travel expenses\n")

# Get user inputs
budget = float(input("Enter Budget: "))
dest = input("Enter your travel destination: ")

gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

print("\n------------Travel Expenses------------")
print(f"Location: {dest}")
print(f"Initial Budget: {budget}")

print(f"\nFuel: {gas}")
print(f"Accommodation: {hotel}")
print(f"Food: {food}")

# Calculate total expenses and remaining balance
total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

print("---------------------------------------")
print(f"\nRemaining Balance: {remaining_balance}")
