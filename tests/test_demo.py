# test_example.py
import pytest
from demo import add, subtract, divide, sayHello

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1
    assert subtract(-1, -1) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert round(divide(1, 3), 5) == 0.33333
    with pytest.raises(ValueError):
        divide(1, 0)

def test_sayHello():
    assert sayHello('Subhajit') == 'Hello Subhajit'
