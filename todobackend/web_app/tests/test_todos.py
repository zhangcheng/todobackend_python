from flask.testing import FlaskClient
import injector
import pytest


def test_create_todo(client: FlaskClient) -> None:
    response = client.post(f"/", json={"title": "pytest"})

    assert response.status_code == 200
    assert response.json == {"message": "Hooray! You are a winner"}
