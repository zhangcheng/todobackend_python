from faker import Faker
from flask.testing import FlaskClient
import injector
import pytest


def test_create_get_then_delete_todo(client: FlaskClient) -> None:
    title = Faker().name()

    # create
    response = client.post(f"/", json={"title": title})

    assert response.status_code == 200
    assert response.json["title"] == title
    assert "id" in response.json
    todo_id = response.json['id']

    # get
    response = client.get(f"/{todo_id}")

    assert response.status_code == 200

    # delete
    response = client.delete(f"/{todo_id}")

    assert response.status_code == 204

    # get
    response = client.get(f"/{todo_id}")

    assert response.status_code == 404
