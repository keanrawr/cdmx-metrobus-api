import subprocess
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_version():
    poetry_version = subprocess.run(['poetry', 'version', '-s'], stdout=subprocess.PIPE)
    poetry_version = poetry_version.stdout.decode('utf-8').replace('\n', '')

    response = client.get('/version')
    assert response.status_code == 200
    assert response.json() == poetry_version, 'API version and poetry version do not match'


def test_healthcheck():
    response = client.get('/healthcheck')

    assert response.status_code == 200
    assert response.json() == 'ok'
