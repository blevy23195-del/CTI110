# Barry Levy
# 3/23/2026
# P4LAB2 - Learn while loops

# Set choice to be the empty string
choice = ""

# Keep running so long as choice is not 'no"
while choice != "no":
    user_int = int(input("Enter an integer) "))
    print()
    if user_int >= 0:
        #show math
        for i in range(1,13):
            print(f"{user_int} * {i} = {user_int * i}")
    else:
        print("Program does not allow negatives!")
    
    
    # Allow user to give input on running agaain
    choice = input("Run program again? (yes/no): ")
    print()
    
# loop breaks here
print("Hope you enjoyed the program, goodbye!")

