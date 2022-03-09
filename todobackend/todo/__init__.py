import injector

from .application.queries import GetSingleTodo, GetAllTodos
from .application.repositories import TodosRepository
from .application.use_cases import (
    CreateTodoOutputBoundary,
    UpdateTodoOutputBoundary,
    CreateTodoOutputDto,
    UpdateTodoOutputDto,
    CreateTodoUseCase,
    UpdateTodoUseCase,
    DeleteTodoUseCase,
    DeleteAllTodosUseCase,
)
from .domain.entities import Todo
from .domain.value_objects import TodoId

__all__ = [
    # module
    "Todos",
    # entities
    "Todo",
    # value objects
    "TodoId",
    # repositories
    "TodosRepository",
    # queries
    "GetSingleTodo",
    "GetAllTodos",
    # use cases
    "CreateTodoUseCase",
    "UpdateTodoUseCase",
    "DeleteTodoUseCase",
    "DeleteAllTodosUseCase",
    "CreateTodoOutputBoundary",
    "UpdateTodoOutputBoundary",
    # input dtos are inner class of uc
    # output dtos
    "CreateTodoOutputDto",
    "UpdateTodoOutputDto",
]


class Todos(injector.Module):
    @injector.provider
    def create_todo_uc(
        self, boundary: CreateTodoOutputBoundary, repo: TodosRepository
    ) -> CreateTodoUseCase:
        return CreateTodoUseCase(boundary, repo)

    @injector.provider
    def update_todo_uc(
        self, boundary: UpdateTodoOutputBoundary, repo: TodosRepository
    ) -> UpdateTodoUseCase:
        return UpdateTodoUseCase(boundary, repo)

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
