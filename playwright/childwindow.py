from playwright.sync_api import Page, Playwright, expect


# open google in new tab, switch to new tab and check title
def test_switch_child_window(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    with page.expect_popup() as tab:
        # action to open new window
        page.get_by_role("link", name="Open google.com in New Tab").click()
        childPage = tab.value
        childPage.wait_for_load_state()
        title = childPage.title()
        assert title == "Google"
    page.wait_for_timeout(3000)
    page.close()
