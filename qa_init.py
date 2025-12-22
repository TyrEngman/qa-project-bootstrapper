from pathlib import Path
import argparse

# Base directory of this bootstrapper
BASE_DIR = Path(__file__).parent

# Templates directory
TEMPLATES_DIR = BASE_DIR / "templates"

# README template path
README_TEMPLATE_PATH = TEMPLATES_DIR / "README_PROJECT.md"
# Requirements template path
REQUIREMENTS_TEMPLATE_PATH = TEMPLATES_DIR / "requirements.txt"

# Load README template (Markdown) with a fallback if file is missing
try:
    README_TEMPLATE = README_TEMPLATE_PATH.read_text(encoding="utf-8")
except FileNotFoundError:
    # Fallback minimal README so the script does not crash
    README_TEMPLATE = (
        "# QA Automation Starter Project\n\n"
        "Template file 'templates/README_PROJECT.md' was not found.\n"
        "Please add it to customize this README.\n"
    )

# Load requirements template with a fallback
try:
    REQUIREMENTS_TEMPLATE = REQUIREMENTS_TEMPLATE_PATH.read_text(encoding="utf-8")
except FileNotFoundError:
    # Fallback minimal requirements so the script does not crash
    REQUIREMENTS_TEMPLATE = "pytest==9.0.2\n"

# Carpetas base del proyecto QA
FOLDERS = [
    "tests",
    "tests/pages",
    "tests/data",
    "tests/utils",
    ".github/workflows",
]

# Archivos base del proyecto QA
FILES = {
    "tests/__init__.py": "",
    "tests/pages/__init__.py": "",
    "tests/data/__init__.py": "",
    "tests/utils/__init__.py": "",
    "tests/test_sample.py": (
        "def test_sample():\n"
        "    assert True\n"
    ),
    # README generado desde template
    "README.md": README_TEMPLATE,
    # ✅ Nuevo: requirements generado desde template
    "requirements.txt": REQUIREMENTS_TEMPLATE,
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


def parse_args() -> str:
    """
    Lee el nombre del proyecto desde la línea de comandos (opcional).

    Uso:
      python qa_init.py           -> modo interactivo (pregunta el nombre)
      python qa_init.py my_proj   -> modo automático (usa my_proj)
    """
    parser = argparse.ArgumentParser(
        description="Bootstrap a QA automation project (pytest-based)."
    )

    parser.add_argument(
        "project_name",
        nargs="?",  # opcional
        help="Name of the folder to create for your new QA project.",
    )

    args = parser.parse_args()
    return (args.project_name or "").strip()


def create_structure(project_name: str) -> None:
    """
    Crea la estructura base de un proyecto QA dentro
    de una carpeta con el nombre indicado.
    """
    base_path = Path(project_name)

    print(f"\n🚀 Creating project at: {base_path.resolve()}\n")

    # Crear carpetas
    for folder in FOLDERS:
        folder_path = base_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"📁 Folder created: {folder_path}")

    # Crear archivos
    for file_path, content in FILES.items():
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


if __name__ == "__main__":
    # 1) Intentar leer el nombre desde la CLI (python qa_init.py my_project)
    project_name = parse_args()

    # 2) Si no vino por argumentos, usamos el modo interactivo
    if not project_name:
        project_name = input("Enter a name for your new QA project: ").strip()

    # 3) Validación final
    if not project_name:
        print("❌ ERROR: project name cannot be empty.")
    else:
        create_structure(project_name)
