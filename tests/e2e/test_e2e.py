import os
import requests

BASE_URL = os.environ.get("BASE_URL", "http://localhost:8080")


def test_app_is_available():
    response = requests.get(f"{BASE_URL}/healthcheck", timeout=10)
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_home_page_served_through_nginx():
    response = requests.get(f"{BASE_URL}/", timeout=10)
    assert response.status_code == 200
    assert "Hello" in response.text
