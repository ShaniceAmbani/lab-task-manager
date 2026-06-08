from datetime import datetime


def validate_task_title(title):
    if not title.strip():
        raise ValueError("Task title cannot be empty.")
    return True


def validate_task_description(description):
    if not description.strip():
        raise ValueError("Task description cannot be empty.")
    return True


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")