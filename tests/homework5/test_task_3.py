from homework5.task3 import sum_of_2


def test_decorator_that_writes_string_before_the_func():
    assert sum_of_2(1, 1) == "hehe 2"
