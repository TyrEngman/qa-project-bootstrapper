from pathlib import Path
import argparse

# === Paths base ===

# Carpeta raíz del bootstrapper (donde vive qa_init.py)
BASE_DIR = Path(__file__).parent

# Carpeta /templates
TEMPLATES_ROOT = BASE_DIR / "templates"

# Carpeta /templates/project
PROJECT_TEMPLATES_DIR = TEMPLATES_ROOT / "project"

# Rutas de templates principales
README_TEMPLATE_PATH = PROJECT_TEMPLATES_DIR / "README_PROJECT.md"
PYTEST_INI_TEMPLATE_PATH = PROJECT_TEMPLATES_DIR / "pytest.ini"
REQUIREMENTS_TEMPLATE_PATH = TEMPLATES_ROOT / "requirements.txt"

# Rutas de templates específicos por preset
README_API_TEMPLATE_PATH = PROJECT_TEMPLATES_DIR / "api" / "README_API_PROJECT.md"
README_UI_TEMPLATE_PATH = PROJECT_TEMPLATES_DIR / "ui" / "README_UI_PROJECT.md"


def _safe_read(path: Path, fallback: str) -> str:
    """
    Lee un archivo de texto de forma segura.
    Si no existe, devuelve el fallback para que el bootstrapper no reviente.
    """
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return fallback


# === Carga de templates ===

# README genérico (preset default)
README_TEMPLATE = _safe_read(
    README_TEMPLATE_PATH,
    "# QA Automation Starter Project\n\n"
    "Template file 'templates/project/README_PROJECT.md' was not found.\n"
    "Please add it to customize this README.\n",
)

# requirements.txt base
REQUIREMENTS_TEMPLATE = _safe_read(
    REQUIREMENTS_TEMPLATE_PATH,
    "pytest==9.0.2\n",
)

# pytest.ini base
PYTEST_INI_TEMPLATE = _safe_read(
    PYTEST_INI_TEMPLATE_PATH,
    "[pytest]\n"
    "markers =\n"
    "    smoke: Quick high-level health check of main flows.\n"
    "    api: Marks tests that hit HTTP APIs.\n"
    "    ui: Marks ui/end-to-end browser tests.\n",
)

# README para preset api (viene del template; fallback mínimo si falta el archivo)
README_API_TEMPLATE = _safe_read(
    README_API_TEMPLATE_PATH,
    "# QA api Testing Starter Project\n\n"
    "Template file 'templates/project/api/README_API_PROJECT.md' was not found.\n"
    "Please add it to customize this README.\n",
)

# README para preset ui (viene del template; fallback mínimo si falta el archivo)
README_UI_TEMPLATE = _safe_read(
    README_UI_TEMPLATE_PATH,
    "# QA ui Testing Starter Project\n\n"
    "Template file 'templates/project/ui/README_UI_PROJECT.md' was not found.\n"
    "Please add it to customize this README.\n",
)

# === Templates de código ===

# Test sample por defecto (preset "default")
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

# api client helper
API_CLIENT_TEMPLATE = (
    "import os\n"
    "import requests\n\n\n"
    "class ApiClient:\n"
    "    \"\"\"Very small HTTP api client using requests.\n\n"
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

# Test sample para preset api
TEST_SAMPLE_API_TEMPLATE = (
    "import pytest\n"
    "from tests.utils.api_client import ApiClient\n\n\n"
    "@pytest.mark.smoke\n"
    "@pytest.mark.api\n"
    "def test_healthcheck_endpoint_returns_200():\n"
    "    \"\"\"Example api smoke test using ApiClient.\n\n"
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

# Page Object de ejemplo para UI
PAGES_LOGIN_TEMPLATE = (
    "class LoginPage:\n"
    "    \"\"\"Example Page Object skeleton for ui tests.\n\n"
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
    "        raise NotImplementedError(\"Implement LoginPage.open() with real ui actions\")\n\n"
    "    def login(self, username: str, password: str) -> None:\n"
    "        \"\"\"Fill the login form and submit.\n\n"
    "        TODO: implement real locators and actions here.\n"
    "        \"\"\"\n"
    "        raise NotImplementedError(\"Implement LoginPage.login() with real ui actions\")\n"
)

# Test sample para preset ui (skeleton sin navegador real)
TEST_SAMPLE_UI_TEMPLATE = (
    "import pytest\n\n\n"
    "@pytest.mark.smoke\n"
    "@pytest.mark.ui\n"
    "def test_ui_sample_placeholder():\n"
    "    \"\"\"Example ui test skeleton.\n\n"
    "    This test does NOT hit a real browser yet. It is a placeholder to\n"
    "    show naming and structure. Replace its body with real ui automation\n"
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

# === Estructura base ===

FOLDERS = [
    "tests",
    "tests/pages",
    "tests/data",
    "tests/utils",
    ".github/workflows",
]

# Archivos base (preset "default")
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
        # Test de ejemplo orientado a api
        files["tests/test_sample.py"] = TEST_SAMPLE_API_TEMPLATE

        # README específico para api (desde templates/project/api)
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
        # Test de ejemplo orientado a ui (placeholder sin navegador real)
        files["tests/test_sample.py"] = TEST_SAMPLE_UI_TEMPLATE

        # Page Object de ejemplo
        files["tests/pages/login_page.py"] = PAGES_LOGIN_TEMPLATE

        # README específico para ui (desde templates/project/ui)
        files["README.md"] = README_UI_TEMPLATE

        # requirements: por ahora igual que base (solo pytest)
        files["requirements.txt"] = REQUIREMENTS_TEMPLATE

    # preset "default" usa BASE_FILES sin cambios
    return files


# === CLI ===

def parse_args() -> argparse.Namespace:
    """
    Lee argumentos de línea de comandos.

    Uso:
      python qa_init.py                         -> modo interactivo (pregunta el nombre)
      python qa_init.py my_proj                 -> crea proyecto default (pytest)
      python qa_init.py my_proj --no-ci         -> crea proyecto default SIN CI
      python qa_init.py my_api --preset api     -> crea proyecto orientado a api
      python qa_init.py my_ui --preset ui       -> crea proyecto orientado a ui
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
        help="Project preset: 'default' for generic pytest, 'api' for api testing, 'ui' for ui/end-to-end testing.",
    )

    return parser.parse_args()


# === Creación de estructura ===

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


# === Entry point ===

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
