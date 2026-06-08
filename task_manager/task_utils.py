from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)


def add_task(tasks, title, description, due_date):

    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully")


def mark_task_as_complete(tasks, task_number):

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number")
        return

    tasks[task_number - 1]["completed"] = True
    print("Task marked as complete")


def view_pending_tasks(tasks):

    pending = [t for t in tasks if not t["completed"]]

    if len(pending) == 0:
        print("No pending tasks")
        return

    for i, task in enumerate(pending, start=1):
        print(f"\nTask {i}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")


def calculate_progress(tasks):

    if len(tasks) == 0:
        return 0

    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    return (completed / len(tasks)) * 100