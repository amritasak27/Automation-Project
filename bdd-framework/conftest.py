import pytest
from playwright.sync_api import sync_playwright

from utils.driver_factory import BrowserFactory
from utils.config_reader import ConfigReader


@pytest.fixture(scope="session")
def config():
    return ConfigReader()


@pytest.fixture(scope="function")
def page(config):
    with sync_playwright() as playwright:
        browser = BrowserFactory.get_browser(
            playwright, config.browser, headless=config.headless
        )
        context = browser.new_context(base_url=config.base_url)
        page = context.new_page()
        yield page
        context.close()
        browser.close()
