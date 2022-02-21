from typing import Dict

from ..application.repositories import TodosRepository
from ..domain.entities import Todo
from ..domain.value_objects import TodoId

class InMemoryTodosRepo(TodosRepository):
    def __init__(self):
        self._data: Dict[TodoId, Todo] = {}

    def get(self, todo_id: TodoId) -> Todo:
        return self._data[todo_id]

    def save(self, todo: Todo) -> None:
        self._data[todo.id] = todo
