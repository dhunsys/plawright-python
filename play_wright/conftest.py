import pytest
#register to store cmd line parameter
def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )

#global variable(fixture) is request
@pytest.fixture(scope="session")
def create_page(playwright,request):
    browser_name=request.config.getoption("browser_name")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()