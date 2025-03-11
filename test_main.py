from main import add, mul


def test_add():
    assert add(2, 3) == 5
    assert add(10, 10) == 20
    assert add(5, 5) != 5


def test_mul():
    assert mul(2, 2) == 4
    assert mul(2, 10) == 20
    assert mul(10, 10) != 10
