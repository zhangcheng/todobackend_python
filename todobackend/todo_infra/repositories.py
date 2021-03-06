from typing import List
from sqlalchemy.engine import Connection, RowProxy

from ..todo.application.repositories import TodosRepository
from ..todo.domain.entities import Todo
from ..todo.domain.exceptions import TodoNotFound
from ..todo.domain.value_objects import TodoId

from .models import todos


class SqlAlchemyTodosRepo(TodosRepository):
    def __init__(self, connection: Connection) -> None:
        self._conn = connection

    def save(self, todo: Todo) -> None:
        raw_todo = {
            "id": todo.id,
            "title": todo.title,
            "order": todo.order,
            "completed": todo.completed,
        }
        update_result = self._conn.execute(
            todos.update(values=raw_todo, whereclause=todos.c.id == todo.id)
        )
        if update_result.rowcount != 1:
            self._conn.execute(todos.insert(values=dict(raw_todo, id=todo.id)))

    def delete(self, todo_id: TodoId) -> None:
        delete_result = self._conn.execute(
            todos.delete().where(todos.c.id == todo_id)
        )

    def delete_all(self) -> None:
        delete_result = self._conn.execute(
            todos.delete()
        )

    def get(self, todo_id: TodoId) -> Todo:
        row = self._conn.execute(todos.select().where(todos.c.id == todo_id)).first()
        if not row:
            raise TodoNotFound

        return self._row_to_dto(row)

    def get_all(self) -> List[Todo]:
        return [
            self._row_to_dto(row) for row in self._conn.execute(todos.select())
        ]

    def _row_to_dto(self, row: RowProxy) -> Todo:
        return Todo(
            id=row.id,
            title=row.title,
            order=row.order,
            completed=row.completed,
        )
