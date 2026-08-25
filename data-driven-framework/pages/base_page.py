from playwright.sync_api import Page


class BasePage:
    """Common actions shared by every page object.

    Page objects should only expose business-meaningful methods
    (login, add_to_cart, ...). Low-level Playwright calls live here
    so locator/wait strategy can change in one place.
    """

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()

    def wait_for(self, locator: str, state: str = "visible", timeout: int = 5000):
        self.page.locator(locator).wait_for(state=state, timeout=timeout)
