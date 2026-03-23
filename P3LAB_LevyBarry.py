# Barry Levy
# March 3, 2026
# This program allows the user to enter a money (float) value with two places after the decimal.

# Get the amount from the user
money_float = float(input("Enter the amount of money: $"))

# Convert float to total cents as an integer
total_cents = int(round(money_float * 100))

# Calculate Dollars
num_dollars = total_cents // 100
total_cents = total_cents % 100  # This keeps only the remaining cents

if num_dollars > 0:
    if num_dollars == 1:
        print(f'{num_dollars} Dollar')
    else:
        print(f'{num_dollars} Dollars')
 # Calculate Quarters
num_quarters = total_cents // 25
total_cents = total_cents % 25

if num_quarters > 0:
    if num_quarters == 1:
        print("1 Quarter")
    else:
        print(f"{num_quarters} Quarters") 


# Calculate Dimes
num_dimes = total_cents // 10
total_cents = total_cents % 10

if num_dimes > 0:
    if num_dimes == 1:
        print("1 Dime")
    else:
        print(f"{num_dimes} Dimes")

# Calculate Nickels
num_nickels = total_cents // 5
total_cents = total_cents % 5

if num_nickels > 0:
    if num_nickels == 1:
        print("1 Nickel")
    else:
        print(f"{num_nickels} Nickels")

# Calculate Pennies
num_pennies = total_cents # Whatever is left over
if num_pennies > 0:
    if num_pennies == 1:
        print("1 Penny")
    else:
        print(f"{num_pennies} Pennies")  
                    
else: 
    print("No Change")