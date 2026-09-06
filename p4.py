tasks = []

while True:
    print("\n--- TASK SCHEDULER ---")
    print("1. Add Task")
    print("2. Run Tasks")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        priority = input("Enter priority (high/low): ").lower()
        condition = input("Is the task ready? (yes/no): ").lower()

        tasks.append([task, priority, condition])
        print("Task added successfully.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nChecking tasks...")

            remaining = []

            for task in tasks:
                name = task[0]
                priority = task[1]
                condition = task[2]

                # Boolean logic and short-circuit evaluation
                if condition == "yes" and priority == "high":
                    print("Executing HIGH priority task:", name)

                elif condition == "yes" or priority == "high":
                    print("Executing task:", name)

                elif not condition == "yes":
                    print("Task not ready:", name)
                    remaining.append(task)

            tasks = remaining

    elif choice == "3":
        if len(tasks) == 0:
            print("Task queue is empty.")
        else:
            print("\nPending Tasks:")

            for task in tasks:
                print(
                    "-", task[0],
                    "| Priority:", task[1],
                    "| Ready:", task[2]
                )

    elif choice == "4":
        print("Exiting Task Scheduler...")
        break

    else:
        print("Invalid choice. Please try again.")