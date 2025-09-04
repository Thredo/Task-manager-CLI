#Imports
from dataclasses import asdict
from datetime import date, timedelta, datetime
import json
#Files
from task import Task

# id, title, priority, due_date, is_completed
def create_task(title:str, priority:str, due_date:int):
    priorities = ("LOW",  "MID", "HIGH")
    if len(title) < 1:
        print("Cannot add Task. Title must have at leat one character")
        return False
    if priority.upper() not in priorities:
        print("Cannot add Task. Priority must be LOW, MID or HIGH")
        return False
    
    corrected_date = str(date.today() + timedelta(due_date))
    correct_id = new_id()

    new_task = Task(id=correct_id,title=title, priority=priority.upper(), due_date=corrected_date)
    upload_task(new_task)

# Depending on the opttion given it will print tasks. By default it wont show completed tasks.
def list_tasks(option = "default"):
    tasks = load_tasks()
    if option.lower() == "all":
        for t in tasks:
            json_date = datetime.strptime(t["due_date"], "%Y-%m-%d").date()
            due = (json_date - date.today()).days
            status = ""
            if t["is_completed"]:
                status = "Completed"
            else:
                status = "NOT Completed"
            print(f'Task id:{t["id"]} -- {t["title"]} -- Due date: {due} days. Priority: {t["priority"]} -- Status: {status}')
    else:
        for t in tasks:
            if not t["is_completed"]:
                json_date = datetime.strptime(t["due_date"], "%Y-%m-%d").date()
                due = (json_date - date.today()).days
                print(f'Task id:{t["id"]} -- {t["title"]} -- Due date: {due} days. Priority: {t["priority"]} -- Status: NOT Completed')


#Finds task by id and deletes it printing a message for error or success
def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [t for t in tasks if t["id"] != task_id]

    if len(tasks) == len(updated_tasks):
        print(f"Task with id {task_id} was not found")
        return False
    try: 
        save_tasks(updated_tasks)
    except Exception as e:
        print(f"Error: {e}")
        return False
    else:
        print(f"Task with id {task_id} was successfully deleted")
        return True

# Finds task with id and marks it as True/False depending on the state, printing a message for error or success.
def toggle_completed(task_id):
    tasks = load_tasks()
    found = False

    for t in tasks:
        if t["id"] == task_id:
            t["is_completed"] = not t["is_completed"]
            found = True
            break
    if not found:
        print("Task not found")
        return False
    try:
        save_tasks(tasks)
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Task with id {task_id} state was changed")
        return True

# Using the id, it changes the field to the new value and prints a message for error or success
def edit_task(task_id, field, edit):
        tasks = load_tasks()
        found = False
        if field.lower()== "id":
            print("Cannot change id of tasks")
            return False
        field = field.lower()
        available_fields = ("title", "priority", "due_date")
        if field not in available_fields:
            print("Please choose a correct field")
            return False
        if field == "due_date":
            days_edit = int(edit)
            edit = str(date.today() + timedelta(days=days_edit)) 
        if field == "priority":
            priorities = ("LOW",  "MID", "HIGH")
            edit = edit.upper()
            if edit not in priorities:
                print("Please choose a correct priority state")
                return False
        for t in tasks:
            if t["id"] == task_id:
                t[f"{field.lower()}"] = edit
                found = True
                break
        if not found:
            print("Task not found, check the id or property you want to change are correct")
            return False
        try:
            save_tasks(tasks)
        except Exception as e:
            print("Error: {e}")
        else:
            print(f"Task id {task_id} -> {field} is now {edit}")
            return True

#loads all the tasks from Json file and returns a LIST
def load_tasks() -> list:
    task_list = []
    try:
        with open("tasks.json", "r") as f:
           task_list = json.load(f)
        return task_list
    except  (json.JSONDecodeError, FileNotFoundError):
        return []
    except Exception as e:
        print(f"Error while opening the JSON file: {e}")
        return []

# Opens json file and uploads the new task returning a print message for error or success
def upload_task(new_task):
    tasks = load_tasks()
    tasks.append(asdict(new_task))
    try:
        save_tasks(tasks)
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("Task added successfully")

# Loads the tasks, checks for the next available id and returns it (id is an INT)
def new_id() -> int:
    tasks_dict = load_tasks()
    existing_id = [t["id"] for t in tasks_dict]
    new_id = 1
    while new_id in existing_id:
        new_id+=1
    return new_id

#Saves task list into the JSON file
def save_tasks(tasks: list):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)