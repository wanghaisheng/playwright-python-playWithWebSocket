import contextlib
import typing
from playwright_remote_context_manager import sync_playwright_remote
from playwright.sync_api import Browser, BrowserType


@contextlib.contextmanager
def playwright_browser(browser_type, **launch_params) -> typing.ContextManager[Browser]:
    with sync_playwright_remote('ws://127.0.0.1:8080/ws') as playwright:
        _browser_type: BrowserType = getattr(playwright, browser_type)
        browser = _browser_type.launch(**launch_params)
        try:
            yield browser
        finally:
            browser.close()
