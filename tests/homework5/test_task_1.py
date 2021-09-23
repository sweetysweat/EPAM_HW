import datetime
from unittest.mock import MagicMock

import pytest

from homework5.task1 import Homework, Student, Teacher

date_and_time_for_tests = datetime.datetime(2021, 9, 5, 15, 7, 13, 123456)


@pytest.fixture(autouse=True)
def patch_datetime_now(monkeypatch):
    datetime_mock = MagicMock(wraps=datetime.datetime)
    datetime_mock.now.return_value = date_and_time_for_tests
    monkeypatch.setattr(datetime, "datetime", datetime_mock)


def test_student_attr():
    student = Student("Andrew", "Ursegov")
    assert student.first_name == "Andrew"
    assert student.last_name == "Ursegov"


def test_homework_attr():
    homework = Homework("task", 5)
    assert homework.homework_name == "task"
    assert homework.deadline == datetime.timedelta(days=5)
    assert homework.created == date_and_time_for_tests


def test_homework_is_active_negative_case():
    homework = Homework("task", 0)
    assert not homework.is_active()


def test_homework_is_active_positive_case():
    homework = Homework("task", 1)
    assert homework.is_active()


def test_teacher_attr():
    teacher = Teacher("Helen", "Gray")
    assert teacher.first_name == "Helen"
    assert teacher.last_name == "Gray"
