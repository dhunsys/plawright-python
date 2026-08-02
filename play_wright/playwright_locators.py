from playwright.sync_api import Page, expect


def test_label(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    page.get_by_label("Name:").fill("Shahab")
    page.get_by_label("Password:").fill("password")
    page.wait_for_timeout(5000)
    page.close()


def test_role(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    page.get_by_role("button", name="Show Alert").click()
    page.get_by_role("checkbox", name="Reading").check()
    page.wait_for_timeout(5000)
    page.close()


def test_placeholder(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    page.get_by_placeholder("Enter text").fill("MS")
    page.get_by_placeholder("Enter email").fill("abc@gmail.com")
    page.get_by_placeholder("Enter number").fill("123")
    page.wait_for_timeout(5000)
    page.close()


def test_static_dropdown_visible_text(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    page.locator("#countryDropdown").scroll_into_view_if_needed()
    page.locator("#countryDropdown").select_option('India')
    page.wait_for_timeout(5000)
    page.close()


def test_static_dropdown_value_attr(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    page.locator("#countryDropdown").scroll_into_view_if_needed()
    page.locator("#countryDropdown").select_option(value="India")
    page.wait_for_timeout(5000)
    page.close()


def test_static_dropdown_index(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    page.locator("#countryDropdown").scroll_into_view_if_needed()
    page.locator("#countryDropdown").select_option(index=3)
    page.wait_for_timeout(5000)
    page.close()


def test_static_dropdown_multi_select(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    page.locator("#multiSelect").scroll_into_view_if_needed()
    page.locator("#multiSelect").select_option(["java", "Python"])
    page.wait_for_timeout(5000)
    page.close()


def test_static_dropdown_get_all_text(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    page.locator("#countryDropdown").scroll_into_view_if_needed()
    options = page.locator("#countryDropdown option").all_text_contents()
    assert len(options) > 0
    print("list items", options)
    for o in options:
        print("Item is :", o)
    page.wait_for_timeout(5000)
    page.close()


def test_static_dropdown_contains_text(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    page.locator("#countryDropdown").scroll_into_view_if_needed()
    options = page.locator("#countryDropdown option").all_text_contents()
    assert "India1" not in options
    assert "India" in options
    page.wait_for_timeout(5000)
    page.close()

def test_verify_option_sorted(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    page.locator("#countryDropdown").scroll_into_view_if_needed()
    # Collect all option texts
    options = page.locator("#countryDropdown option").all_text_contents()
    # Assert "India1" is not present
    assert "India1" not in options, "Unexpected option found in dropdown!"
    # Create a sorted copy of the list
    sorted_options = sorted(options)
    # Print both lists
    print("Original list:", options)
    print("Sorted list:", sorted_options)
    # Assert that the original list is already sorted
    assert options == sorted_options, "Dropdown options are not sorted!"
    page.wait_for_timeout(3000)
    page.close()
