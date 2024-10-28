import pytest
from playwright.sync_api import Browser, BrowserContext, Page
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as playwright:
        browser: Browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        context: BrowserContext = browser.new_context(no_viewport=True)

        page: Page = context.new_page()
        yield page

        context.close()
        browser.close()
