import datetime
from unittest.mock import MagicMock

import pytest

from homework6.task_2_oop2 import (DeadlineError, Homework, HomeworkResult,
                                   Student, Teacher)

date_and_time_for_tests = datetime.datetime(2021, 9, 5, 15, 7, 13, 123456)


@pytest.fixture(autouse=True)
def patch_datetime_now(monkeypatch):
    datetime_mock = MagicMock(wraps=datetime.datetime)
    datetime_mock.now.return_value = date_and_time_for_tests
    monkeypatch.setattr(datetime, "datetime", datetime_mock)


def test_student_attr():
    student = Student('Roman', 'Petrov')
    assert student.first_name == 'Roman'
    assert student.last_name == 'Petrov'


def test_teacher_attr():
    teacher = Teacher('Daniil', 'Shadrin')
    assert teacher.first_name == 'Daniil'
    assert teacher.last_name == 'Shadrin'
    assert len(teacher.homework_done) == 0


def test_homework_attr():
    homework = Homework('task', 5)
    assert homework.homework_name == "task"
    assert homework.deadline == datetime.timedelta(days=5)
    assert homework.created == date_and_time_for_tests


def test_homework_result_attr():
    student = Student('Roman', 'Petrov')
    homework = Homework('task', 5)
    check_homework = HomeworkResult(homework, 'I did my task', student)
    assert check_homework.created == date_and_time_for_tests
    assert check_homework.homework == homework
    assert check_homework.author == student
    assert check_homework.solution == 'I did my task'


def test_homework_methods():
    homework_positive_case = Homework("task", 5)
    homework_negative_case = Homework("task", 0)
    assert homework_positive_case.is_active()
    assert not homework_negative_case.is_active()


def test_homework_result_exception():
    student = Student('Roman', 'Petrov')
    with pytest.raises(Exception):
        HomeworkResult(student, 'qwe', student)


def test_student_methods():
    student = Student('Roman', 'Petrov')
    homework = Homework("task0", 5)
    homework_to_test_exception = Homework("task", 0)
    assert isinstance(student.do_homework(homework, "I did it!"), HomeworkResult)
    with pytest.raises(DeadlineError):
        student.do_homework(homework_to_test_exception, "I did it!")


def test_teacher_methods():
    teacher = Teacher('Daniil', 'Shadrin')
    created_homework = teacher.create_homework('OOP task', 5)
    assert isinstance(created_homework, Homework)
    student = Student('Roman', 'Petrov')
    bad_student = Student('Andrew', 'Ursegov')
    students_homework = student.do_homework(created_homework, "I did it!")
    bad_students_homework = bad_student.do_homework(created_homework, "did")
    assert teacher.check_homework(students_homework)  # сдано вовремя
    assert not teacher.check_homework(bad_students_homework)  # просрочено
    created_homework1 = teacher.create_homework('OOP task2', 5)
    students_new_homework = student.do_homework(created_homework1, "I did it!!!!!")
    teacher.check_homework(students_new_homework)
    teacher.reset_results(created_homework)  # удалим created_homework
    assert created_homework not in teacher.homework_done
    assert not teacher.reset_results()  # полное удаление
    assert not teacher.homework_done  # проверим, что все удалилось
