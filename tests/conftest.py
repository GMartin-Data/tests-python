import pytest

import source.shapes as shapes


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(20, 10)

@pytest.fixture
def another_rectangle():
    return shapes.Rectangle(30, 15)

@pytest.fixture
def my_circle():
    return shapes.Circle(10)
