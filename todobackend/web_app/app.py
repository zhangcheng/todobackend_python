from typing import Optional

from flask import Flask, Response, request
from flask_cors import CORS
from flask_injector import FlaskInjector
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session

from ..main import bootstrap_app
from ..main.modules import RequestScope
from .blueprints.todos import TodosWeb, todos_blueprint
from .blueprints.smorest import ApiModule, provide_ext


def create_app(settings_override: Optional[dict] = None) -> Flask:
    if settings_override is None:
        settings_override = {}

    app = Flask(__name__)
    CORS(app, resources=r'/*', allow_headers="Content-Type")

    app.register_blueprint(todos_blueprint, url_prefix="/")
    provide_ext(app)

    # TODO: move this config
    app.config["SECRET_KEY"] = "super-secret"
    app.config["DEBUG"] = True
    for key, value in settings_override.items():
        app.config[key] = value

    print("bootstrap_app()")
    app_context = bootstrap_app()
    FlaskInjector(app, modules=[TodosWeb(), ApiModule], injector=app_context.injector)
    app.injector = app_context.injector

    @app.before_request
    def transaction_start() -> None:
        app_context.injector.get(RequestScope).enter()

        request.connection = app_context.injector.get(Connection)  # type: ignore
        request.tx = request.connection.begin()  # type: ignore
        request.session = app_context.injector.get(Session)  # type: ignore

    @app.after_request
    def transaction_commit(response: Response) -> Response:
        scope = app_context.injector.get(RequestScope)
        try:
            if hasattr(request, "tx") and response.status_code < 400:
                request.tx.commit()  # type: ignore
        finally:
            scope.exit()

        return response

    @app.after_request
    def add_cors_headers(response: Response) -> Response:
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "*"
        return response

    return app
