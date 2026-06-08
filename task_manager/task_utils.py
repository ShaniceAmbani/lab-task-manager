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
    return True


def mark_task_as_complete(tasks, task_number):

    if task_number < 1 or task_number > len(tasks):
        return False

    tasks[task_number - 1]["completed"] = True
    return True


def view_pending_tasks(tasks):

    pending_tasks = [
        task for task in tasks
        if not task["completed"]
    ]

    if not pending_tasks:
        return []

    return pending_tasks


def calculate_progress(tasks):

    if len(tasks) == 0:
        return 0

    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    return (completed / len(tasks)) * 100