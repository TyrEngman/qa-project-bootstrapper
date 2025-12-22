
# QA Project Bootstrapper

The **QA Project Bootstrapper** is a simple CLI tool that creates a ready-to-run **pytest** automation project in a new folder.

It is designed to help you (or your team) go from _zero to running tests_ in a few minutes, with a clean structure and opinionated defaults. Instead of copying old repos or fighting with boilerplate, you run one command and start writing tests.

This tool is the **lightweight CLI companion** to the **QA Web Starter Kit PRO**:

- The **bootstrapper** gives you a minimal, standardized pytest skeleton (great for internal projects, experiments, and quick PoCs).
- The **QA Web Starter Kit PRO** adds a full Playwright + Pytest stack, advanced fixtures, HTML reports, CI artifacts, and production-ready patterns for client work.

---

## 1. What this tool does

Given a project name, the bootstrapper:

- Creates a new folder with that name.
- Generates a **minimal but structured pytest project**, including:
  - `tests/` package with subfolders:
    - `tests/pages/`
    - `tests/data/`
    - `tests/utils/`
  - An example test: `tests/test_sample.py`
  - A `README.md` inside the generated project, based on a Markdown template
  - A `requirements.txt` inside the generated project (pytest only, by default; more if preset requires it)
  - A basic **GitHub Actions CI** workflow at `.github/workflows/ci.yml` (unless you disable it with `--no-ci`)
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

   ```
   python -m venv .venv

Activate it:

Windows (PowerShell):

.\.venv\Scripts\activate


Linux / macOS:

source .venv/bin/activate


Install bootstrapper dependencies:

pip install -r requirements.txt


These dependencies are for the bootstrapper itself, not for the projects it generates.

4. Usage

You can use the bootstrapper in two modes: CLI mode and interactive mode.

4.1 CLI mode (recommended)

From the root of this repo, with the virtualenv active:

python qa_init.py my_new_qa_project


This will:

Create a folder my_new_qa_project/

Generate all folders and files inside

Print a short summary and “next steps”

4.2 Interactive mode

If you prefer to type the name when prompted:

python qa_init.py


You will see:

Enter a name for your new QA project:


Type the project name (e.g. my_new_qa_project) and press Enter.

5. What gets generated

A typical generated project (default preset) looks like this:

my_new_qa_project/
├── README.md
├── requirements.txt
├── pytest.ini
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


Depending on the preset (default, api, ui), the content of README.md, requirements.txt, and sample tests will change.

6. Next steps inside a generated project

After generating a project:

Enter the project folder:

cd my_new_qa_project


Create and activate a virtual environment (project-local):

python -m venv .venv


Windows (PowerShell):

.\.venv\Scripts\activate


Linux / macOS:

source .venv/bin/activate


Install project dependencies:

pip install -r requirements.txt


Run tests:

pytest -v


You should see at least one passing test (test_sample.py).
After that, you can delete test_sample.py and start writing your real tests.

7. Templates: README and requirements

The bootstrapper uses templates stored inside the templates/ folder.

Typical structure (example):

templates/
    README_PROJECT.md        # Base README used in default preset
    requirements.txt         # Base requirements template
    pytest.ini               # Base pytest configuration


These give you two big advantages:

You can improve the project README (add sections, examples, screenshots) without touching Python code.

You can adjust the default stack (for example, add pytest-html, requests, etc.) just by editing the template requirements.txt.

If a template file is missing, the bootstrapper falls back to a minimal default so it does not crash.

8. Continuous Integration (GitHub Actions)

Each generated project includes a basic CI workflow (unless disabled with --no-ci):

.github/workflows/ci.yml


By default, it:

Checks out the code

Sets up Python

Installs requirements.txt

Runs:

pytest -v


To enable it in your repo:

Initialize a git repository inside the generated project:

git init
git add .
git commit -m "Initial QA project bootstrap"


Push it to GitHub (e.g. to a main or master branch).

GitHub Actions will automatically run the workflow on push / pull request.

You can extend the CI pipeline to:

Upload test reports as artifacts

Run in multiple Python versions

Integrate with Playwright, Selenium, API tests, etc.

9. CLI usage and presets

The bootstrapper can generate different types of QA projects using presets and flags.

9.1 Basic usage (default preset)

Creates a generic pytest project with a simple smoke test, pytest.ini and a GitHub Actions workflow:

python qa_init.py my_qa_project


Then:

cd my_qa_project
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
pytest -v

9.2 Disable CI (--no-ci)

If you don’t want a GitHub Actions workflow, use:

python qa_init.py my_qa_project --no-ci


This will not create the .github/workflows/ci.yml file.

9.3 API preset (--preset api)

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

9.4 UI preset (--preset ui)

Creates a project oriented to UI / end-to-end testing with:

pytest

tests/test_sample.py → UI test skeleton (no real browser yet)

tests/pages/login_page.py → Page Object stub

pytest.ini with smoke and ui markers

A UI-focused README.md

Command:

python qa_init.py my_ui_project --preset ui


Then:

cd my_ui_project
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
pytest -v

9.5 Summary of options

--preset default (default)

Generic pytest project with a smoke test and optional CI.

--preset api

API testing starter project with requests and an ApiClient.

--preset ui

UI testing starter project with a Page Object stub.

--no-ci

Skips creating .github/workflows/ci.yml.

10. When this tool is useful

Spinning up quick POCs for clients or interviews.

Teaching QA automation with a repeatable starting point.

Keeping your team aligned on project structure & conventions.

Generating disposable sandboxes for experiments.

Standardizing your QA repos so every new project starts consistent and automation-ready from day one.

11. Upgrade: QA Web Starter Kit PRO

This CLI focuses on generating a clean, minimal pytest project.

If you need a full, production-ready stack with:

Playwright + Pytest UI automation

HTML reports for clients and stakeholders

CI pipelines with test artifacts (screenshots, videos, traces)

Markers, tagging and a documented PRO structure

you can upgrade to:

QA Web Starter Kit PRO
→ https://tyrengman.gumroad.com/l/QAKITPRO

You can position them like this:

Use the QA Project Bootstrapper as your one-command project generator for pytest-based QA repos.

Use QA Web Starter Kit PRO when you want a polished, client-ready solution with Playwright, reporting and CI artifacts.

12. License & usage

This bootstrapper is intended as a starting point for QA/Automation projects.

You can adapt the structure, templates and CI configuration to fit your team or client standards.

This project is released under the MIT License.
Feel free to use it in personal, educational, or commercial projects.