import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    """Fixture for creating a test client."""
    return TestClient(app)