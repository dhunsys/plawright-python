import pytest


 # use fixture 'initBrowser' (defined in conftest.py), by passing its name as argument in test
def test_test1(initBrowser):
    print("Running test1")
