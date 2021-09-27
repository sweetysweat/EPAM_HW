import datetime
from unittest.mock import MagicMock

import pytest

from homework6.task_2_oop2 import Homework, HomeworkResult, Student, Teacher

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
