import os
import requests


class ApiClient:
    """Very small HTTP api client using requests.

    This is only a starting point. Extend it with auth, headers,
    logging, retries, etc., depending on your needs.
    """

    def __init__(self, base_url: str | None = None) -> None:
        # You can override the base URL via the API_BASE_URL env var
        self.base_url = base_url or os.getenv("API_BASE_URL", "https://httpbin.org")

    def _build_url(self, path: str) -> str:
        if not path.startswith("/"):
            path = "/" + path
        return f"{self.base_url}{path}"

    def get(self, path: str, **kwargs):
        return requests.get(self._build_url(path), **kwargs)

    def post(self, path: str, **kwargs):
        return requests.post(self._build_url(path), **kwargs)
