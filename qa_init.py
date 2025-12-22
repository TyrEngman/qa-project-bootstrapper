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

SAMPLE_TEST_API = dedent(
    """
    import pytest

    from tests.utils.api_client import ApiClient


    @pytest.mark.smoke
    @pytest.mark.api
    def test_healthcheck_endpoint_returns_200():
        \"\"\"Example API smoke test using ApiClient.

        By default it hits https://httpbin.org/status/200.
        You can change the base URL via the API_BASE_URL env var.
        \"\"\"
        client = ApiClient()
        response = client.get("/status/200")

        assert response.status_code == 200
    """
).strip() + "\n"

SAMPLE_TEST_UI = dedent(
    """
    import pytest


    @pytest.mark.smoke
    @pytest.mark.ui
    def test_ui_sample_placeholder():
        \"\"\"UI smoke placeholder.

        Wire this into Playwright (page fixture, locators, etc.)
        to turn it into a real UI test.
        \"\"\"
        assert True
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
    import os
    from typing import Any, Dict, Optional

    import requests


    class ApiClient:
        \"\"\"Small helper to call HTTP endpoints in tests.

        Defaults to https://httpbin.org, but you can override the base URL
        via the environment variable API_BASE_URL.
        \"\"\"

        def __init__(self, base_url: Optional[str] = None, timeout: int = 10) -> None:
            self.base_url = base_url or os.getenv("API_BASE_URL", "https://httpbin.org")
            self.timeout = timeout

        def _build_url(self, path: str) -> str:
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

    print(f"\n🚀 Creating project at: {base_path.resolve()}")
    print(f"   Preset: {preset}")
    print(f"   CI workflow: {'ENABLED' if with_ci else 'DISABLED'}\n")

    # --- Folders según preset ---
    if preset == "minimal":
        folders = [
            "tests",
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

    # Crear carpetas
    for folder in folders:
        folder_path = base_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"📁 Folder created: {folder_path}")

    # --- Elegir contenido según preset ---
    if preset == "api":
        readme_content = README_API
        requirements_content = REQUIREMENTS_API
        test_sample_content = SAMPLE_TEST_API
    elif preset == "ui":
        readme_content = README_UI
        requirements_content = REQUIREMENTS_UI
        test_sample_content = SAMPLE_TEST_UI
    elif preset == "minimal":
        readme_content = README_MINIMAL
        requirements_content = REQUIREMENTS_MINIMAL
        test_sample_content = SAMPLE_TEST_MINIMAL
    else:
        readme_content = README_DEFAULT
        requirements_content = REQUIREMENTS_DEFAULT
        test_sample_content = SAMPLE_TEST_DEFAULT

    # --- Archivos base compartidos ---
    files: dict[str, str] = {
        "tests/__init__.py": "",
        "README.md": readme_content,
        "pytest.ini": PYTEST_INI_CONTENT,
        "requirements.txt": requirements_content,
        "tests/test_sample.py": test_sample_content,
    }

    # Archivos extra por preset
    if preset == "api":
        files["tests/utils/__init__.py"] = ""
        files["tests/utils/api_client.py"] = API_CLIENT_CONTENT

    # CI workflow
    if with_ci:
        files[".github/workflows/ci.yml"] = CI_WORKFLOW_CONTENT

    # Crear archivos
    for rel_path, content in files.items():
        full_path = base_path / rel_path
        full_path.parent.mkdir(parents=True, exist_ok=True)

        with full_path.open("w", encoding="utf-8") as f:
            f.write(content)

        print(f"📄 File created: {full_path}")

    # --- Mensaje final ---
    print("\n🎉 Project created successfully!")
    print("\nNext steps (Windows / PowerShell):")
    print(f"  cd {project_name}")
    print("  python -m venv .venv")
    print("  .venv\\Scripts\\activate")
    print("  pip install -r requirements.txt")
    print("  pytest -v\n")


if __name__ == "__main__":
    args = parse_args()

    project_name = (args.project_name or "").strip()
    if not project_name:
        project_name = input("Enter a name for your new QA project: ").strip()

    if not project_name:
        print("❌ ERROR: project name cannot be empty.")
    else:
        create_structure(project_name, preset=args.preset, with_ci=not args.no_ci)
