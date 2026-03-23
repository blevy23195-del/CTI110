# Barry Levy 
# Date: March 14, 2026
# Grade Analysis

# 1. Get grades for six modules (Fixed names and added float  conversion)

mod_1 = float(input('Enter grade for module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# 2. Add grades to a list (Fixed commas and missing mod_6)
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# 3. Calculate statistics (Fixed case sensitivity and logic)
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# 4. Display Results
print("\n------------Results------------")
print(f'{"Lowest Grade:":<18}{low}')
print(f'{"Highest Grade:":<18}{high}')
print(f'{"Sum of Grades:":<18}{total}')
print(f'{"Average:":<18}{avg:.2f}')
print("--------------------------------")

# 5. Determine letter grade (Fixed logic with elif)
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')

