import contextlib
import typing
from playwright_remote.sync_api import sync_playwright_remote
from playwright.sync_api import Browser, BrowserType
import os


@contextlib.contextmanager
def playwright_browser(browser_type, **launch_params) -> typing.ContextManager[Browser]:
    ws_endpoint = os.getenv('PLAYWRIGHT_WS_URL', 'ws://127.0.0.1:8080/ws')
    with sync_playwright_remote(ws_endpoint) as playwright:
        _browser_type: BrowserType = getattr(playwright, browser_type)
        browser = _browser_type.launch(**launch_params)
        try:
            yield browser
        finally:
            browser.close()
