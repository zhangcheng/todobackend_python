from typing import Type, TypeVar, cast

from flask import Request, abort, jsonify, make_response
from marshmallow import Schema, exceptions
from marshmallow_dataclass import class_schema


TDto = TypeVar("TDto")


def get_dto(request: Request, dto_cls: Type[TDto], context: dict) -> TDto:
    schema_cls = class_schema(dto_cls)
    schema = schema_cls()
    try:
        return cast(TDto, schema.load(dict(context, **request.json)))
    except exceptions.ValidationError as exc:
        abort(make_response(jsonify(exc.messages), 400))
