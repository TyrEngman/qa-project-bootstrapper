# QA Automation Starter Project (pytest)

This project was generated using the **QA Project Bootstrapper**.

It gives you a clean, minimal **pytest** setup so you can start writing automated tests in minutes, without copy-pasting from old repos or fighting with boilerplate.

---

## 1. Goals of this starter

- ✅ Have a **consistent project structure** for QA automation.
- ✅ Make it easy to run tests locally (`pytest -v`).
- ✅ Provide a simple CI pipeline (GitHub Actions) out of the box.
- ✅ Let you extend it with your own tools (Playwright, Selenium, API clients, etc.).

This preset is intentionally generic so you can use it for:
- Web UI tests
- API tests
- Integration/system tests
- Mixed or layered suites

---

## 2. Quick start

### 2.1 Create and activate a virtual environment

From the root of this project:

```bash
python -m venv .venv


Activate it:

Windows (PowerShell):

.\.venv\Scripts\activate


Linux / macOS:

source .venv/bin/activate

2.2 Install dependencies
pip install -r requirements.txt

2.3 Run tests
pytest -v


You should see the sample test in tests/test_sample.py passing.
Once you confirm that, you can delete test_sample.py and start adding your own tests.

3. Project structure

A typical structure for this starter:

.
├── README.md
├── requirements.txt
├── pytest.ini
├── .github/
│   └── workflows/
│       └── ci.yml             # Basic GitHub Actions pipeline (optional)
└── tests/
    ├── __init__.py
    ├── test_sample.py         # Example test (safe to delete)
    ├── data/
    │   └── __init__.py        # For payloads, JSON, CSV, factories, etc.
    ├── pages/
    │   └── __init__.py        # For Page Objects / Screen Objects (UI)
    └── utils/
        └── __init__.py        # For helpers, custom assertions, clients, etc.


You can freely add more subfolders under tests/ as your suite grows.

4. Pytest configuration and markers

The pytest.ini file is pre-configured with a few example markers (like smoke), so you can start grouping tests from day one.

Example usage:

import pytest

@pytest.mark.smoke
def test_critical_login_flow():
    ...


Then you can run only smoke tests:

pytest -m smoke -v


Feel free to edit pytest.ini to add your own domains, components or tags.

5. Continuous Integration (GitHub Actions)

If this project was generated with CI enabled, you will find:

.github/workflows/ci.yml


This workflow does:

Checks out the code.

Sets up Python.

Installs requirements.txt.

Runs:

pytest -v


To enable CI:

Initialize git (if not already):

git init
git add .
git commit -m "Initial QA project bootstrap"


Create a repository on GitHub and push this project.

GitHub Actions will automatically run the workflow on each push and pull request.

You can extend ci.yml to:

run on multiple Python versions,

upload test reports as artifacts,

integrate with coverage, HTML reports, Slack notifications, etc.

6. Next steps

Some ideas to evolve this starter:

Add real tests for your application under tests/.

Introduce Page Objects in tests/pages/ if you are testing web UIs.

Store reusable payloads or fixtures under tests/data/.

Add helper modules under tests/utils/ (custom assertions, API clients, factories…).

Integrate with your preferred test reporting tools.

7. Need a full Playwright + Pytest web stack?

This starter is intentionally minimal and generic.

If you need a production-ready Playwright + Pytest setup with:

UI automation already wired,

HTML reports for stakeholders,

CI artifacts (screenshots, videos, traces),

Proven structure and patterns,

check out:

QA Web Starter Kit PRO (Playwright + Pytest)
→ https://tyrengman.gumroad.com/l/QAKITPRO


---

## 2️⃣ README para preset `api` (README del proyecto API)

```markdown
# QA API Testing Starter Project (pytest + requests)

This project was generated using the **QA Project Bootstrapper** with the **API preset**.

It is focused on **HTTP API testing** using:

