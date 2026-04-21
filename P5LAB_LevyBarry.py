# Barry Levy
# April 19, 2026
# Assignment Name: P5LAB_LevyBarry.py
# Program simulates a self-checkout and calculates change using functions.
import random

def disperse_change(change_amount):
    """This function handles ALL the math and ALL the printing."""
    # 1. Convert the float to pennies first
    user_money_int = int(round(change_amount * 100))
    
    if user_money_int <= 0:
        print("No change")
        return # Exit the function early

    # 2. DO ALL MATH HERE (Indented)
    dollars = user_money_int // 100
    user_money_int %= 100
    
    quarters = user_money_int // 25
    user_money_int %= 25
    
    dimes = user_money_int // 10
    user_money_int %= 10
    
    nickels = user_money_int // 5
    user_money_int %= 5
    
    pennies = user_money_int

    # 3. DO ALL PRINTING HERE (Indented)
    if dollars > 0:
        print(f"{dollars} {'dollar' if dollars == 1 else 'dollars'}")
    
    if quarters > 0:
        print(f"{quarters} {'quarter' if quarters == 1 else 'quarters'}")

    if dimes > 0:
        print(f"{dimes} {'dime' if dimes == 1 else 'dimes'}")

    if nickels > 0:
        print(f"{nickels} {'nickel' if nickels == 1 else 'nickels'}")

    if pennies > 0:
        print(f"{pennies} {'penny' if pennies == 1 else 'pennies'}")


def main():
    """This function handles the logic and calls the other function."""
    # 1. Generate random total
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed}")
    
    # 2. Get user input
    cash_put_in = float(input("How much cash will you put in the self-checkout? "))
    
    # 3. Calculate the difference
    change_owed = round(cash_put_in - amount_owed, 2)
    print(f"Change is: ${change_owed}")
    print() 
    
    # 4. HAND THE BATON to the other function
    disperse_change(change_owed)

# THE STARTING LINE: This must be at the very bottom, NOT indented
if __name__ == "__main__":
    main()