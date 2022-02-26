import injector

from .application.queries import GetSingleTodo, GetAllTodos
from .application.repositories import TodosRepository
from .application.use_cases import (
    CreateTodoOutputBoundary,
    CreateTodoOutputDto,
    CreateTodoUseCase,
    DeleteTodoUseCase,
    DeleteAllTodosUseCase,
)
from .domain.value_objects import TodoId

__all__ = [
    # module
    "Todos",
    # value objects
    "TodoId",
    # repositories
    "TodosRepository",
    # queries
    "GetSingleTodo",
    "GetAllTodos",
    # use cases
    "CreateTodoUseCase",
    "DeleteTodoUseCase",
    "DeleteAllTodosUseCase",
    "CreateTodoOutputBoundary",
    # input dtos are inner class of uc
    # output dtos
    "CreateTodoOutputDto",
]


class Todos(injector.Module):
    @injector.provider
    def create_todo_uc(
        self, boundary: CreateTodoOutputBoundary, repo: TodosRepository
    ) -> CreateTodoUseCase:
        return CreateTodoUseCase(boundary, repo)

    @injector.provider
    def delete_todo_uc(
        self, repo: TodosRepository
    ) -> DeleteTodoUseCase:
        return DeleteTodoUseCase(repo)

    @injector.provider
    def delete_all_todos_uc(
        self, repo: TodosRepository
    ) -> DeleteAllTodosUseCase:
        return DeleteAllTodosUseCase(repo)
