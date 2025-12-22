from pathlib import Path
import argparse

# Base directory of this bootstrapper
BASE_DIR = Path(__file__).parent

# Templates directory
TEMPLATES_DIR = BASE_DIR / "templates"

# Template paths
README_TEMPLATE_PATH = TEMPLATES_DIR / "README_PROJECT.md"
REQUIREMENTS_TEMPLATE_PATH = TEMPLATES_DIR / "requirements.txt"
PYTEST_INI_TEMPLATE_PATH = TEMPLATES_DIR / "pytest.ini"

# Load README template (Markdown) with a fallback if file is missing
try:
    README_TEMPLATE = README_TEMPLATE_PATH.read_text(encoding="utf-8")
except FileNotFoundError:
    README_TEMPLATE = (
        "# QA Automation Starter Project\n\n"
        "Template file 'templates/README_PROJECT.md' was not found.\n"
        "Please add it to customize this README.\n"
    )

# Load requirements template with a fallback
try:
    REQUIREMENTS_TEMPLATE = REQUIREMENTS_TEMPLATE_PATH.read_text(encoding="utf-8")
except FileNotFoundError:
    REQUIREMENTS_TEMPLATE = "pytest==9.0.2\n"

# Load pytest.ini template with a fallback
try:
    PYTEST_INI_TEMPLATE = PYTEST_INI_TEMPLATE_PATH.read_text(encoding="utf-8")
except FileNotFoundError:
    PYTEST_INI_TEMPLATE = (
        "[pytest]\n"
        "markers =\n"
        "    smoke: Quick high-level health check of main flows.\n"
        "    api: Marks tests that hit HTTP APIs.\n"
        "    ui: Marks UI/end-to-end browser tests.\n"
    )

# Template for the default sample test (generic pytest)
TEST_SAMPLE_DEFAULT_TEMPLATE = (
    "import pytest\n\n\n"
    "@pytest.mark.smoke\n"
    "def test_sample_smoke_check():\n"
    "    \"\"\"Basic smoke test to verify that the test suite is wired correctly.\"\"\"\n"
    "    # Given\n"
    "    expected_value = 1\n\n"
    "    # When\n"
    "    result = 1\n\n"
    "    # Then\n"
    "    assert result == expected_value\n"
)

# Template for the API client helper
API_CLIENT_TEMPLATE = (
    "import os\n"
    "import requests\n\n\n"
    "class ApiClient:\n"
    "    \"\"\"Very small HTTP API client using requests.\n\n"
    "    This is only a starting point. Extend it with auth, headers,\n"
    "    logging, retries, etc., depending on your needs.\n"
    "    \"\"\"\n\n"
    "    def __init__(self, base_url: str | None = None) -> None:\n"
    "        # You can override the base URL via the API_BASE_URL env var\n"
    "        self.base_url = base_url or os.getenv(\"API_BASE_URL\", \"https://httpbin.org\")\n\n"
    "    def _build_url(self, path: str) -> str:\n"
    "        if not path.startswith(\"/\"):\n"
    "            path = \"/\" + path\n"
    "        return f\"{self.base_url}{path}\"\n\n"
    "    def get(self, path: str, **kwargs):\n"
    "        return requests.get(self._build_url(path), **kwargs)\n\n"
    "    def post(self, path: str, **kwargs):\n"
    "        return requests.post(self._build_url(path), **kwargs)\n"
)

# Template for the API sample test
TEST_SAMPLE_API_TEMPLATE = (
    "import pytest\n"
    "from tests.utils.api_client import ApiClient\n\n\n"
    "@pytest.mark.smoke\n"
    "@pytest.mark.api\n"
    "def test_healthcheck_endpoint_returns_200():\n"
    "    \"\"\"Example API smoke test using ApiClient.\n\n"
    "    By default it hits https://httpbin.org/status/200.\n"
    "    You can change the base URL via the API_BASE_URL env var.\n"
    "    \"\"\"\n"
    "    # Given\n"
    "    client = ApiClient()\n"
    "    path = \"/status/200\"\n\n"
    "    # When\n"
    "    response = client.get(path)\n\n"
    "    # Then\n"
    "    assert response.status_code == 200\n"
)

# Template for a simple Page Object (UI preset)
PAGES_LOGIN_TEMPLATE = (
    "class LoginPage:\n"
    "    \"\"\"Example Page Object skeleton for UI tests.\n\n"
    "    Replace the methods below with real interactions using Playwright,\n"
    "    Selenium, or any other browser automation library.\n"
    "    \"\"\"\n\n"
    "    def __init__(self, page) -> None:\n"
    "        \"\"\"`page` can be a Playwright/Selenium driver or similar.\"\"\"\n"
    "        self.page = page\n\n"
    "    def open(self) -> None:\n"
    "        \"\"\"Open the login page.\n\n"
    "        TODO: implement real navigation here.\n"
    "        \"\"\"\n"
    "        raise NotImplementedError(\"Implement LoginPage.open() with real UI actions\")\n\n"
    "    def login(self, username: str, password: str) -> None:\n"
    "        \"\"\"Fill the login form and submit.\n\n"
    "        TODO: implement real locators and actions here.\n"
    "        \"\"\"\n"
    "        raise NotImplementedError(\"Implement LoginPage.login() with real UI actions\")\n"
)

