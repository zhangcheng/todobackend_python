from dataclasses import dataclass

from .value_objects import TodoId

@dataclass
class Todo:
    id: TodoId
    title: str
    order: int
    completed: bool = False
