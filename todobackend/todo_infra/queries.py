from ..todo.application.queries import GetSingleTodo
from ..todo.application.repositories import TodosRepository
from ..todo.domain.entities import Todo
from ..todo.domain.value_objects import TodoId

from .repositories import SqlAlchemyTodosRepo


class SqlQuery:
    def __init__(self, repo: TodosRepository) -> None:
        self._repo = repo


class SqlGetSingleTodo(GetSingleTodo, SqlQuery):
    def query(self, todo_id: TodoId) -> Todo:
        return self._repo.get(todo_id)
