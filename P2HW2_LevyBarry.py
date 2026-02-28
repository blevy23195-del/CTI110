# Barry Levy
# February 27, 2026
# Assignment: P2HW2 - List Basics
# Description: This program collects grades for six modules, stores them in a list
# displays the lowest, highest, sum, and average of those grades.


'''
Pseudocode:
1. Input Module 1 grade and convert to float
2. Input Module 2 grade and convert to float
3. Input Module 3 grade and convert to float
4. Input Module 4 grade and convert to float
5. Input Module 5 grade and convert to float
6. Input Module 6 grade and convert to float
7. Store grades in a list named 'module_grades'
8. Find lowest grade in list
9. Find highest grade in list
10. Calculate sum of grades
11. Calculate average of grades
12. Display results formatted with 2 decimal places
'''

# Step 1: Get user inputs (20 points)
m1 = float(input("Enter grade for Module 1: "))
m2 = float(input("Enter grade for Module 2: "))
m3 = float(input("Enter grade for Module 3: "))
m4 = float(input("Enter grade for Module 4: "))
m5 = float(input("Enter grade for Module 5: "))
m6 = float(input("Enter grade for Module 6: "))

# Step 2: Create the list (20 points)
module_grades = [m1, m2, m3, m4, m5, m6]

# Step 3: Perform calculations (10 points each)
lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

# Using a width of 18 or 20 to make sure the values line up in a column

print("\n------------Results------------")
print(f"{'Lowest Grade:':<18} {lowest:.2f}")
print(f"{'Highest Grade:':<18} {highest:.2f}")
print(f"{'Sum of Grades:':<18} {total:.2f}")
print(f"{'Average:':<18} {average:.2f}")
print("--------------------------------")
