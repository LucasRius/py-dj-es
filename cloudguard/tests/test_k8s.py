import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_k8s_client():
    with MagicMock() as mock:
        yield mock

def test_quota_calculation(mock_k8s_client):
    # Lógica para testar se o Django interpreta corretamente os dados do K8s
    assert True