from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def click_first(self, locator: str):
        self.page.locator(locator).first.click()

    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()

    def wait_for_visible(self, locator: str, timeout: int = 10000) -> bool:
        """Waits up to `timeout` ms for the element to become visible,
        instead of checking instantly. Use this after any action that
        triggers navigation or async UI updates (login, form submit, etc.)."""
        try:
            self.page.locator(locator).wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False