from dataclasses import dataclass
from uuid import uuid4

from .repositories import TodosRepository
from ..domain.entities import Todo

class CreateTodoUseCase:
    @dataclass
    class InputDto:
        title: str

    def __init__(self, todos_repo: TodosRepository) -> None:
        self.todos_repo = todos_repo

    def execute(self, input_dto: InputDto) -> None:
        new_todo = Todo(id=uuid4().hex, title=input_dto.title)
        self.todos_repo.save(new_todo)
