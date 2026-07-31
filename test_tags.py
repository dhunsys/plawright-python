import pytest

#use tag
@pytest.mark.smoke
def test_test6():
    print("Running test6 with tag name")


#use tag
@pytest.mark.regression
def test_test7():
    print("Running test7 with tag name")
