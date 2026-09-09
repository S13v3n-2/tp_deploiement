import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "app"))

import pytest
from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data


def test_healthcheck_returns_200_and_healthy_status(client):
    response = client.get("/healthcheck")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_unknown_route_returns_404(client):
    response = client.get("/does-not-exist")
    assert response.status_code == 404
