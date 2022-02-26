import injector
from sqlalchemy.engine import Connection

from ..todo.application.queries import GetSingleTodo, GetAllTodos
from ..todo.application.repositories import TodosRepository

from .models import todos, metadata
from .queries import SqlGetSingleTodo, SqlGetAllTodos
from .repositories import SqlAlchemyTodosRepo

__all__ = [
    # module
    "TodosInfra",
    # models
    "metadata",
    "todos",
]


class TodosInfra(injector.Module):
    @injector.provider
    def todos_repo(self, conn: Connection) -> TodosRepository:
        return SqlAlchemyTodosRepo(conn)

    @injector.provider
    def get_single_todo(self, repo: TodosRepository) -> GetSingleTodo:
        return SqlGetSingleTodo(repo)

    @injector.provider
    def get_all_todos(self, repo: TodosRepository) -> GetAllTodos:
        return SqlGetAllTodos(repo)
