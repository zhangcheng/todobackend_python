import injector
from sqlalchemy.engine import Connection

from ..todo.application.repositories import TodosRepository

from .repositories import SqlAlchemyTodosRepo

__all__ = [
    # module
    "TodosInfra",
    # models
    "todos",
]


class TodosInfra(injector.Module):
    @injector.provider
    def todos_repo(self, conn: Connection) -> TodosRepository:
        return SqlAlchemyTodosRepo(conn)
