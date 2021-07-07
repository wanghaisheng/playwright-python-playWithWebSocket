import contextlib
import typing
from playwright.sync_api import sync_playwright, Browser, BrowserType, Page


@contextlib.contextmanager
def playwright_browser(browser_type, **launch_params) -> typing.ContextManager[Browser]:
    with sync_playwright() as playwright:
        _browser_type: BrowserType = getattr(playwright, browser_type)
        browser = _browser_type.launch(**launch_params)
        try:
            yield browser
        finally:
            browser.close()


with playwright_browser('chromium', headless=False) as browser:
    page: Page = browser.new_page()
    page.goto('https://github.com/YusukeIwaki')
    page.screenshot(path='YusukeIwaki.png')

with playwright_browser('firefox', headless=False) as browser:
    page: Page = browser.new_page()
    page.goto('https://github.com/microsoft')
    page.screenshot(path='microsoft.png')
