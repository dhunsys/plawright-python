import time

from playwright.sync_api import Page, Playwright, expect

import time

from playwright.sync_api import Page, Playwright, expect


def test_verify_alert(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    # get frame
    frame=page.frame_locator("body > iframe")
    frame.locator("#username").fill("python")
    expect(frame.get_by_role("button",name="Submit")).to_be_visible()
    page.wait_for_timeout(3000)
    page.close()

