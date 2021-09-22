from homework5.task2 import custom_sum


def test_custom_wrapper_to_get_info_about_the_custom_sum():
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"
    assert custom_sum.__name__ == 'custom_sum'
    assert not custom_sum.__original_func == custom_sum
