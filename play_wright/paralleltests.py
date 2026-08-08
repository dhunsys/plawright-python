import pytest

#install pip install pytest-xdist
#run command: pytest -n 3-> run 3 tests in parallel
def test_1():
    print("1")

def test_2():
    print("2")
def test_3():
    print("3")
def test_4():
    print("4")