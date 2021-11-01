from homework11.hw_11_task_2 import Order


def morning_discount(price):
    return price * 0.75


def elder_discount(price):
    return price * 0.1


def test_Order():
    purchase_without_discount = Order(100)
    assert purchase_without_discount.final_price() == 100

    purchase_with_morning_discount = Order(100, morning_discount)
    assert purchase_with_morning_discount.final_price() == 75

    purchase_with_morning_discount = Order(100, elder_discount)
    assert purchase_with_morning_discount.final_price() == 10
