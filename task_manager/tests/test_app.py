from task_manager import app

def test_index():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
def test_app_exists():
    assert app