from flask import Blueprint, Response, abort, jsonify, make_response, request
import flask_injector
import injector

from ...todo import (
    TodoId,
    GetSingleTodo,
    GetAllTodos,
    CreateTodoUseCase,
    DeleteTodoUseCase,
    CreateTodoOutputBoundary,
    CreateTodoOutputDto,
)
from ..serialization.dto import get_dto

todos_blueprint = Blueprint("todos_blueprint", __name__)


class TodosWeb(injector.Module):
    @injector.provider
    @flask_injector.request
    def create_todo_output_boundary(self) -> CreateTodoOutputBoundary:
        return CreateTodoPresenter()


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


@todos_blueprint.route("/<string:todo_id>", methods=["DELETE"])
def delete_todo(todo_id: TodoId, delete_todo_uc: DeleteTodoUseCase) -> Response:
    dto = get_dto(request, DeleteTodoUseCase.InputDto, context={"todo_id": todo_id})

    delete_todo_uc.execute(dto)
    return '', 204


@todos_blueprint.route("/<string:todo_id>")
def single_todo(todo_id: TodoId, query: GetSingleTodo) -> Response:
    try:
        return make_response(jsonify(query.query(todo_id)))
    except:
        return '', 404


@todos_blueprint.route("/")
def all_todos(query: GetAllTodos) -> Response:
    return make_response(jsonify(query.query()))
