from unittest.mock import Mock
import pytest

from ..application.use_cases import CreateTodoUseCase, DeleteTodoUseCase
from ..domain.entities import Todo

def test_saves_todo(
    create_todo_uc: CreateTodoUseCase, todos_repo_mock: Mock, create_todo_output_boundary_mock: Mock, create_todo_input_dto: CreateTodoUseCase.InputDto
) -> None:
    create_todo_uc.execute(create_todo_input_dto)

    todos_repo_mock.save.assert_called_once()
    create_todo_output_boundary_mock.present.assert_called_once()


def test_delete_todo(
    delete_todo_uc: DeleteTodoUseCase, todos_repo_mock: Mock, delete_todo_input_dto: DeleteTodoUseCase.InputDto
) -> None:
    delete_todo_uc.execute(delete_todo_input_dto)

    todos_repo_mock.delete.assert_called_once()
