from playwright.sync_api import Playwright, Browser


class BrowserFactory:
    """Factory pattern: same rationale as data-driven-framework/utils/driver_factory.py -
    one place to add new browser targets."""

    @staticmethod
    def get_browser(playwright: Playwright, browser_name: str, headless: bool = True) -> Browser:
        browser_name = browser_name.lower()
        if browser_name == "chromium":
            return playwright.chromium.launch(headless=headless)
        elif browser_name == "firefox":
            return playwright.firefox.launch(headless=headless)
        elif browser_name == "webkit":
            return playwright.webkit.launch(headless=headless)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
