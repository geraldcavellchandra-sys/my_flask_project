import pytest
from main import app, SESSIONS


@pytest.fixture
def client():
    app.config["TESTING"] = True
    SESSIONS["logged_in"] = False      # reset login state before each test
    with app.test_client() as client:
        yield client


def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "version": "1.0.0"}


def test_addition_logic(client):
    response = client.get("/add/5/10")
    assert response.status_code == 200
    assert response.get_json() == {"result": 15}


def test_invalid_input(client):
    response = client.get("/add/five/ten")
    assert response.status_code == 404


def test_login_success(client):
    payload = {"username": "admin", "password": "password123"}
    response = client.post("/login", json=payload)

    assert response.status_code == 200
    assert response.get_json()["success"] is True
    assert SESSIONS["logged_in"] is True


def test_login_fail(client):
    payload = {"username": "admin", "password": "wrong"}
    response = client.post("/login", json=payload)

    assert response.status_code == 401
    assert response.get_json()["success"] is False
    assert SESSIONS["logged_in"] is False


def test_subtract_not_logged_in(client):
    response = client.get("/subtract/10/3")
    assert response.status_code == 401
    assert response.get_json() == {"error": "Not authorized"}


def test_subtract_logged_in(client):
    # login first
    login_response = client.post("/login", json={"username": "admin", "password": "password123"})
    assert login_response.status_code == 200

    # now subtract
    response = client.get("/subtract/10/3")
    assert response.status_code == 200
    assert response.get_json() == {"result": 7}
