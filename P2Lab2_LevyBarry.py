# Your First name and Last Name
# 2/19/2026
# P2LAB2
# A program that calculates gas consumption based on vehicle MPG stored in a dictionary.

# 1. Create the dictionary with the specified car data
cars_mpg = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}

# 2. Get all keys from the dictionary 
keys = cars_mpg.keys()

# 3. Print the keys (this shows the user what options they have)
print (keys)
print() # Adding a blank line for readability

# 4. Prompt the user to enter a vehicle name
selected_car = input("Enter a vehicle to see it's MPG: ")
mpg = cars_mpg[selected_car]
# 5. Retrieve and display the MPG for the entered vehicle 
print(f"The {selected_car} gets {mpg} MPG.")
print()

# 6. Prompt user for miles they will drive
miles_to_drive = float(input(f"How many miles will you drive the {selected_car}? "))
                             
# 7. Calculate gallons of gas needed
# Formula: Gallons = Miles / mpg 
gallons_needed = miles_to_drive / mpg

# 8. Display result rounded to two decimal places using an f-string
print(f"{gallons_needed:.2f} gallons of gas are needed to drive the {selected_car} {miles_to_drive} miles.")


                                                   