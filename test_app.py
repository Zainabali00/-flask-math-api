import pytest
from app import app


@pytest.fixture
def client():
    """Creates a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_add_valid(client):
    response = client.get('/add?a=5&b=10')
    assert response.status_code == 200
    assert response.get_json() == {"result": 15}


def test_add_invalid(client):
    response = client.get('/add?a=abc&b=10')
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_subtract_valid(client):
    response = client.get('/subtract?a=20&b=3')
    assert response.status_code == 200
    assert response.get_json() == {"result": 17}


def test_subtract_invalid(client):
    response = client.get('/subtract?a=20&b=xyz')
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_multiply_valid(client):
    response = client.get('/multiply?a=4&b=6')
    assert response.status_code == 200
    assert response.get_json() == {"result": 24}


def test_multiply_invalid(client):
    response = client.get('/multiply?a=4&b=none')
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_divide_valid(client):
    response = client.get('/divide?a=30&b=5')
    assert response.status_code == 200
    assert response.get_json() == {"result": 6}


def test_divide_by_zero(client):
    response = client.get('/divide?a=10&b=0')
    assert response.status_code == 400
    assert response.get_json() == {"error": "Division by zero is not allowed"}


def test_divide_invalid(client):
    response = client.get('/divide?a=xyz&b=5')
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_health_check(client):
    response = client.get('/healthz')
    assert response.status_code == 200
    assert "status" in response.get_json()
    assert response.get_json()["status"] == "healthy"
