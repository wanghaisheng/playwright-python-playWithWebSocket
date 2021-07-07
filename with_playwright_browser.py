import contextlib
import typing
from playwright.sync_api import sync_playwright, Browser, BrowserType


@contextlib.contextmanager
def playwright_browser(browser_type, **launch_params) -> typing.ContextManager[Browser]:
    with sync_playwright() as playwright:
        _browser_type: BrowserType = getattr(playwright, browser_type)
        browser = _browser_type.launch(**launch_params)
        try:
            yield browser
        finally:
            browser.close()
