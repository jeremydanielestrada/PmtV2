import os

os.environ.setdefault("DATABASE_URL", "sqlite+pysqlite:///:memory:")
os.environ.setdefault("SECRET_KEY", "test-secret-key")

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_openapi_schema_is_available():
    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert response.json()["info"]["title"] == "FastAPI"

    print("Succes")
    