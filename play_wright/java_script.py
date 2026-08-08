import time


def test_java_script_fill(page):
    page.goto("https://testingsrc.blogspot.com/")
    # Locate the element
    element = page.locator("#textInput")
    # Execute JavaScript click
    time.sleep(4)
    page.evaluate("element => element.value='Hello", element)

def test_java_script_click(page):
    page.goto("https://testingsrc.blogspot.com/")
    # Locate the element
    element = page.locator("#countryDropdown")
    # Execute JavaScript click
    page.evaluate("element => element.click()", element)