import pytest

import source.shapes as shapes


def test_area(rectangle_factory):
    assert rectangle_factory(10, 20).area() == 10 * 20

def test_perimeter(rectangle_factory):
    assert rectangle_factory(10, 20).perimeter() == 2*20 + 2*10

def test_not_eq(rectangle_factory):
    assert rectangle_factory(10, 20) != rectangle_factory(30, 15)
