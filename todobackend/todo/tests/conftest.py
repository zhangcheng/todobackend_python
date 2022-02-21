from unittest.mock import Mock
import pytest

from ..application.use_cases import CreateTodoUseCase, CreateTodoOutputBoundary
from ..application.repositories import TodosRepository
from ..domain.entities import Todo
from ..domain.value_objects import TodoId


@pytest.fixture()
def title() -> str:
    return "todo title"


@pytest.fixture()
def input_dto(title: str) -> CreateTodoUseCase.InputDto:
    return CreateTodoUseCase.InputDto(title)


@pytest.fixture()
def todo() -> Todo:
    return Todo("id", "title")


@pytest.fixture()
def todos_repo_mock(todo: Todo) -> Mock:
    return Mock(spec_set=TodosRepository, get=Mock(return_value=todo))


@pytest.fixture()
def create_todo_output_boundary_mock() -> Mock:
    return Mock(spec_set=CreateTodoOutputBoundary)


@pytest.fixture()
def create_todo_uc(create_todo_output_boundary_mock: Mock, todos_repo_mock: Mock) -> CreateTodoUseCase:
    return CreateTodoUseCase(create_todo_output_boundary_mock, todos_repo_mock)
