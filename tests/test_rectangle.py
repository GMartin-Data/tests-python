import pytest

import source.shapes as shapes


def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2*20 + 2*10

def test_not_eq(my_rectangle, another_rectangle):
    assert my_rectangle != another_rectangle
