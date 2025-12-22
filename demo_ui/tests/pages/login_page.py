class LoginPage:
    """Example Page Object skeleton for ui tests.

    Replace the methods below with real interactions using Playwright,
    Selenium, or any other browser automation library.
    """

    def __init__(self, page) -> None:
        """`page` can be a Playwright/Selenium driver or similar."""
        self.page = page

    def open(self) -> None:
        """Open the login page.

        TODO: implement real navigation here.
        """
        raise NotImplementedError("Implement LoginPage.open() with real ui actions")

    def login(self, username: str, password: str) -> None:
        """Fill the login form and submit.

        TODO: implement real locators and actions here.
        """
        raise NotImplementedError("Implement LoginPage.login() with real ui actions")
