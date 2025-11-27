import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_read_main(client):
    """Test the root endpoint returns 200 and correct structure."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "version": "1.0.0"}


def test_addition_logic(client):
    """Test the math endpoint to ensure logic holds."""
    response = client.get("/add/5/10")
    assert response.status_code == 200
    assert response.get_json() == {"result": 15}


def test_invalid_input(client):
    """Test that sending text instead of integers results in 404 (Flask behavior)."""
    response = client.get("/add/five/ten")
    assert response.status_code == 404
 
