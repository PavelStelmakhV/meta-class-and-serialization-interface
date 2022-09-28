# Домашнее задание
# Напишите классы сериализации контейнеров с данными Python в json, bin файлы. Сами классы должны соответствовать
# общему интерфейсу (абстрактному базовому классу) SerializationInterface.
# Напишите класс метакласс Meta, который всем классам, для кого он будет метаклассом, устанавливает порядковый номер.
# Код для проверки правильности решения:


class Meta(type):
    children_number = 0

    def __new__(mcs, name, bases, namespace, *args, **kwargs):
        instance = super().__new__(mcs, name, bases, namespace)
        instance.class_number = mcs.children_number
        mcs.children_number += 1
        return instance

    @classmethod
    def __prepare__(msc, name, bases, **kwargs):
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


if __name__ == '__main__':

    assert (Cls1.class_number, Cls2.class_number) == (0, 1)
    a, b = Cls1(''), Cls2('')
    assert (a.class_number, b.class_number) == (0, 1)
