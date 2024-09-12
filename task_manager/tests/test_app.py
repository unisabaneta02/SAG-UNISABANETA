import pytest
from app import app, db, Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.json == []

def test_add_task(client):
    response = client.post('/tasks', json={'description': 'Test task'})
    assert response.status_code == 201
    assert response.json['description'] == 'Test task'
