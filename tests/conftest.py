import pytest

import source.shapes as shapes


@pytest.fixture
def rectangle_factory():
    def create_rectangle(length, width) -> shapes.Rectangle:
        return shapes.Rectangle(length=length, width=width)
    return create_rectangle

@pytest.fixture
def my_circle():
    return shapes.Circle(10)
