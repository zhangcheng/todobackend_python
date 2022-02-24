from sqlalchemy.engine import Connection

from ..todo.application.repositories import TodosRepository
from ..todo.domain.entities import Todo
from ..todo.domain.value_objects import TodoId

from .models import todos


class SqlAlchemyTodosRepo(TodosRepository):
    def __init__(self, connection: Connection) -> None:
        self._conn = connection

    def save(self, todo: Todo) -> None:
        raw_todo = {
            "id": todo.id,
            "title": todo.title,
        }
        update_result = self._conn.execute(
            todos.update(values=raw_todo, whereclause=todos.c.id == todo.id)
        )
        if update_result.rowcount != 1:
            self._conn.execute(todos.insert(values=dict(raw_todo, id=todo.id)))

    def delete(self, todo_id: TodoId) -> None: ...
