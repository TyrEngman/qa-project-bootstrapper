# QA UI Starter — Generated Project

This project was generated using the **QA Project Bootstrapper** with the `ui` preset.

It is a clean starting point for **web UI test automation**.  
You can plug in tools like **Playwright**, **Selenium** or **Playwright + Pytest** (recommended).

---

## 1. Tech stack (suggested)

Out of the box you get a **pytest** skeleton.  
You can choose your UI engine:

- ✅ **Playwright + Pytest** (modern, fast, powerful)
- ✅ Selenium / SeleniumBase
- ✅ Any other browser automation library you prefer

> This preset focuses on folder structure and test layout.  
> You are free to install the UI automation library that best fits your project.

---

## 2. Project structure

```text
your-ui-project/
├─ tests/
│  ├─ __init__.py
│  └─ test_sample.py          # Example placeholder test
├─ pytest.ini                 # Basic pytest configuration
├─ requirements.txt           # Python dependencies
└─ README.md                  # You are here
A typical Playwright-based layout could look like:


tests/
├─ pages/
│  ├─ home_page.py
│  └─ login_page.py
├─ flows/
│  └─ user_login_flow.py
├─ test_login.py
└─ test_smoke_navigation.py
3. Getting started
3.1. Create and activate virtualenv

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
3.2. Install dependencies
At minimum:


pip install -r requirements.txt
If you want to use Playwright + Pytest, install:


pip install playwright pytest-playwright
playwright install
For Selenium:


pip install selenium
(Add these to requirements.txt if they will be used by the team.)

3.3. Run tests

pytest -v
If you use pytest markers (e.g. smoke):


pytest -m smoke -v
4. Turning this into a real UI automation suite
Some recommendations:

Adopt a pattern

Page Object Model (tests/pages/)

Flows or “screenplay” style (tests/flows/)

Create reusable fixtures in conftest.py

Browser / page lifecycle

Login sessions

Base URL, environment selection (DEV, QA, STAGE, etc.)

Add markers

@pytest.mark.smoke for fast checks

@pytest.mark.regression for full suites

@pytest.mark.slow for heavy scenarios

Integrate with CI
Run UI tests on every PR or at least nightly:

GitHub Actions

GitLab CI

Azure Pipelines / Jenkins

5. Example: minimal Playwright-style test


import pytest

@pytest.mark.smoke
def test_ui_sample_placeholder():
    # Replace this with your real UI scenario:
    # e.g. open page, log in, assert something visible
    assert True
Once you wire Playwright’s fixtures, this could evolve to:



def test_home_page_title(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
6. Recommended next steps
Decide which UI engine you'll use (Playwright, Selenium, etc.).

Install the necessary libraries and update requirements.txt.

Add your first real smoke scenario:

open app

log in (if needed)

assert a key element / title / widget

Define a folder convention and stick to it.

7. About the generator
This project was created with:

QA Project Bootstrapper
Quickly scaffold QA projects with presets for:

default (pytest basics)

api

ui

If you want a production-ready Playwright + Pytest framework (traces, HTML reports, artifacts, CI-ready), check out:

QA Web Starter Kit PRO (Playwright + Pytest)
👉 https://tyrengman.gumroad.com/l/QAKITPRO