import pytest


# this file includes all fixtures

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
