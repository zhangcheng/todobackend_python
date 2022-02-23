from dataclasses import dataclass
import os

import dotenv
import injector
from sqlalchemy.engine import Connection, Engine, create_engine

from ..todo import Todos
from ..todo_infra import TodosInfra, metadata
from .modules import Db

__all__ = ["bootstrap_app"]


@dataclass
class AppContext:
    injector: injector.Injector


def bootstrap_app() -> AppContext:
    """This is bootstrap function independent from the context.

    This should be used for Web, CLI, or worker context."""
    config_path = os.environ.get(
        "CONFIG_PATH", os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, ".env_file")
    )
    dotenv.load_dotenv(config_path)
    settings = {
        # "redis.host": os.environ["REDIS_HOST"],
    }

    engine = create_engine(os.environ["DB_DSN"])
    dependency_injector = _setup_dependency_injection(settings, engine)

    _create_db_schema(engine)  # TEMPORARY

    return AppContext(dependency_injector)


def _setup_dependency_injection(settings: dict, engine: Engine) -> injector.Injector:
    return injector.Injector(
        [
            Db(engine),
            Todos(),
            TodosInfra(),
        ],
        auto_bind=False,
    )


def _create_db_schema(engine: Engine) -> None:
    # Models has to be imported for metadata.create_all to discover them
    from ..todo_infra import todos  # noqa

    # TODO: Use migrations for that
    metadata.create_all(engine)
