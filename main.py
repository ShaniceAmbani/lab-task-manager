from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)

tasks = []

while True:

    print("\nTASK MANAGEMENT SYSTEM")
    print("1. Add Task")
    print("2. Mark Task Complete")
    print("3. View Pending Tasks")
    print("4. View Progress")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        title = input("Title: ")
        description = input("Description: ")
        due_date = input("Due Date (YYYY-MM-DD): ")

        try:
            add_task(tasks, title, description, due_date)
        except ValueError as e:
            print(e)


    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")
            continue

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['title']}")

        try:
            number = int(input("Task number: "))
            mark_task_as_complete(tasks, number)
        except ValueError:
            print("Invalid input")


    elif choice == "3":

        view_pending_tasks(tasks)


    elif choice == "4":

        progress = calculate_progress(tasks)
        print(f"Progress: {progress:.2f}%")


    elif choice == "5":

        print("Goodbye!")
        break


    else:
        print("Invalid choice")