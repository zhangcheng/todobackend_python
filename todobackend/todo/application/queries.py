import abc

from ..domain.entities import Todo
from ..domain.value_objects import TodoId


class GetSingleTodo(abc.ABC):
    @abc.abstractmethod
    def query(self, todo_id: TodoId) -> Todo:
        pass
