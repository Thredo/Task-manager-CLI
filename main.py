#Imports
import argparse

#Files
import task_manager as tm

def main():
    parser = argparse.ArgumentParser(description="Task manager CLI!")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add function
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="Task title")
    add_parser.add_argument("priority", type=str, help="Priority: LOW, MID, HIGH")
    add_parser.add_argument("due", type=int, help="Due date in days from today")

    # List of tasks
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--all", action="store_true", help="Show completed tasks as well")

    # Deletes task by id
    delete_parser = subparsers.add_parser("delete", help="Delete a task by id")
    delete_parser.add_argument("id", type=int, help="Task id")

    # Toggle completion of task
    toggle_parser = subparsers.add_parser("toggle", help="Toggle task completed state")
    toggle_parser.add_argument("id", type=int, help="Task id")

    # Edits fields (title, priority, due date) of task
    edit_parser = subparsers.add_parser("edit", help="Edit a field of a task")
    edit_parser.add_argument("id", type=int, help="Task id")
    edit_parser.add_argument("field", type=str, help="Field: title, priority, due_date")
    edit_parser.add_argument("value", type=str, help="New value (string or days for due_date)")

    # Parse args
    args = parser.parse_args()

    # Assigning commands to task_manager
    if args.command == "add":
        tm.create_task(args.title, args.priority, args.due)

    elif args.command == "list":
        option = "all" if args.all else "default"
        tm.list_tasks(option)

    elif args.command == "delete":
        tm.delete_task(args.id)

    elif args.command == "toggle":
        tm.toggle_completed(args.id)

    elif args.command == "edit":
        tm.edit_task(args.id, args.field, args.value)


if __name__ == "__main__":
    main()