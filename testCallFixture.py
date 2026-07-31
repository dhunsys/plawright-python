import pytest


@pytest.fixture
def initBrowser():
    print("To initialize browser here")

 # use fixture 'initBrowser' by passing its name as argument in test
def test_test1(initBrowser):
    print("Running test1")
