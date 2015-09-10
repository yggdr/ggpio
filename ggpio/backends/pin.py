from abc import ABCMeta, abstractmethod, abstractproperty


class BasicPin(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, gpio, direction):
        self.gpio = gpio
        self.direction = direction

    def __str__(self):
        return str(self.gpio)

    def __repr__(self):
        return str(self.gpio)


class BasicInputPin(BasicPin):

    """docstring for InputPin"""
    @abstractmethod
    def read(self):
        raise NotImplemented


class BasicOutputPin(BasicPin):

    """docstring for OutputPin"""
    @abstractmethod
    def high(self):
        raise NotImplemented

    @abstractmethod
    def low(self):
        raise NotImplemented

    @abstractproperty
    def state(self):
        raise NotImplemented
