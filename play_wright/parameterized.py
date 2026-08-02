import pytest
from playwright.sync_api import Page, expect
from test_data import CHECKBOX_VALUES

@pytest.mark.parametrize("value", ["reading", "traveling", "sports"])
def test_checkboxes_by_value(page: Page, value):
    page.goto("https://testingsrc.blogspot.com/")
    checkbox = page.locator(f"input[type='checkbox'][value='{value}']")
    checkbox.check()
    expect(checkbox).to_be_checked()


@pytest.mark.parametrize("checkbox", CHECKBOX_VALUES)
def test_checkboxes_by_dict(page: Page, checkbox):
    page.goto("https://testingsrc.blogspot.com/")

    # Use the dictionary values
    attr_value = checkbox["attr_value"]
    label = checkbox["label"]

    # Locate checkbox by its value attribute
    locator = page.locator(f"input[type='checkbox'][value='{attr_value}']")
    locator.check()

    # Verify it's checked
    expect(locator).to_be_checked()

    print(f"Checked checkbox with value='{attr_value}' and label='{label}'")

    page.wait_for_timeout(1000)
    page.close()
