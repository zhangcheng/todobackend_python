import flask_injector
import injector

from typing import List
from flask import Flask
from flask.views import MethodView
from flask_smorest import Api, Blueprint, abort
from marshmallow_dataclass import class_schema

from ...todo import (
    Todo,
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


class ApiModule(injector.Module):
    @injector.provider
    @flask_injector.request
    def create_todo_output_boundary(self) -> CreateTodoOutputBoundary:
        return CreateTodoPresenter()

    def configure(self, binder):
        print("ApiModule::configure")
        # binder.bind(Api, to=self.provide_ext(self.app), scope=injector.singleton)


def provide_ext(app: Flask) -> Api:
    print("provide_ext")
    app.config["API_TITLE"] = "My API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_RAPIDOC_PATH"] = "/rapidoc"
    app.config["OPENAPI_RAPIDOC_URL"] = "https://unpkg.com/rapidoc/dist/rapidoc-min.js"
    # app.config[""] = ""
    api = Api(app)
    api.register_blueprint(blp)
    return api

blp = Blueprint("pets", "pets", url_prefix="/pets", description="Operations on pets")


TodoSchema = class_schema(Todo)


class CreateTodoPresenter(CreateTodoOutputBoundary):
    output: Todo

    def present(self, output_dto: CreateTodoOutputDto) -> None:
        self.output = output_dto.created_todo


@blp.route("/")
class Pets(MethodView):
    @injector.inject
    def __init__(
        self,
        query: GetAllTodos,
        create_todo_uc: CreateTodoUseCase,
        presenter: CreateTodoOutputBoundary,
    ):
        self._query = query
        self._uc = create_todo_uc
        self._presenter = presenter

    @blp.response(200, TodoSchema(many=True))
    def get(self) -> List[Todo]:
        """List pets"""
        return self._query.query()

    @blp.arguments(class_schema(CreateTodoUseCase.InputDto))
    @blp.response(201, TodoSchema)
    def post(self, dto):
        self._uc.execute(dto)
        return self._presenter.output  # type: ignore
