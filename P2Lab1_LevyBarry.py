# Your First Name and Last Name
# 2/16/2026
# P2LAB1
# Using a Library with formulas of a circle

import math

# print(math.pi)
# Get a radius from the user as a float
radius = float(input("Enter the radius of the circle"))

print()

# Calculate diameter
diameter = 2 * radius


# Display diameter with 1 decimal place
print(f"The diameter of the circle is {diameter:.1f}")

print()
# Calculate circumference
circumference = 2 * math.pi * radius

# Display circumference with 2 decimal places
print(f"The circumference is: {circumference:.2f}")

print()

# Calculate the area
area = math.pi * math.pow(radius,2)

# Display the area with 3 decimal places
print(f"The area is: {area:.3f}")
