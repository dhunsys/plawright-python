import time

from playwright.sync_api import Page, Playwright, expect

import time

from playwright.sync_api import Page, Playwright, expect


def test_verify_hover(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    # get frame
    page.locator("#menuItem").hover()
    # takes time to show submenu so put wait
    expect(page.locator("#submenu")).to_be_visible(timeout=5000)
    page.close()