# Template for the UI sample test (no real browser yet, just skeleton)
TEST_SAMPLE_UI_TEMPLATE = (
    "import pytest\n\n\n"
    "@pytest.mark.smoke\n"
    "@pytest.mark.ui\n"
    "def test_ui_sample_placeholder():\n"
    "    \"\"\"Example UI test skeleton.\n\n"
    "    This test does NOT hit a real browser yet. It is a placeholder to\n"
    "    show naming and structure. Replace its body with real UI automation\n"
    "    using Playwright, Selenium, etc.\n"
    "    \"\"\"\n"
    "    # Given\n"
    "    expected_title = \"Swag Labs\"\n\n"
    "    # When\n"
    "    # TODO: replace this with a real browser call to get the title\n"
    "    current_title = expected_title\n\n"
    "    # Then\n"
    "    assert current_title == expected_title\n"
)

# README template for API preset (inline, independent from README_PROJECT.md)
README_API_TEMPLATE = (
    "# QA API Testing Starter Project\n\n"
    "This project was generated using the **QA Project Bootstrapper** with the **API preset**.\n\n"
    "It is focused on automated testing of HTTP APIs using **pytest** and **requests**.\n"
    "The goal is: _create env, install requirements, run your first API test_ in a few minutes,\n"
    "and then start adding real endpoints and test scenarios.\n\n"
    "---\n\n"
    "## 1. What you get\n\n"
    "- ✅ Python + pytest + requests\n"
    "- ✅ A basic API smoke test in `tests/test_sample.py`\n"
    "- ✅ `pytest.ini` with registered `smoke` and `api` markers\n"
    "- ✅ A small `ApiClient` helper in `tests/utils/api_client.py`\n\n"
    "---\n\n"
    "## 2. Quick start\n\n"
    "Create and activate a virtual environment:\n\n"
    "```bash\n"
    "python -m venv .venv\n"
    "```\n\n"
    "Activate it:\n\n"
    "- **Windows (PowerShell):**\n\n"
    "  ```bash\n"
    "  .\\.venv\\Scripts\\activate\n"
    "  ```\n\n"
    "- **Linux / macOS:**\n\n"
    "  ```bash\n"
    "  source .venv/bin/activate\n"
    "  ```\n\n"
    "Install dependencies:\n\n"
    "```bash\n"
    "pip install -r requirements.txt\n"
    "```\n\n"
    "Run tests:\n\n"
    "```bash\n"
    "pytest -v\n"
    "```\n\n"
    "---\n\n"
    "## 3. Project structure\n\n"
    "```text\n"
    ".\n"
    "├── tests/\n"
    "│   ├── __init__.py\n"
    "│   ├── test_sample.py        # Example API smoke test using ApiClient\n"
    "│   ├── data/                 # Test data (JSON, payloads, etc.)\n"
    "│   │   └── __init__.py\n"
    "│   ├── pages/                # (Optional) for UI / hybrid projects\n"
    "│   │   └── __init__.py\n"
    "│   └── utils/                # Helpers, clients, custom assertions\n"
    "│       ├── __init__.py\n"
    "│       └── api_client.py     # Minimal HTTP client wrapper\n"
    "├── pytest.ini\n"
    "├── requirements.txt\n"
    "└── README.md\n"
    "```\n\n"
    "---\n\n"
    "## 4. Next steps\n\n"
    "- Replace `test_sample.py` with real tests hitting your API endpoints\n"
    "- Extend `ApiClient` with auth, default headers, logging, retries, etc.\n"
    "- Store JSON payloads or test data inside `tests/data/`\n"
    "- Integrate this project into your CI pipeline\n\n"
    "---\n\n"
    "## Need a full Playwright + reporting stack?\n\n"
    "This API starter is minimal on purpose.\n"
    "If you need a more advanced, production-ready setup with:\n\n"
    "- Playwright + Pytest UI automation\n"
    "- HTML reports\n"
    "- CI artifacts (screenshots, videos, traces)\n"
    "- Opinionated PRO structure\n\n"
    "check out **QA Web Starter Kit PRO**:\n"
    "https://tyrengman.gumroad.com/l/QAKITPRO\n"
)

