import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []

    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not load tasks. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except OSError:
        print("Error: Could not save tasks.")


def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n========== TO-DO LIST ==========")

    for task in tasks:
        status = "✓" if task["completed"] else " "
        print(f'{task["id"]}. [{status}] {task["title"]}')

    print("================================")


def add_task(tasks):
    """Add a new task."""
    title = input("\nEnter task: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    new_id = max((task["id"] for task in tasks), default=0) + 1

    task = {
        "id": new_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def complete_task(tasks):
    """Mark a task as completed."""
    display_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("\nEnter task ID to complete: "))

        for task in tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("Task is already completed.")
                else:
                    task["completed"] = True
                    save_tasks(tasks)
                    print("Task marked as completed.")
                return

        print("Task not found.")

    except ValueError:
        print("Please enter a valid task ID.")


def delete_task(tasks):
    """Delete a task."""
    display_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("\nEnter task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks(tasks)
                print("Task deleted successfully.")
                return

        print("Task not found.")

    except ValueError:
        print("Please enter a valid task ID.")


def clear_completed_tasks(tasks):
    """Delete all completed tasks."""
    completed_count = sum(task["completed"] for task in tasks)

    if completed_count == 0:
        print("\nNo completed tasks to clear.")
        return

    tasks[:] = [task for task in tasks if not task["completed"]]
    save_tasks(tasks)

    print(f"{completed_count} completed task(s) removed.")


def show_menu():
    """Display the main menu."""
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Clear Completed Tasks")
    print("6. Exit")
    print("================================")


def main():
    """Run the To-Do List application."""
    tasks = load_tasks()

    print("\nWelcome to the Python To-Do List!")

    while True:
        show_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            clear_completed_tasks(tasks)

        elif choice == "6":
            print("\nThank you for using the To-Do List!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()