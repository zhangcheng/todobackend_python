from faker import Faker
from flask.testing import FlaskClient
import injector
import pytest


def test_create_then_delete_todo(client: FlaskClient) -> None:
    title = Faker().name()
    response = client.post(f"/", json={"title": title})

    assert response.status_code == 200
    assert response.json["title"] == title
    assert "id" in response.json

    response = client.delete(f"/{response.json['id']}")

    assert response.status_code == 204
