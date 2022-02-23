import abc

from ..domain.entities import Todo
from ..domain.value_objects import TodoId


class TodosRepository(abc.ABC):
    # @abc.abstractmethod
    # def get(self, todo_id: TodoId) -> Todo:
    #     pass

    @abc.abstractmethod
    def save(self, todo: Todo) -> None:
        pass
