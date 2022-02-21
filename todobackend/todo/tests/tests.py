from unittest.mock import Mock
import pytest

from ..application.use_cases import CreateTodoUseCase
from ..domain.entities import Todo

def test_saves_todo(
    create_todo_uc: CreateTodoUseCase, todos_repo_mock: Mock, todo: Todo, input_dto: CreateTodoUseCase.InputDto
) -> None:
    create_todo_uc.execute(input_dto)

    todos_repo_mock.save.assert_called_once()