# README template for UI preset (inline)
README_UI_TEMPLATE = (
    "# QA UI Testing Starter Project\n\n"
    "This project was generated using the **QA Project Bootstrapper** with the **UI preset**.\n\n"
    "It is focused on **browser-based UI/end-to-end tests** using pytest.\n"
    "The goal is to give you a Page Object structure and markers so that you\n"
    "can plug in Playwright, Selenium, or any other UI automation tool.\n\n"
    "---\n\n"
    "## 1. What you get\n\n"
    "- ✅ Python + pytest\n"
    "- ✅ `tests/test_sample.py` with a UI test skeleton\n"
    "- ✅ `tests/pages/login_page.py` with a Page Object stub\n"
    "- ✅ `pytest.ini` with `smoke` and `ui` markers\n\n"
    "---\n\n"
    "## 2. Quick start\n\n"
    "Create and activate a virtual environment:\n\n"
    "```bash\n"
    "python -m venv .venv\n"
    "```\n\n"
    "Activate it:\n\n"
    "- **Windows (PowerShell):**\n\n"
    "  ```bash\n"
    "  .\\.venv\\Scripts\\activate\n"
    "  ```\n\n"
    "- **Linux / macOS:**\n\n"
    "  ```bash\n"
    "  source .venv/bin/activate\n"
    "  ```\n\n"
    "Install dependencies:\n\n"
    "```bash\n"
    "pip install -r requirements.txt\n"
    "```\n\n"
    "Run tests:\n\n"
    "```bash\n"
    "pytest -v\n"
    "```\n\n"
    "---\n\n"
    "## 3. Project structure\n\n"
    "```text\n"
    ".\n"
    "├── tests/\n"
    "│   ├── __init__.py\n"
    "│   ├── test_sample.py        # UI test skeleton (no real browser call yet)\n"
    "│   ├── data/                 # For test data if needed\n"
    "│   │   └── __init__.py\n"
    "│   ├── pages/                # Page Objects\n"
    "│   │   ├── __init__.py\n"
    "│   │   └── login_page.py     # Example Page Object stub\n"
    "│   └── utils/                # Helpers and shared code\n"
    "│       └── __init__.py\n"
    "├── pytest.ini\n"
    "├── requirements.txt\n"
    "└── README.md\n"
    "```\n\n"
    "---\n\n"
    "## 4. How to plug in Playwright or Selenium\n\n"
    "This preset does not install any specific UI automation library by default,\n"
    "to keep the starter lightweight and compatible.\n\n"
    "Typical next steps:\n\n"
    "- Install your preferred UI tool, e.g.:\n"
    "  - `pip install playwright` + `playwright install`\n"
    "  - or `pip install selenium`\n"
    "- Create fixtures (e.g. `page`, `driver`) in `conftest.py`\n"
    "- Implement real actions in `LoginPage.open()` and `LoginPage.login()`\n"
    "- Update `test_sample.py` to use real browser interactions\n\n"
    "---\n\n"
    "## Need a full Playwright + reporting stack?\n\n"
    "If you want a ready-to-use stack with:\n\n"
    "- Playwright + Pytest UI automation\n"
    "- HTML reports for stakeholders\n"
    "- CI artifacts (screenshots, videos, traces)\n"
    "- Proven, PRO-level structure\n\n"
    "check out **QA Web Starter Kit PRO**:\n"
    "https://tyrengman.gumroad.com/l/QAKITPRO\n"
)

# Carpetas base del proyecto QA
FOLDERS = [
    "tests",
    "tests/pages",
    "tests/data",
    "tests/utils",
    ".github/workflows",
]

# Base FILES (por defecto/preset 'default')
BASE_FILES = {
    "tests/__init__.py": "",
    "tests/pages/__init__.py": "",
    "tests/data/__init__.py": "",
    "tests/utils/__init__.py": "",
    "tests/test_sample.py": TEST_SAMPLE_DEFAULT_TEMPLATE,
    "README.md": README_TEMPLATE,
    "requirements.txt": REQUIREMENTS_TEMPLATE,
    "pytest.ini": PYTEST_INI_TEMPLATE,
    ".github/workflows/ci.yml": (
        "name: CI\n"
        "\n"
        "on:\n"
        "  push:\n"
        "    branches: [ \"main\" ]\n"
        "  pull_request:\n"
        "\n"
        "jobs:\n"
        "  test:\n"
        "    runs-on: ubuntu-latest\n"
        "    steps:\n"
        "      - uses: actions/checkout@v4\n"
        "      - uses: actions/setup-python@v5\n"
        "        with:\n"
        "          python-version: '3.10'\n"
        "      - run: pip install -r requirements.txt\n"
        "      - run: pytest -v\n"
    ),
}


