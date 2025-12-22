# QA Minimal Pytest Project

This project was generated with **qa-project-bootstrapper** using the `minimal` preset.

It gives you a clean, lightweight structure to start any kind of automated tests
(API, UI, integration, etc.) with plain **pytest**.

---

## Quick start

```bash
# 1. Create and enter your project (already done by the bootstrapper)
cd <your-project-name>

# 2. (Recommended) Create a virtualenv
python -m venv .venv
.venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run tests
pytest -v
Project structure
text
Copiar código
.
├─ tests/
│  ├─ __init__.py
│  └─ test_sample.py
├─ pytest.ini
├─ README.md
└─ requirements.txt
tests/ – your test suite.

test_sample.py – a tiny example you can delete or adapt.

pytest.ini – basic pytest configuration (markers, options).

requirements.txt – minimal dependencies (pytest and friends).

💡 Tip: For a very minimal project, create it with:
python qa_init.py my_project --preset minimal --no-ci

Next steps
Rename test_sample.py to match your real feature (e.g. test_login.py).

Add new tests inside tests/ as your suite grows.

Integrate additional tools (requests, Playwright, etc.) by updating
requirements.txt as needed.



---

## 2) Ajustes en `qa_init.py` (idea general)

Sin tocar todavía nada de tu código, te resumo lo que haría este preset:

1. **Argumento nuevo:**

   En la parte donde defines `--preset`:

   ```python
   parser.add_argument(
       "--preset",
       choices=["default", "api", "ui", "minimal"],
       default="default",
       help="Project template to use (default, api, ui, minimal).",
   )
Leer el README según preset:

Antes teníamos algo tipo:


PROJECT_TEMPLATES_DIR = TEMPLATES_DIR / "project"

README_DEFAULT = (PROJECT_TEMPLATES_DIR / "README_PROJECT.md").read_text(...)
README_API     = (PROJECT_TEMPLATES_DIR / "api" / "README_API_PROJECT.md").read_text(...)
README_UI      = (PROJECT_TEMPLATES_DIR / "ui" / "README_UI_PROJECT.md").read_text(...)
Añade:


README_MINIMAL = (PROJECT_TEMPLATES_DIR / "minimal" / "README_MINIMAL_PROJECT.md").read_text(encoding="utf-8")
Elegir contenido según preset:

Donde construyes el diccionario FILES o donde eliges el README, algo como:



if preset == "api":
    readme_content = README_API
    sample_test_content = SAMPLE_TEST_API
elif preset == "ui":
    readme_content = README_UI
    sample_test_content = SAMPLE_TEST_UI
elif preset == "minimal":
    readme_content = README_MINIMAL
    sample_test_content = SAMPLE_TEST_MINIMAL
else:
    readme_content = README_DEFAULT
    sample_test_content = SAMPLE_TEST_DEFAULT
Y luego pones FILES["README.md"] = readme_content y el contenido del sample.

Sample test minimal:

Muy simple, sin Playwright ni requests:



SAMPLE_TEST_MINIMAL = (
    "import pytest\n\n"
    "@pytest.mark.smoke\n"
    "def test_example():\n"
    "    assert 1 + 1 == 2\n"
)