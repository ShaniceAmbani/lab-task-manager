from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)


def add_task(tasks, title, description, due_date):

    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })


def mark_task_as_complete(tasks, task_number):

    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True


def view_pending_tasks(tasks):

    return [
        task for task in tasks
        if not task["completed"]
    ]


def calculate_progress(tasks):

    if len(tasks) == 0:
        return 0

    completed = sum(1 for t in tasks if t["completed"])
    return (completed / len(tasks)) * 100