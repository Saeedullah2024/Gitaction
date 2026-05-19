from src.math_operation import addition , subtraction

def test_add():
    assert addition(2,3) == 5
    assert addition(5,2) == 7

def test_sub():
    assert subtraction(5,5) == 0
    assert subtraction(4,2) == 2

