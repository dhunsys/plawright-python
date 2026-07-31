from playwright.sync_api import Page, Playwright, expect


# from a list of countries, filter one and assert
def test_verify_option_sorted(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    page.locator("#countryDropdown").scroll_into_view_if_needed()
    # Collect all countries
    country = page.locator("#countryDropdown option").filter(has_text="Bangladesh").inner_text()
    assert country == "Bangladesh", "Unexpected option found in dropdown!"
    page.wait_for_timeout(3000)
    page.close()


# from a list of checkbox, filter one and select
def test_verify_check(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    page.locator("//h2[text()='Checkboxes']").scroll_into_view_if_needed()
    # Collect all checkboxes
    # travelling = page.locator("input[type='checkbox']")
    # travelling=travelling.filter(has_text="sports")
    # print(travelling.inner_text())
    # travelling.check()
    # expect(travelling).to_be_checked()
    checkboxes = page.get_by_role("checkbox")
    for i in range(checkboxes.count()):
        cb = checkboxes.nth(i)
        cb.check()
        expect(cb).to_be_checked()
    page.wait_for_timeout(3000)
    page.close()
