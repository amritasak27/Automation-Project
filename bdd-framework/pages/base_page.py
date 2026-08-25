from playwright.sync_api import Page


class BasePage:
    """Common actions shared by every page object (mirrors data-driven-framework's
    base_page.py - same pattern, kept independent per framework)."""

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()
