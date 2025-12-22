# QA Project Bootstrapper

The **QA Project Bootstrapper** is a simple CLI tool that creates a ready-to-run **pytest** automation project in a new folder.

It is designed to help you (or your team) go from _zero to running tests_ in a few minutes, with a clean structure and opinionated defaults. Instead of copying old repos or fighting with boilerplate, you run one command and start writing tests.

This tool is the **lightweight CLI companion** to the **QA Web Starter Kit PRO**:  
- The **bootstrapper** gives you a minimal, standardized pytest skeleton (great for internal projects, experiments, and quick PoCs).  
- The **QA Web Starter Kit PRO** adds a full Playwright + Pytest stack, advanced fixtures, HTML reports, CI artifacts, and production-ready patterns for client work.

---

## 1. What this tool does

Given a project name, the bootstrapper:

- Creates a new folder with that name
- Generates a **minimal but structured pytest project**, including:
  - `tests/` package with subfolders:
    - `tests/pages/`
    - `tests/data/`
    - `tests/utils/`
  - An example test: `tests/test_sample.py`
  - A `README.md` inside the generated project, based on a Markdown template
  - A `requirements.txt` inside the generated project (pytest only, by default)
  - A basic **GitHub Actions CI** workflow at `.github/workflows/ci.yml`
- Prints the exact next steps to:
  - create a virtual environment,
  - install dependencies,
  - and run tests.

The generated project is intentionally minimal. You can extend it with Playwright, Selenium, API clients, etc., depending on your stack.

---

## 2. Requirements

To use this bootstrapper, you need:

- Python **3.10+**
- `pip` available in your PATH
- A terminal:
  - Windows: PowerShell or the integrated terminal in PyCharm / VS Code
  - Linux / macOS: bash, zsh, etc.

Optional but recommended:

- Git
- An editor like PyCharm, VS Code, etc.

---

## 3. Setup (bootstrapper itself)

This repo is the _bootstrapper_, not the generated project.

From the root of this repository:

