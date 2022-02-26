import abc
from typing import List

from ..domain.entities import Todo
from ..domain.value_objects import TodoId


class GetSingleTodo(abc.ABC):
    @abc.abstractmethod
    def query(self, todo_id: TodoId) -> Todo:
        pass


class GetAllTodos(abc.ABC):
    @abc.abstractmethod
    def query(self) -> List[Todo]:
        pass
