from dataclasses import dataclass

@dataclass
class Task:
    id : int
    title : str
    priority : str
    due_date : str
    is_completed : bool = False
