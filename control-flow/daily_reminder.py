task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        priority_statement = f"'{task}' is a high priority task"
    case "medium":
        priority_statement = f"'{task}' is a medium priority task"
    case "low":
        priority_statement = f"'{task}' is a low priority task"
    case _:
        print("Unknown priority level.")

if time_bound == "yes":
    time_bound_statement = "that requires immediate attention today!"
    print(f"Reminder: {priority_statement} {time_bound_statement}")
else:
    time_bound_statement = "Consider completing it when you have free time."
    print(f"Note: {priority_statement}. {time_bound_statement}")
