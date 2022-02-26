from typing import List
from ..todo.application.queries import GetSingleTodo, GetAllTodos
from ..todo.application.repositories import TodosRepository
from ..todo.domain.entities import Todo
from ..todo.domain.value_objects import TodoId


class SqlQuery:
    def __init__(self, repo: TodosRepository) -> None:
        self._repo = repo


class SqlGetSingleTodo(GetSingleTodo, SqlQuery):
    def query(self, todo_id: TodoId) -> Todo:
        return self._repo.get(todo_id)


class SqlGetAllTodos(GetAllTodos, SqlQuery):
    def query(self) -> List[Todo]:
        return self._repo.get_all()
