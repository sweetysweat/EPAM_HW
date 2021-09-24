"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):


    class Decorated_class(cls):
        cls.count = 0

        def __init__(self, *args, **kwargs):
            cls.count += 1
            cls(*args, **kwargs)

        @staticmethod
        def reset_instances_counter():
            memory = cls.count
            cls.count = 0
            return memory

        @staticmethod
        def get_created_instances():
            return cls.count

    return Decorated_class
