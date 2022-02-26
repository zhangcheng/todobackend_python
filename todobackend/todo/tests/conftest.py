from unittest.mock import Mock
import pytest

from ..application.use_cases import CreateTodoUseCase, CreateTodoOutputBoundary, DeleteTodoUseCase, DeleteAllTodosUseCase
from ..application.repositories import TodosRepository
from ..domain.entities import Todo
from ..domain.value_objects import TodoId


@pytest.fixture()
def title() -> str:
    return "todo title"


@pytest.fixture()
def todo() -> Todo:
    return Todo(id="id", title="title", order=0)


@pytest.fixture()
def todo_id() -> TodoId:
    return "todo id"


@pytest.fixture()
def todos_repo_mock(todo: Todo) -> Mock:
    return Mock(spec_set=TodosRepository)


@pytest.fixture()
def create_todo_input_dto(title: str) -> CreateTodoUseCase.InputDto:
    return CreateTodoUseCase.InputDto(title=title, order=1)


@pytest.fixture()
def create_todo_output_boundary_mock() -> Mock:
    return Mock(spec_set=CreateTodoOutputBoundary)


@pytest.fixture()
def create_todo_uc(create_todo_output_boundary_mock: Mock, todos_repo_mock: Mock) -> CreateTodoUseCase:
    return CreateTodoUseCase(create_todo_output_boundary_mock, todos_repo_mock)


@pytest.fixture()
def delete_todo_input_dto(todo_id: TodoId) -> DeleteTodoUseCase.InputDto:
    return DeleteTodoUseCase.InputDto(todo_id)


@pytest.fixture()
def delete_todo_uc(todos_repo_mock: Mock) -> DeleteTodoUseCase:
    return DeleteTodoUseCase(todos_repo_mock)


@pytest.fixture()
def delete_all_todos_uc(todos_repo_mock: Mock) -> DeleteAllTodosUseCase:
    return DeleteAllTodosUseCase(todos_repo_mock)
