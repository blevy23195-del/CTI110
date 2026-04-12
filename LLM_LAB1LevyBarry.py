# Barry Levy
# 4/10/2026
# LLM_LAB1 To-Do List Manager
# This program is A to-do list manager that saves tasks to a file

import datetime

def main():
    # List to store task dictionaries
    tasks = []
    
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        # --- OPTION 1: ADD TASK ---
        if choice == '1':
            name = input("Enter task name: ")
            
            # Input Validation Loop for Difficulty
            while True:
                difficulty = input("Enter difficulty level (1-5): ")
                if difficulty.isdigit() and 1 <= int(difficulty) <= 5:
                    difficulty = int(difficulty) 
                    break 
                else:
                    print("Invalid input! Please enter a whole number between 1 and 5.")
            
            # Creating the dictionary and adding to list
            new_task = {
                "task_name": name,
                "creation_date": datetime.date.today().strftime("%Y-%m-%d"),
                "completion_date": "Awaiting Completion",
                "difficulty_level": difficulty
            }
            tasks.append(new_task)
            print("Task added successfully!")

        # --- OPTION 2: VIEW ALL TASKS ---
        elif choice == '2':
            if not tasks:
                print("\nYour list is currently empty.")
            else:
                print("\n--- Current Tasks ---")
                for index, t in enumerate(tasks, start=1):
                    print(f"{index}. {t['task_name']} | Difficulty: {t['difficulty_level']}")
                    print(f"   Created: {t['creation_date']} | Status: {t['completion_date']}")

        # --- OPTION 3: MARK TASK AS COMPLETED ---
        elif choice == '3':
            if not tasks:
                print("\nNo tasks to complete.")
            else:
                # Show tasks so the user knows which number to pick
                for index, t in enumerate(tasks, start=1):
                    print(f"{index}. {t['task_name']}")
                
                try:
                    task_num = int(input("Enter the task number to mark complete: "))
                    if 1 <= task_num <= len(tasks):
                        tasks[task_num - 1]["completion_date"] = datetime.date.today().strftime("%Y-%m-%d")
                        print("Task marked as completed!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        # --- OPTION 4: EXIT ---
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        
        # --- CATCH-ALL FOR INVALID MENU CHOICES ---
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()