from flask import Blueprint, Response, abort, jsonify, make_response, request
import flask_injector
import injector
from todobackend.todo.domain.exceptions import TodoNotFound

from ...todo import (
    TodoId,
    GetSingleTodo,
    GetAllTodos,
    CreateTodoUseCase,
    UpdateTodoUseCase,
    DeleteTodoUseCase,
    DeleteAllTodosUseCase,
    CreateTodoOutputBoundary,
    UpdateTodoOutputBoundary,
    CreateTodoOutputDto,
    UpdateTodoOutputDto,
)
from ..serialization.dto import get_dto

todos_blueprint = Blueprint("todos_blueprint", __name__)


class TodosWeb(injector.Module):
    @injector.provider
    @flask_injector.request
    def create_todo_output_boundary(self) -> CreateTodoOutputBoundary:
        return CreateTodoPresenter()

    @injector.provider
    @flask_injector.request
    def update_todo_output_boundary(self) -> UpdateTodoOutputBoundary:
        return UpdateTodoPresenter()


@todos_blueprint.route("/", methods=["POST"])
def create_todo(create_todo_uc: CreateTodoUseCase, presenter: CreateTodoOutputBoundary) -> Response:
    dto = get_dto(request, CreateTodoUseCase.InputDto, context={})

    create_todo_uc.execute(dto)
    return presenter.response  # type: ignore


class CreateTodoPresenter(CreateTodoOutputBoundary):
    response: Response

    def present(self, output_dto: CreateTodoOutputDto) -> None:
        message = {
            "id": output_dto.created_todo.id,
            "title": output_dto.created_todo.title,
        }
        self.response = make_response(jsonify(message))


@todos_blueprint.route("/<string:todo_id>", methods=["PATCH"])
def update_todo(todo_id: TodoId, update_todo_uc: UpdateTodoUseCase, presenter: UpdateTodoOutputBoundary) -> Response:
    dto = get_dto(request, UpdateTodoUseCase.InputDto, context={"id": todo_id})

    update_todo_uc.execute(dto)
    return presenter.response  # type: ignore


class UpdateTodoPresenter(UpdateTodoOutputBoundary):
    response: Response

    def present(self, output_dto: UpdateTodoOutputDto) -> None:
        message = {
            "id": output_dto.updated_todo.id,
            "title": output_dto.updated_todo.title,
            "order": output_dto.updated_todo.order,
            "completed": output_dto.updated_todo.completed,
        }
        self.response = make_response(jsonify(message))


@todos_blueprint.route("/<string:todo_id>", methods=["DELETE"])
def delete_todo(todo_id: TodoId, delete_todo_uc: DeleteTodoUseCase) -> Response:
    dto = get_dto(request, DeleteTodoUseCase.InputDto, context={"todo_id": todo_id})

    delete_todo_uc.execute(dto)
    return '', 204


@todos_blueprint.route("/<string:todo_id>")
def single_todo(todo_id: TodoId, query: GetSingleTodo) -> Response:
    try:
        return make_response(jsonify(query.query(todo_id)))
    except TodoNotFound:
        return '', 404


@todos_blueprint.route("/")
def all_todos(query: GetAllTodos) -> Response:
    return make_response(jsonify(query.query()))


@todos_blueprint.route("/", methods=["DELETE"])
def delete_all_todos(delete_all_todos_uc: DeleteAllTodosUseCase) -> Response:
    delete_all_todos_uc.execute()
    return '', 200
