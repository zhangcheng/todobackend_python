import injector

from .application.repositories import TodosRepository
from .application.use_cases import CreateTodoOutputBoundary, CreateTodoUseCase
from .domain.value_objects import TodoId

__all__ = [
    # module
    "Todos",
    # value objects
    "TodoId",
    # repositories
    "TodosRepository",
    # use cases
    "CreateTodoUseCase",
    # input dtos are inner class of uc
    # output dtos
    "CreateTodoOutputDto",
]


class Todos(injector.Module):
    @injector.provider
    def create_todo_uc(self, boundary: CreateTodoOutputBoundary, repo: TodosRepository) -> CreateTodoUseCase:
        return CreateTodoUseCase(boundary, repo)
