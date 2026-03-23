# Barry Levy
# February 13, 2026
# P1HW1
# A program that calculates exponents and performs basic addition and subtraction

print("-----Calculating Exponents-----\n")
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
result_exp = base ** exponent
print(f"\n{base} raised to the power of {exponent} is {result_exp} !!")


print("\n-----Addition and Subtraction-----\n")
start_num = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
sub_num = int(input("Enter an integer to subtract: "))



# Perform the math 
final_total = start_num + add_num - sub_num 
 
# Display the final string 
print(f"\n{start_num} + {add_num} - {sub_num} is equal to {final_total}")