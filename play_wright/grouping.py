import pytest

# run only smoke tests: pytest -m smoke
@pytest.mark.smoke
def test_smoke1():
    print("smoke2")

@pytest.mark.smoke
def test_smoke2():
    print("smoke3")