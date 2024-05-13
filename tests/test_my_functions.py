import time

import pytest

import source.my_functions as smf


def test_add_pass():
    assert smf.add(1, 4) == 5

def test_add_fail():
    assert not smf.add(1, 2) == 4

def test_add_str():
    assert smf.add("Bou", "din") == "Boudin"   

def test_divide_pass():
    assert smf.divide(6, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        smf.divide(number_one=10, number_two=0)

def test_multiply_positives():
    assert smf.multiply(2, 3) == 6

def test_multiply_negatives():
    assert smf.multiply(-2, -3) == 6

def test_multiply_mixed():
    assert smf.multiply(-2, 3) == -6

def test_multiply_zero():
    assert smf.multiply(0, 5) == 0

@pytest.mark.slow
def test_multiply_slow():
    time.sleep(5)
    assert smf.multiply(5, 0) == 0
