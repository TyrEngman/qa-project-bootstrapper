from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


# --------------------------------------------------------------------
# Rutas base
# --------------------------------------------------------------------
BASE_DIR = Path(__file__).parent
PROJECT_TEMPLATES_DIR = BASE_DIR / "templates" / "project"


def _load_template(path: Path, fallback: str) -> str:
    """Lee un archivo de plantilla si existe; si no, devuelve un fallback."""
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return fallback


# --------------------------------------------------------------------
# Plantillas de README por preset
# --------------------------------------------------------------------
README_DEFAULT = _load_template(
    PROJECT_TEMPLATES_DIR / "README_PROJECT.md",
    "# QA Starter Project\n\nGenerated with qa-project-bootstrapper (default preset).\n",
)

README_API = _load_template(
    PROJECT_TEMPLATES_DIR / "api" / "README_API_PROJECT.md",
    "# QA API Project\n\nGenerated with qa-project-bootstrapper (api preset).\n",
)

README_UI = _load_template(
    PROJECT_TEMPLATES_DIR / "ui" / "README_UI_PROJECT.md",
    "# QA UI Project\n\nGenerated with qa-project-bootstrapper (ui preset).\n",
)

README_MINIMAL = _load_template(
    PROJECT_TEMPLATES_DIR / "minimal" / "README_MINIMAL_PROJECT.md",
    "# QA Minimal Pytest Project\n\nGenerated with qa-project-bootstrapper (minimal preset).\n",
)

# --------------------------------------------------------------------
# Plantilla de pytest.ini
# --------------------------------------------------------------------
PYTEST_INI_CONTENT = _load_template(
    PROJECT_TEMPLATES_DIR / "pytest.ini",
    dedent(
        """
        [pytest]
        addopts = -v
        markers =
            smoke: smoke tests
            api: api tests
            ui: ui tests
        """
    ).strip()
    + "\n",
)

# --------------------------------------------------------------------
# Plantilla de CI (GitHub Actions)
# --------------------------------------------------------------------
CI_WORKFLOW_CONTENT = _load_template(
    PROJECT_TEMPLATES_DIR / ".github" / "workflows" / "ci.yml",
    dedent(
        """
        name: CI

        on:
          push:
            branches: [ "main" ]
          pull_request:

        jobs:
          test:
            runs-on: ubuntu-latest
            steps:
              - uses: actions/checkout@v4
              - uses: actions/setup-python@v5
                with:
                  python-version: "3.10"
              - run: pip install -r requirements.txt
              - run: pytest -v
        """
    ).strip()
    + "\n",
)

# --------------------------------------------------------------------
# Requisitos por preset
# --------------------------------------------------------------------
REQUIREMENTS_DEFAULT = dedent(
    """
    pytest
    pytest-html
    pytest-metadata
    pytest-base-url
    pytest-playwright
    requests
    """
).strip() + "\n"

REQUIREMENTS_API = dedent(
    """
    pytest
    requests
    """
).strip() + "\n"

REQUIREMENTS_UI = dedent(
    """
    pytest
    playwright
    pytest-playwright
    pytest-html
    pytest-metadata
    pytest-base-url
    """
).strip() + "\n"

REQUIREMENTS_MINIMAL = dedent(
    """
    pytest
    """
).strip() + "\n"

# --------------------------------------------------------------------
# Tests de ejemplo
# --------------------------------------------------------------------
SAMPLE_TEST_DEFAULT = dedent(
    """
    import pytest


    @pytest.mark.smoke
    def test_sample_smoke_check():
        \"\"\"Basic smoke test placeholder.

        Replace this test with something that matches your real feature.
        \"\"\"
        assert True
    """
).strip() + "\n"

# --------------------------------------------------------------------
# API PRESET: OFFLINE (sin internet)  ✅ CORREGIDO
# --------------------------------------------------------------------
SAMPLE_TEST_API = dedent(
    """
    import threading
    from http.server import BaseHTTPRequestHandler, HTTPServer

    import pytest

    from tests.utils.api_client import ApiClient


    class _Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/status/200":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(b'{"status":"ok"}')
                return

            self.send_response(404)
            self.end_headers()

        def log_message(self, format, *args):
            # Silence server logs during tests
            return


    @pytest.fixture()
    def local_server_base_url():
        server = HTTPServer(("127.0.0.1", 0), _Handler)
        host, port = server.server_address
        base_url = f"http://{host}:{port}"

        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()

        try:
            yield base_url
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)


    @pytest.mark.smoke
    @pytest.mark.api
    def test_healthcheck_offline_returns_200(local_server_base_url):
        \"\"\"Offline API smoke test.

        It starts a local HTTP server and calls /status/200.
        No internet required, stable in CI.
        \"\"\"
        client = ApiClient(base_url=local_server_base_url)
        response = client.get("/status/200")

        assert response.status_code == 200
    """
).strip() + "\n"

UI_BASE_PAGE = dedent(
    """
    from playwright.sync_api import Page


    class BasePage:
        def __init__(self, page: Page):
            self.page = page

        def open(self, url: str) -> None:
            self.page.goto(url, wait_until="domcontentloaded")
    """
).strip() + "\n"

UI_EXAMPLE_PAGE = dedent(
    """
    from playwright.sync_api import expect
    from .base_page import BasePage


    class ExamplePage(BasePage):
        URL = "https://example.com/"

        def open_default(self) -> None:
            self.open(self.URL)

        def expect_title(self) -> None:
            expect(self.page).to_have_title("Example Domain")
    """
).strip() + "\n"

