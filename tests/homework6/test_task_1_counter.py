from homework6.task_1_counter import instances_counter


@instances_counter
class User:
    pass


@instances_counter
class AnotherUser:
    pass


def test_instances_counter():
    assert User.get_created_instances() == 0
    user1, user2, user3 = User(), User(), User()
    a_user1, a_user2 = AnotherUser(), AnotherUser()
    assert user1.get_created_instances() == 3
    assert a_user1.get_created_instances() == 2
    assert user1.reset_instances_counter() == 3
    assert user1.get_created_instances() == 0