- [`pytest`](https://docs.pytest.org/)
- [`requests`](https://requests.readthedocs.io/)

The goal is to go from _empty folder_ to _first passing API test_ in a few minutes, and then let you grow the suite around your real endpoints.

---

## 1. What you get

- ✅ Python + pytest + requests
- ✅ A basic API smoke test in `tests/test_sample.py`
- ✅ `pytest.ini` with registered `smoke` and `api` markers
- ✅ A small `ApiClient` helper in `tests/utils/api_client.py`

You can use this as:

- A starting point for a new API test suite
- A playground for learning pytest + requests
- A template to standardize API QA projects in your team

---

## 2. Quick start

From the root of this project:

### 2.1 Create and activate a virtual environment

```bash
python -m venv .venv


Activate it:

Windows (PowerShell):

.\.venv\Scripts\activate


Linux / macOS:

source .venv/bin/activate

2.2 Install dependencies
pip install -r requirements.txt

2.3 Run tests
pytest -v


You should see the sample API test passing.

By default it may hit a public endpoint (e.g. https://httpbin.org/status/200) just to validate the plumbing. You will replace this with your own API later.

3. Project structure
.
├── README.md
├── requirements.txt
├── pytest.ini
└── tests/
    ├── __init__.py
    ├── test_sample.py         # Example API test
    ├── data/
    │   └── __init__.py        # For payloads, JSON bodies, test data…
    ├── pages/
    │   └── __init__.py        # Optional (for hybrid UI/API projects)
    └── utils/
        ├── __init__.py
        └── api_client.py      # Simple HTTP API client wrapper


You can add more modules under tests/utils/ for:

Authentication flows

Custom assertions

Reusable request builders

Test data generation

4. The ApiClient helper

tests/utils/api_client.py contains a small wrapper over requests.
It is intentionally minimal so you can adjust it to your needs.

Key ideas:

It reads a base URL from an environment variable, e.g. API_BASE_URL.

It builds GET / POST calls for you, so tests stay clean.

Example (pseudocode):

from tests.utils.api_client import ApiClient

def test_healthcheck():
    client = ApiClient()
    response = client.get("/status/200")
    assert response.status_code == 200

4.1 Configuring the base URL

You can set the target API host via environment variable, for example:

set API_BASE_URL=https://your-api.example.com   # Windows (PowerShell: $env:API_BASE_URL)
export API_BASE_URL=https://your-api.example.com  # Linux / macOS


Then the client will hit https://your-api.example.com/<path>.

This makes it easy to switch between environments:

local

staging

production-like test envs

5. Pytest markers

The pytest.ini is pre-configured with markers like:

smoke – for critical or high-level flows.

api – for tests that hit HTTP APIs.

Example:

import pytest

@pytest.mark.smoke
@pytest.mark.api
def test_healthcheck():
    ...


Run only smoke API tests:

pytest -m "smoke and api" -v


You can add more markers to pytest.ini (e.g. regression, contract, performance-lite, etc.) to structure your suite.

6. Continuous Integration (GitHub Actions)

If this project was generated with CI support, you will find:

.github/workflows/ci.yml


This file is a basic pipeline that:

Sets up Python

Installs requirements.txt

Runs pytest -v

To enable CI:

Initialize a git repo here and commit:

git init
git add .
git commit -m "Initial API QA project bootstrap"


Push to a remote repository (GitHub, GitLab, etc.).

GitHub Actions (or equivalent) will run the pipeline on each push.

You can extend the workflow to:

Publish HTML reports or JUnit XML results

Run different test subsets (smoke, regression)

Integrate with Slack, Teams, or dashboards

7. How to grow this project

Some suggestions:

Replace test_sample.py with real tests for your endpoints.

Put sample JSON payloads or request bodies under tests/data/.

Add authentication helpers to api_client.py:

OAuth tokens

API keys

Session cookies

Split tests into multiple modules by domain:

tests/test_users.py

tests/test_orders.py

tests/test_healthcheck.py

Add parametrized tests for:

status codes

edge cases

invalid inputs

8. Need a full Playwright + Pytest UI stack?

This API starter is intentionally focused on backend / HTTP services.

If you also need a production-ready web UI stack with:

Playwright + Pytest

HTML test reports

CI artifacts (screenshots, videos, traces)

A documented, client-ready structure

check out:

QA Web Starter Kit PRO (Playwright + Pytest)
→ https://tyrengman.gumroad.com/l/QAKITPRO


---

## 3️⃣ README para preset `ui` (README del proyecto UI)

```markdown
# QA UI Testing Starter Project (pytest)

This project was generated using the **QA Project Bootstrapper** with the **UI preset**.

It is focused on **UI / end-to-end testing**, using pytest as the test runner.  
By design, this preset does **not** enforce a specific UI automation library. You can plug in:

- Playwright
- Selenium
- Or any other browser automation tool

The goal is to give you a clean structure and Page Object skeleton so you can focus on your tests, not on wiring everything from scratch.

---

## 1. What you get

- ✅ Python + pytest
- ✅ `tests/test_sample.py` with a UI test skeleton (no real browser yet)
- ✅ `tests/pages/login_page.py` with a Page Object stub
- ✅ `pytest.ini` with `smoke` and `ui` markers

You decide which UI engine to integrate (Playwright, Selenium, etc.).

---

## 2. Quick start

From the root of this project:

### 2.1 Create and activate a virtual environment

```bash
python -m venv .venv


Activate it:

Windows (PowerShell):

.\.venv\Scripts\activate


Linux / macOS:

source .venv/bin/activate

2.2 Install dependencies
pip install -r requirements.txt


At the beginning, this file might only include pytest.
You will add Playwright, Selenium or other packages later when you decide your stack.

2.3 Run tests
pytest -v


You should see the sample UI test passing.
Right now it is just a placeholder to verify that pytest and your environment work correctly.

3. Project structure
.
├── README.md
├── requirements.txt
├── pytest.ini
└── tests/
    ├── __init__.py
    ├── test_sample.py         # Placeholder UI test
    ├── data/
    │   └── __init__.py        # For test data or fixtures
    ├── pages/
    │   ├── __init__.py
    │   └── login_page.py      # Example Page Object stub
    └── utils/
        └── __init__.py        # For helpers, drivers, etc.


You can add more Page Objects under tests/pages/:

home_page.py

inventory_page.py

checkout_page.py

etc.

And shared helpers under tests/utils/.

4. Page Object skeleton (LoginPage)

tests/pages/login_page.py contains an example LoginPage class with unimplemented methods.

It is there to show you the pattern:

One class per screen/page

Methods that wrap interactions (open page, login, click buttons, etc.)

You are expected to:

Choose your engine (e.g. Playwright or Selenium).

Add locators and concrete actions inside the methods.

Create fixtures that provide the page or driver objects to your tests.

Example (conceptual):

# tests/pages/login_page.py (to be implemented by you)

class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://your-app.example.com/login")

    def login(self, username: str, password: str):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")


Once implemented, your tests can stay clean and focused on behavior, not on low-level selectors.

5. Pytest markers

The pytest.ini for this preset defines the ui marker (in addition to smoke).

Example usage:

import pytest

@pytest.mark.smoke
@pytest.mark.ui
def test_login_happy_path():
    ...


Run only UI smoke tests:

pytest -m "smoke and ui" -v


You can add more markers to organize your suite:

regression

slow

mobile

etc.

6. How to plug in Playwright or Selenium

This preset is intentionally tool-agnostic. Common next steps:

6.1 For Playwright

Install Playwright + pytest plugin:

pip install playwright pytest-playwright
playwright install


Add fixtures or use the built-in page fixture.

Implement real actions in your Page Objects (like LoginPage).

Update test_sample.py or add new tests that use the page fixture and your Page Objects.

6.2 For Selenium

Install Selenium:

pip install selenium


Create a conftest.py with a driver fixture (Chrome, Firefox, etc.).

Pass the driver to your Page Objects.

Update your tests to use the driver fixture.

7. Continuous Integration (optional)

You can easily integrate this project into CI:

Add or refine .github/workflows/ci.yml to:

install your UI driver dependencies,

run headless browsers (for Playwright, Selenium, etc.),

and execute pytest -v or a specific marker subset.

Typical CI steps:

- run: pip install -r requirements.txt
- run: pytest -m "smoke and ui" -v

8. Growing this project

Ideas to evolve this UI starter:

Define a consistent naming convention for Page Objects and locators.

Add screenshot capture on failure.

Integrate with HTML test reports.

Add environment configuration (URLs, credentials) via config files or environment variables.

Create test suites for different areas of the app (auth, inventory, checkout…).

9. Need a full Playwright + Pytest web stack?

This preset only provides the structure and a starting point.

If you want a ready-to-use, production-level Playwright + Pytest setup with:

Browser fixtures already implemented

HTML reports

Video, screenshot and trace artifacts on failure

CI-ready configuration and examples

check out:

QA Web Starter Kit PRO (Playwright + Pytest)
→ https://tyrengman.gumroad.com/l/QAKITPRO