UI_TEST_EXAMPLE = dedent(
    """
    import pytest

    from tests.ui.pages.example_page import ExamplePage


    @pytest.mark.smoke
    @pytest.mark.ui
    def test_example_domain_title(page):
        p = ExamplePage(page)
        p.open_default()
        p.expect_title()
    """
).strip() + "\n"

SAMPLE_TEST_MINIMAL = dedent(
    """
    import pytest


    @pytest.mark.smoke
    def test_example():
        \"\"\"Ultra-minimal example test.

        Feel free to delete this file and start fresh.
        \"\"\"
        assert 1 + 1 == 2
    """
).strip() + "\n"

# --------------------------------------------------------------------
# ApiClient para preset API
# --------------------------------------------------------------------
API_CLIENT_CONTENT = dedent(
    """
    from typing import Any, Dict, Optional

    import requests


    class ApiClient:
        \"\"\"Small helper to call HTTP endpoints in tests.

        You can pass base_url directly (recommended), or set API_BASE_URL env var.
        \"\"\"

        def __init__(self, base_url: Optional[str] = None, timeout: int = 10) -> None:
            self.base_url = base_url
            self.timeout = timeout

        def _build_url(self, path: str) -> str:
            if not self.base_url:
                raise ValueError("ApiClient.base_url is required. Pass base_url explicitly.")
            return self.base_url.rstrip("/") + "/" + path.lstrip("/")

        def get(self, path: str, **kwargs: Dict[str, Any]) -> requests.Response:
            url = self._build_url(path)
            return requests.get(url, timeout=self.timeout, **kwargs)
    """
).strip() + "\n"


# --------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Bootstrap a QA automation project (pytest-based)."
    )

    parser.add_argument(
        "project_name",
        nargs="?",
        help="Name of the folder to create for your new QA project.",
    )

    parser.add_argument(
        "--preset",
        choices=["default", "api", "ui", "minimal"],
        default="default",
        help="Project template to use (default, api, ui, minimal).",
    )

    parser.add_argument(
        "--no-ci",
        action="store_true",
        help="Do not create the GitHub Actions CI workflow.",
    )

    return parser.parse_args()


# --------------------------------------------------------------------
# Core
# --------------------------------------------------------------------
def create_structure(project_name: str, preset: str, with_ci: bool = True) -> None:
    base_path = Path(project_name)

    print(f"Creating project at: {base_path.resolve()}")
    print(f"Preset: {preset}")
    print(f"CI workflow: {'ENABLED' if with_ci else 'DISABLED'}\n")

    if preset == "minimal":
        folders = ["tests"]
    elif preset == "ui":
        folders = [
            "tests",
            "tests/ui",
            "tests/ui/pages",
            "tests/data",
            "tests/utils",
        ]
    else:
        folders = [
            "tests",
            "tests/pages",
            "tests/data",
            "tests/utils",
        ]

    if with_ci:
        folders.append(".github/workflows")

    for folder in folders:
        folder_path = base_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Folder created: {folder_path}")

    if preset == "api":
        readme_content = README_API
        requirements_content = REQUIREMENTS_API
    elif preset == "ui":
        readme_content = README_UI
        requirements_content = REQUIREMENTS_UI
    elif preset == "minimal":
        readme_content = README_MINIMAL
        requirements_content = REQUIREMENTS_MINIMAL
    else:
        readme_content = README_DEFAULT
        requirements_content = REQUIREMENTS_DEFAULT

    files: dict[str, str] = {
        "README.md": readme_content,
        "pytest.ini": PYTEST_INI_CONTENT,
        "requirements.txt": requirements_content,
        "tests/__init__.py": "",
    }

    if preset == "api":
        files["tests/utils/__init__.py"] = ""
        files["tests/utils/api_client.py"] = API_CLIENT_CONTENT
        files["tests/test_sample.py"] = SAMPLE_TEST_API

    elif preset == "ui":
        files["tests/ui/__init__.py"] = ""
        files["tests/ui/pages/__init__.py"] = ""
        files["tests/ui/pages/base_page.py"] = UI_BASE_PAGE
        files["tests/ui/pages/example_page.py"] = UI_EXAMPLE_PAGE
        files["tests/ui/test_example_ui.py"] = UI_TEST_EXAMPLE

    elif preset == "minimal":
        files["tests/test_sample.py"] = SAMPLE_TEST_MINIMAL

    else:
        files["tests/test_sample.py"] = SAMPLE_TEST_DEFAULT
        files["tests/pages/__init__.py"] = ""
        files["tests/data/__init__.py"] = ""
        files["tests/utils/__init__.py"] = ""

    if with_ci:
        files[".github/workflows/ci.yml"] = CI_WORKFLOW_CONTENT

    for rel_path, content in files.items():
        full_path = base_path / rel_path
        full_path.parent.mkdir(parents=True, exist_ok=True)

        with full_path.open("w", encoding="utf-8") as f:
            f.write(content)

        print(f"File created: {full_path}")

    print("\nProject created successfully!")
    print("\nNext steps (Windows / PowerShell):")
    print(f"cd {project_name}")
    print("python -m venv .venv")
    print(".venv\\Scripts\\activate")
    print("pip install -r requirements.txt")
    if preset == "ui":
        print("python -m playwright install")
    print("pytest -v\n")


if __name__ == "__main__":
    args = parse_args()

    project_name = (args.project_name or "").strip()
    if not project_name:
        project_name = input("Enter a name for your new QA project: ").strip()

    if not project_name:
        print("ERROR: project name cannot be empty.")
    else:
        create_structure(project_name, preset=args.preset, with_ci=not args.no_ci)
