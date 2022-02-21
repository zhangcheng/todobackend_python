import abc
from dataclasses import dataclass
from uuid import uuid4

from .repositories import TodosRepository
from ..domain.entities import Todo


@dataclass
class CreateTodoOutputDto:
    created_todo: Todo


class CreateTodoOutputBoundary(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def present(self, output_dto: CreateTodoOutputDto) -> None:
        pass


class CreateTodoUseCase:
    @dataclass
    class InputDto:
        title: str

    def __init__(self, output_boundary: CreateTodoOutputBoundary, todos_repo: TodosRepository) -> None:
        self.output_boundary = output_boundary
        self.todos_repo = todos_repo

    def execute(self, input_dto: InputDto) -> None:
        new_todo = Todo(id=uuid4().hex, title=input_dto.title)
        self.todos_repo.save(new_todo)

        output_dto = CreateTodoOutputDto(created_todo=new_todo)
        self.output_boundary.present(output_dto)
