import pytest

import pytest
from playwright.sync_api import sync_playwright

# register to listent comd line argument --browser,--headed,--device are built in so no need to register
def pytest_addoption(parser):
    # parser.addoption(
    #     "--browser",
    #     action="store",
    #     default="chromium",
    #     help="Browser to run tests against"
    # )
    parser.addoption(
        "--api-url",
        action="store",
        default="https://rahulshettyacademy.com",
        help="API Base URL"
    )

@pytest.fixture
def api_context(playwright,request):
    base_url = request.config.getoption("--api-url")
    request_context = playwright.request.new_context(base_url=base_url)
    yield request_context
    request_context.dispose()

#return --browser passed in cmd line to test using this fixture
@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser")

#return --web_url passed in cmd line to test using this fixture
@pytest.fixture(scope="session")
def web_url(request):
    return request.config.getoption("--web_url")

# call fixture to get browser_name
@pytest.fixture(scope="session")
def browser(browser_name):
    with sync_playwright() as p:
        print(f"Fixture value: {browser_name}")
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=False)

        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=False)

        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=False)

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        yield browser # stop till the consumer returns then close

        browser.close()

#call above fixture browser, and get browser object. scope is function so that if a test runs more than once with different data, new page is created for each
#always function scope in parallel
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()

    yield page # stop till caller finish and close

    context.close()



    #--------------------------End of try---------------

# this file includes all fixtures
@pytest.fixture
def initBrowser(): #default scope
    print("To initialize browser")

@pytest.fixture(scope="function")  # default scope. runs per test
def defaultScope():
    print("To initialize browser here")
    return "pass"


@pytest.fixture(scope="function")  # default scope. runs per test
def defaultScopeYield():
    print("Yieding after this line")
    yield
    print("tear down")


@pytest.fixture(scope="class")  # once for entire class
def classScope():
    print("run only once per class")


@pytest.fixture(scope="module")  # for a sigle file
def moduleScope():
    print("To module scope")


@pytest.fixture(scope="session")  # once for entire suite
def sessionScope():
    print("run only once for entire suite, like before suite in testng")
