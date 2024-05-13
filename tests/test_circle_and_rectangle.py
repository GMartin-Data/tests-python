import pytest

import source.shapes as shapes





def test_not_the_same_area(my_rectangle, my_circle):
    assert my_rectangle.area() != my_circle.area()
