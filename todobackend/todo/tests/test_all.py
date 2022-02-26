from unittest.mock import Mock
import pytest

from ..application.use_cases import CreateTodoUseCase, DeleteTodoUseCase, DeleteAllTodosUseCase
from ..domain.entities import Todo


def test_create_todo(
    create_todo_uc: CreateTodoUseCase, todos_repo_mock: Mock, create_todo_output_boundary_mock: Mock, create_todo_input_dto: CreateTodoUseCase.InputDto
) -> None:
    create_todo_uc.execute(create_todo_input_dto)

    todos_repo_mock.save.assert_called_once()
    create_todo_output_boundary_mock.present.assert_called_once()


def test_update_todo(
    update_todo_uc: DeleteTodoUseCase, todos_repo_mock: Mock, update_todo_output_boundary_mock: Mock, update_todo_input_dto: DeleteTodoUseCase.InputDto
) -> None:
    update_todo_uc.execute(update_todo_input_dto)

    todos_repo_mock.save.assert_called_once()
    update_todo_output_boundary_mock.present.assert_called_once()


def test_delete_todo(
    delete_todo_uc: DeleteTodoUseCase, todos_repo_mock: Mock, delete_todo_input_dto: DeleteTodoUseCase.InputDto
) -> None:
    delete_todo_uc.execute(delete_todo_input_dto)

    todos_repo_mock.delete.assert_called_once()


def test_delete_all_todos(
    delete_all_todos_uc: DeleteAllTodosUseCase, todos_repo_mock: Mock,
) -> None:
    delete_all_todos_uc.execute()

    todos_repo_mock.delete_all.assert_called_once()
