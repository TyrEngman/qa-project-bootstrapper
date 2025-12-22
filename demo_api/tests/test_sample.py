import pytest
from tests.utils.api_client import ApiClient


@pytest.mark.smoke
@pytest.mark.api
def test_healthcheck_endpoint_returns_200():
    """Example api smoke test using ApiClient.

    By default it hits https://httpbin.org/status/200.
    You can change the base URL via the API_BASE_URL env var.
    """
    # Given
    client = ApiClient()
    path = "/status/200"

    # When
    response = client.get(path)

    # Then
    assert response.status_code == 200
