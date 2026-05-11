# TO-DO LIST APPLICATION

tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                status = "✅ Completed" if t["completed"] else "❌ Pending"
                print(f"{i}. {t['task']} - {status}")

    # Update Task
    elif choice == "3":
        if not tasks:
            print("No tasks to update.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['task']}")

            try:
                task_no = int(input("Enter task number to update: "))
                if 1 <= task_no <= len(tasks):
                    new_task = input("Enter updated task: ")
                    tasks[task_no - 1]["task"] = new_task
                    print("Task updated successfully!")
                else:
                    print("Invalid task number. Please enter a number from the list.")
            except ValueError:
                print("Error: Please enter a valid numerical value.")

    # Delete Task
    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['task']}")

            try:
                task_no = int(input("Enter task number to delete: "))
                if 1 <= task_no <= len(tasks):
                    removed = tasks.pop(task_no - 1)
                    print(f"Deleted task: {removed['task']}")
                else:
                    print("Invalid task number. Please enter a number from the list.")
            except ValueError:
                print("Error: Please enter a valid numerical value.")

    # Mark Task
