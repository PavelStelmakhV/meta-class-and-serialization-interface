from abc import ABCMeta, abstractmethod
from pathlib import Path
import pickle
import json


class SerializationInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, filename: Path):
        ...

    @abstractmethod
    def load(self):
        ...

    @abstractmethod
    def dump(self, data):
        ...


class SerializationPickle(SerializationInterface):
    def __init__(self, filename: Path='data.bin'):
        self.filename = filename

    def load(self):
        with open(self.filename, "rb") as fh:
            unpacked = pickle.load(fh)
        return unpacked

    def dump(self, data):
        with open(self.filename, "wb") as fh:
            pickle.dump(data, fh)


class SerializationJson(SerializationInterface):
    def __init__(self, filename: Path = 'data.json'):
        self.filename = filename

    def load(self):
        with open(self.filename, "r") as fh:
            unpacked = json.load(fh)
        return unpacked

    def dump(self, data):
        with open(self.filename, "w") as fh:
            json.dump(data, fh)


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

