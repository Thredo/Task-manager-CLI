# Task Manager CLI:
A simple CLI tool to manage tasks. Built in Python, using a JSON file for storage, and tested with unittest.

## Features:
  - Add tasks with title, priority, and due date
  
  - List tasks (pending (default) or all)
  
  - Edit tasks
  
  - Toggle completion of tasks
  
  - Delete tasks
    
  
## Usage
  Run the CLI:
  
    python main.py add "Buy milk" --priority LOW --due 3
    python main.py list
    
## Tests:

    python -m unittest discover -s tests -p "test_*.py" -v


## List of commands:

  - New task:
    
    - title → string (required, at least 1 character)
    - priority → LOW, MID, HIGH
    - due → number of days from today
      
  Example: 
  
    python main.py add "New task" --priority HIGH --due 5



  - List Tasks:
    - --all -> to show all tasks (even completed) else will show only pending tasks
      
  Example:
  
    python main.py list --all
    python main.py list


  
  - Delete Task:
    - Remove a task by its ID
    
  Example:
    
    python main.py delete 2



  - Toggle Completion:
    - Mark a task as completed, or unmarks it if already completed
 
  Example:

    python main.py toggle 2



  - Edit a Task:
    - You can update title, priority, or due_date
    - due_date expects a number of days from today.
 
  Example:
  
    python main.py edit 3 title "Buy apples"
    python main.py edit 3 priority HIGH
    python main.py edit 3 due_date 1


## Example Workflow
  
    python main.py add "Study Python" --priority MID --due 5
    python main.py list
    python main.py toggle 1
    python main.py edit 1 title "Study Python and AWS"
    python main.py delete 1