1. **Create a virtual environment (once):**

   ```bash
   python -m venv .venv
Activate it:

Windows (PowerShell):

bash
Copiar código
.\.venv\Scripts\activate
Linux / macOS:

bash
Copiar código
source .venv/bin/activate
Install bootstrapper dependencies:

bash
Copiar código
pip install -r requirements.txt
These dependencies are for the bootstrapper itself, not for the projects it generates.

4. Usage
You can use the bootstrapper in two modes:

4.1 CLI mode (recommended)
From the root of this repo, with the virtualenv active:

bash
Copiar código
python qa_init.py my_new_qa_project
This will:

Create a folder my_new_qa_project/

Generate all folders and files inside

Print a short summary and “next steps”

4.2 Interactive mode
If you prefer to type the name when prompted:

bash
Copiar código
python qa_init.py
You will see:

text
Copiar código
Enter a name for your new QA project:
Type the project name (e.g. my_new_qa_project) and press Enter.

5. What gets generated
A typical generated project looks like this:

text
Copiar código
my_new_qa_project/
├── README.md
├── requirements.txt
├── .github/
│   └── workflows/
│       └── ci.yml
└── tests/
    ├── __init__.py
    ├── test_sample.py         # Example test (safe to delete once you add your own)
    ├── data/
    │   └── __init__.py        # For test data: JSON, CSV, builders, etc.
    ├── pages/
    │   └── __init__.py        # For Page Object / Screen Object models
    └── utils/
        └── __init__.py        # For helpers, factories, custom assertions
6. Next steps inside a generated project
After generating a project:

Enter the project folder:

bash
Copiar código
cd my_new_qa_project
Create and activate a virtual environment (project-local):

bash
Copiar código
python -m venv .venv
Activate it:

Windows (PowerShell):

bash
Copiar código
.\.venv\Scripts\activate
Linux / macOS:

bash
Copiar código
source .venv/bin/activate
Install project dependencies:

bash
Copiar código
pip install -r requirements.txt
Run tests:

bash
Copiar código
pytest -v
You should see at least one passing test (test_sample.py).
After that, you can delete test_sample.py and start writing your real tests.

7. Templates: README and requirements
The bootstrapper uses templates stored inside the templates/ folder:

templates/README_PROJECT.md
→ Copied inside each generated project as README.md.

templates/requirements.txt
→ Copied inside each generated project as requirements.txt.

This has two advantages:

You can improve the project README (add sections, examples, screenshots) without touching Python code.

You can adjust the default stack (for example, add pytest-html, requests, etc.) just by editing the template requirements.txt.

If a template file is missing, the bootstrapper falls back to a minimal default so it does not crash.

8. Continuous Integration (GitHub Actions)
Each generated project includes a basic CI workflow:

text
Copiar código
.github/workflows/ci.yml
By default, it:

Checks out the code

Sets up Python

Installs requirements.txt

Runs:

bash
Copiar código
pytest -v
To enable it in your repo:

Initialize a git repository inside the generated project:

bash
Copiar código
git init
git add .
git commit -m "Initial QA project bootstrap"
Push it to GitHub (e.g. to a main branch).

GitHub Actions will automatically run the workflow on push / pull request.

You can extend the CI pipeline to:

Upload test reports as artifacts

Run in multiple Python versions

Integrate with Playwright, Selenium, API tests, etc.

9. Current scope and roadmap
Right now, the bootstrapper focuses on:

✅ A clean pytest skeleton

✅ Project structure with clear places for:

tests

pages

data

utils

✅ Basic CI with GitHub Actions

✅ Template-based README and requirements

Planned / possible future improvements:

Optional Playwright integration (UI tests) behind a flag:

e.g. python qa_init.py my_project --with-playwright

Optional pytest-html / HTML reporting template

Project presets:

“UI only”

“API only”

“Hybrid (UI + API)”

Packaging this bootstrapper as an installable CLI:

pip install qa-bootstrapper

qa-init my_project

10. License & usage
This bootstrapper is intended as an internal tool or starter for QA/Automation projects.
You can adapt the structure, templates and CI configuration to fit your team or client standards.

If you use this inside a paid QA Web Starter Kit PRO, you can position it as:

“One-command project generator for pytest-based QA repos”

“Standard QA skeleton used in all our projects”

So every new project starts consistent, organized, and automation-ready from day one.

---

## CLI usage and presets

The bootstrapper can generate different types of QA projects using presets and flags.

### Basic usage (default preset)

Creates a **generic pytest** project with a simple smoke test, `pytest.ini` and a GitHub Actions workflow:

```bash
python qa_init.py my_qa_project
then:
cd my_qa_project
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
pytest -v

Disable CI (--no-ci)

If you don’t want a GitHub Actions workflow, use:

python qa_init.py my_qa_project --no-ci


This will not create the .github/workflows/ci.yml file.

API preset (--preset api)

Creates a project oriented to HTTP API testing with:

pytest + requests

tests/utils/api_client.py → small ApiClient wrapper

tests/test_sample.py → smoke test using ApiClient

pytest.ini with smoke and api markers

An API-focused README.md

Command:

python qa_init.py my_api_project --preset api


Then:

cd my_api_project
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
pytest -v


You can also combine the API preset with --no-ci:

python qa_init.py my_api_project --preset api --no-ci

Summary of options

--preset default (por defecto)
Generic pytest project with a smoke test and optional CI.

--preset api
API testing starter project with requests and an ApiClient.

--no-ci
Skips creating .github/workflows/ci.yml.

### UI preset (`--preset ui`)

Creates a project oriented to **UI / end-to-end testing** with:

- `pytest`
- `tests/test_sample.py` → UI test skeleton (no real browser yet)
- `tests/pages/login_page.py` → Page Object stub
- `pytest.ini` with `smoke` and `ui` markers

Command:

```bash
python qa_init.py my_ui_project --preset ui
Then:

bash
Copiar código
cd my_ui_project
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
pytest -v

## 11. Upgrade: QA Web Starter Kit PRO

This CLI focuses on generating a clean, minimal pytest project.

If you need a **full, production-ready stack** with:

- Playwright + Pytest UI automation
- HTML reports for clients and stakeholders
- CI pipelines with test artifacts (screenshots, videos, traces)
- Markers, tagging and a documented PRO structure

you can upgrade to:

**QA Web Starter Kit PRO**  
→ [Get the PRO kit here](https://tyrengman.gumroad.com/l/QAKITPRO)