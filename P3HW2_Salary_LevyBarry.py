# Barry Levy 
# Date: March 14, 2026
# Assignment: P3HW2 - Salary
# A program to calculate an employee's regular pay, overtime pay, and gross pay.
'''  
1. Get the employee name as a string.
2. Get the number of hours worked as a float.
3. Get the hourly pay rate as a float.
4. Check if hours worked is greater than 40:
    a. If yes, calculate overtime hours (hours - 40).
    b. Calculate overtime pay (overtime hours * rate * 1.5).
    c. Calculate regular pay (40 * rate).
5. If hours worked is 40 or less:
    a. Overtime hours is 0.
    b. Overtime pay is 0.
    c. Regular pay is (hours worked * rate).
6. Calculate gross pay by adding regular pay and overtime pay.
7. Display employee name.
8. Display a table showing: Hours Worked, Pay Rate, Overtime, Overtime Pay, RegHour Pay, and Gross Pay.
'''                                                                                                                                                                                                  

def main():
    # User inputs
    name = input("Enter employee's name: ")
    hours = float(input("Enter number of hours worked: "))
    rate = float(input("Enter employee's pay rate: "))

    # Decision logic for overtime
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours * rate

    # Calculate total gross pay
    gross_pay = regular_pay + overtime_pay

    # Output formatting
    print("-" * 37)
    print(f"Employee name:  {name}")
    print()
    
    # Column headers
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'Overtime':<12}{'Overtime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")
    print("-" * 85)
    
    # Data row formatted for currency/alignment
    print(f"{hours:<15.1f}{rate:<12.1f}{overtime_hours:<12.1f}{overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:<10.2f}")

if __name__ == "__main__":
    main()




