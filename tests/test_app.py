import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert "tasks" in response.get_json()

def test_add_task_success(client):
    response = client.post('/tasks', json={"titulo": "Entrega Prioritária Logística", "descricao": "Rota SP"})
    assert response.status_code == 201
    assert response.get_json()["titulo"] == "Entrega Prioritária Logística"

def test_add_task_validation(client):
    response = client.post('/tasks', json={})
    assert response.status_code == 400
