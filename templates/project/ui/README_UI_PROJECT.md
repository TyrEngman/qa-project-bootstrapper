# UI Automation Project (Playwright + Pytest)

## Quick start

1) Create and activate a virtual environment
```bash
python -m venv .venv
Install dependencies


pip install -r requirements.txt
python -m playwright install
Run tests


pytest
What you get
Playwright + Pytest ready to run

A real example test (opens a page and checks the title)

Minimal Page Object structure to scale



### 4) `templates/project/ui/tests/ui/pages/base_page.py`
```python
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str) -> None:
        self.page.goto(url, wait_until="domcontentloaded")
5) templates/project/ui/tests/ui/pages/example_page.py

from playwright.sync_api import Page, expect
from .base_page import BasePage


class ExamplePage(BasePage):
    URL = "https://example.com/"

    def open_default(self) -> None:
        self.open(self.URL)

    def expect_title(self) -> None:
        # "Example Domain" es estable y normalmente no cambia.
        expect(self.page).to_have_title("Example Domain")
6) templates/project/ui/tests/ui/test_example_ui.py

from tests.ui.pages.example_page import ExamplePage


def test_example_domain_title(page):
    p = ExamplePage(page)
    p.open_default()
    p.expect_title()