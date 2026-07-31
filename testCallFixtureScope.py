import pytest


@pytest.fixture(scope="module")  # only once for all test in this file
def onlyOnce():
    print("run only once")


@pytest.fixture(scope="function")  # default scope. runs per test
def initBrowser():
    print("To initialize browser here")


# use fixture 'initBrowser' by passing its name as argument in test
def test_test(initBrowser):
    print("Running test")


def test_test1(initBrowser):
    print("Running test1")


def test_test2(onlyOnce):
    print("Running test2")


def test_test3(onlyOnce):  #fixture onlyOnce will not invoke now. its already invoked once
    print("Running test3")


def test_test4(sessionScope):  #fixture sessionScope is defined in inConfTest.py
    print("Running test4")


#get return value from fixture
def test_test5(defaultScope):  #return value will be stored in fixture name
    print("Running test5 with return value from fixture", defaultScope)
    assert "pass" == defaultScope


#use multiple fixture and yield for tear down
def test_test5(defaultScope, defaultScopeYield):  #return value will be stored in fixture name
    print("Running test5 with return value from fixture", defaultScope)
    assert "pass" == defaultScope


#use tag
@pytest.mark.smoke
def test_test6():
    print("Running test6 with tag name")


#use tag
@pytest.mark.regression
def test_test7():
    print("Running test7 with tag name")