def build_files_for_preset(preset: str) -> dict:
    """
    Devuelve el diccionario de FILES según el preset elegido.
    """
    files = dict(BASE_FILES)

    if preset == "api":
        # Test de ejemplo orientado a API
        files["tests/test_sample.py"] = TEST_SAMPLE_API_TEMPLATE

        # README específico para API
        files["README.md"] = README_API_TEMPLATE

        # requirements: base + requests
        req = REQUIREMENTS_TEMPLATE
        if "requests" not in req:
            if not req.endswith("\n"):
                req += "\n"
            req += "requests==2.32.3\n"
        files["requirements.txt"] = req

        # ApiClient helper
        files["tests/utils/api_client.py"] = API_CLIENT_TEMPLATE

    elif preset == "ui":
        # Test de ejemplo orientado a UI (placeholder sin navegador real)
        files["tests/test_sample.py"] = TEST_SAMPLE_UI_TEMPLATE

        # Page Object de ejemplo
        files["tests/pages/login_page.py"] = PAGES_LOGIN_TEMPLATE

        # README específico para UI
        files["README.md"] = README_UI_TEMPLATE

        # requirements: por ahora igual que base (solo pytest)
        files["requirements.txt"] = REQUIREMENTS_TEMPLATE

    # preset "default" usa BASE_FILES sin cambios
    return files


def parse_args() -> argparse.Namespace:
    """
    Lee argumentos de línea de comandos.

    Uso:
      python qa_init.py                         -> modo interactivo (pregunta el nombre)
      python qa_init.py my_proj                 -> crea proyecto default (pytest)
      python qa_init.py my_proj --no-ci         -> crea proyecto default SIN CI
      python qa_init.py my_api --preset api     -> crea proyecto orientado a API
      python qa_init.py my_ui --preset ui       -> crea proyecto orientado a UI
    """
    parser = argparse.ArgumentParser(
        description="Bootstrap a QA automation project (pytest-based)."
    )

    parser.add_argument(
        "project_name",
        nargs="?",  # opcional
        help="Name of the folder to create for your new QA project.",
    )

    parser.add_argument(
        "--no-ci",
        action="store_true",
        help="Do not create the .github/workflows/ci.yml file in the new project.",
    )

    parser.add_argument(
        "--preset",
        choices=["default", "api", "ui"],
        default="default",
        help="Project preset: 'default' for generic pytest, 'api' for API testing, 'ui' for UI/end-to-end testing.",
    )

    return parser.parse_args()


def create_structure(project_name: str, *, no_ci: bool = False, preset: str = "default") -> None:
    """
    Crea la estructura base de un proyecto QA dentro
    de una carpeta con el nombre indicado.
    """
    base_path = Path(project_name)

    # Protección: si la carpeta existe y NO está vacía, no pisamos nada
    if base_path.exists() and any(base_path.iterdir()):
        print(f"\n❌ ERROR: The target folder '{base_path}' already exists and is not empty.")
        print("   Aborting to avoid overwriting an existing project.")
        print("   Please choose a different project name, or clean the folder before retrying.\n")
        return

    print(f"\n🚀 Creating project at: {base_path.resolve()}")
    print(f"   Preset: {preset}")
    print(f"   CI: {'disabled (--no-ci)' if no_ci else 'enabled (GitHub Actions workflow)'}\n")

    files = build_files_for_preset(preset)

    # Crear carpetas
    for folder in FOLDERS:
        # Si no_ci es True, evitamos crear la carpeta .github/workflows
        if no_ci and folder.startswith(".github"):
            continue

        folder_path = base_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"📁 Folder created: {folder_path}")

    # Crear archivos
    for file_path, content in files.items():
        # Si no_ci es True, no crear el workflow de CI
        if no_ci and file_path.startswith(".github/workflows"):
            continue

        full_path = base_path / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)

        with full_path.open("w", encoding="utf-8") as f:
            f.write(content)

        print(f"📄 File created: {full_path}")

    print("\n🎉 Project created successfully!")
    print("\nNext steps:")
    print(f"  cd {project_name}")
    print("  python -m venv .venv")
    print("  .venv\\Scripts\\activate")
    print("  pip install -r requirements.txt")
    print("  pytest -v")

    print("\nOptional:")
    print("  For a full Playwright + reporting setup, see:")
    print("  QA Web Starter Kit PRO → https://tyrengman.gumroad.com/l/QAKITPRO")


if __name__ == "__main__":
    args = parse_args()

    project_name = (args.project_name or "").strip()

    # Modo interactivo si no se pasó project_name
    if not project_name:
        project_name = input("Enter a name for your new QA project: ").strip()

    if not project_name:
        print("❌ ERROR: project name cannot be empty.")
    else:
        create_structure(project_name, no_ci=args.no_ci, preset=args.preset)
