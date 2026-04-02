# Barry Levy
# 3/24/2026
# P4HW1- Score Collector
# This program collects a user-defined number of scores, validates them,
# drops the lowest, and calculates a final letter grade.

# 1. Input: num_scores (int)
# 2. Loop for i in range(num_scores):
#      Input: score
#      While score < 0 or score > 100:
#          Output Error, Re-input score
#      Append valid score to list
# 3. lowest = min(list)
# 4. list.remove(lowest)
# 5. average = sum(list) / len(list)
# 6. Determine Grade (A, B, C, D, or F)
# 7. Display results formatted to 1 decimal place

def main():
    # 1. Ask for number of scores
    num_scores = int(input("How many scores do you want to enter? "))
    
    
    score_list = []
    
    # 2. Collect scores using a loop
    for i in range(1, num_scores + 1):
        score = float(input(f"Enter score #{i}: "))
        
        # Validation Loop (The "Nested" loop)
        while score < 0 or score > 100:
            print("\nINVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            score = float(input(f"Enter score #{i} again: "))
        
        score_list.append(score)

    # --- Processing Results ---
    lowest_score = min(score_list)
    
    # Create a copy or modify list to drop lowest
    modified_list = score_list[:]
    modified_list.remove(lowest_score)
    
    avg_score = sum(modified_list) / len(modified_list)

    # Determine Letter Grade
    if avg_score >= 90:
        grade = "A"
    elif avg_score >= 80:
        grade = "B"
    elif avg_score >= 70:
        grade = "C"
    elif avg_score >= 60:
        grade = "D"
    else:
        grade = "F"

    # --- Final Output ---
    print("\n--------------Results-----------")
    print(f"Lowest Score  : {lowest_score}")
    print(f"Modified List : {modified_list}")
    print(f"Scores Average: {avg_score:.2f}")
    print(f"Grade         : {grade}")
    print("----------------------------------")

    # Run the program
main()
