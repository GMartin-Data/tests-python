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
