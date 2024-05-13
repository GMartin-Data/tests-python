import pytest

import source.school as school


def test_add_student(course_factory, student_factory):
    course = course_factory(course_id=1, title="History")
    student = student_factory(student_id=1, name="François Ier")
    course.add_student(student)
    assert student in course.students


def test_count_student(course_factory, student_factory):
    course1 = course_factory(course_id=2, title="DevIA")
    course2 = course_factory(course_id=3, title="Centre aéré pour les seniors")
    students_names_c1 = ["Tibo", "Farid", "Sensei", "Greg"]
    students_names_c2 = ["Alphonse", "Gisèle", "Hervé", "Serge", "Marinette", "Greg"]  # ;)
    for idx, student_name in enumerate(students_names_c1, 1):
        student = student_factory(student_id=idx, name=student_name)
        course1.add_student(student)
    for idx, student_name in enumerate(students_names_c2, 1):
        student = student_factory(student_id=idx, name=student_name)
        course2.add_student(student)        
    assert len(course1.students) == 4
    assert len(course2.students) == 6
