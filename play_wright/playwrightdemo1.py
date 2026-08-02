from playwright.sync_api import Page, Playwright


#use 'play_wright' fixture in parameter
def test_playwrightDemo1(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/")
    assert "Playwright" in page.title()
    browser.close()


#use 'page' fixture in parameter. But settings on chromium or choosing browser is issue
def test_usingPageFixture(page):
    page.goto("https://playwright.dev/")
    assert "Playwright" in page.title()
    page.close()


#use 'page' fixture in parameter. But settings on chromium or choosing browser is issue
def test_usingPageFixtureAndSuggestion(page: Page):
    page.goto("https://playwright.dev/")
    assert "Playwright" in page.title()
    page.close()


#use 'play_wright' fixture in parameter. play_wright: Playwright means play_wright argument will be a Playwright instance
def test_playwrightDemo2(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    assert "Playwright" in page.title()
    browser.close()
