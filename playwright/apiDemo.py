import time

from playwright.sync_api import Page, Playwright, expect

from api.apiDemo import APIUtils


def test_verify_api(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    #use API
    api=APIUtils()
    api.createOrder(playwright)
    # page.goto("https://testingsrc.blogspot.com/")
    # # get frame
    # page.locator("#menuItem").hover()
    # # takes time to show submenu so put wait
    # expect(page.locator("#submenu")).to_be_visible(timeout=5000)
    # page.close()

