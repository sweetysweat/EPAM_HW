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

    class AddNewMethods(cls):
        count = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, ** kwargs)
            self.increment_instances_counter()

        @classmethod
        def increment_instances_counter(cls):
            cls.count += 1

        @classmethod
        def reset_instances_counter(cls):
            memory = cls.count
            cls.count = 0
            return memory

        @classmethod
        def get_created_instances(cls):
            return cls.count

    return AddNewMethods
