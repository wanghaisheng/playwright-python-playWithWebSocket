from with_playwright_browser import playwright_browser
from playwright.sync_api import Page

with playwright_browser('chromium') as browser:
    page: Page = browser.new_page()
    page.goto('https://github.com/YusukeIwaki')
    page.screenshot(path='YusukeIwaki.png')

with playwright_browser('firefox') as browser:
    page: Page = browser.new_page()
    page.goto('https://github.com/microsoft')
    page.screenshot(path='microsoft.png')
