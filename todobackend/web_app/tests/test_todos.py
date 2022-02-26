from faker import Faker
from flask.testing import FlaskClient
import injector
import pytest


def test_create_get_then_delete_todo(client: FlaskClient) -> None:
    # create
    title = Faker().name()
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


def test_get_all_todos(client: FlaskClient) -> None:
    # no todo at first
    response = client.get(f"/")

    assert response.status_code == 200
    assert len(response.json) == 0

    # create one
    title = Faker().name()
    response = client.post(f"/", json={"title": title})

    # one todo now
    response = client.get(f"/")

    assert response.status_code == 200
    assert len(response.json) == 1

    # create another two
    title = Faker().name()
    response = client.post(f"/", json={"title": title})
    title = Faker().name()
    response = client.post(f"/", json={"title": title})

    # three todos now
    response = client.get(f"/")

    assert response.status_code == 200
    assert len(response.json) == 3
