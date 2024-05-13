import source.shapes as shapes


rectangle = shapes.Rectangle(20, 10)

def test_area():
    assert rectangle.area() == 10 * 20

def test_perimeter():
    assert rectangle.perimeter() == 2*20 + 2*10
