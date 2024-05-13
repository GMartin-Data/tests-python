import pytest

import source.shapes as shapes
import source.school as school


@pytest.fixture
def rectangle_factory():
    def create_rectangle(length, width) -> shapes.Rectangle:
        return shapes.Rectangle(length=length, width=width)
    return create_rectangle

@pytest.fixture
def my_circle():
    return shapes.Circle(10)

@pytest.fixture
def student_factory():
    def create_student(student_id, name) -> school.Student:
        return school.Student(student_id=student_id, name=name)
    return create_student

@pytest.fixture
def course_factory():
    def create_course(course_id, title) -> school.Course:
        return school.Course(course_id=course_id, title=title)
    return create_course

