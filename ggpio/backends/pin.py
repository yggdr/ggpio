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
        raise NotImplementedError

    @abstractmethod
    def add_edge_detection(self):
        raise NotImplementedError

    @abstractmethod
    def remove_edge_detection(self):
        raise NotImplementedError

    @abstractmethod
    def edge_detected(self):
        raise NotImplementedError

    @abstractmethod
    def add_edge_callback(self):
        raise NotImplementedError


class BasicOutputPin(BasicPin):

    """docstring for OutputPin"""
    @abstractmethod
    def high(self):
        raise NotImplementedError

    @abstractmethod
    def low(self):
        raise NotImplementedError

    @abstractproperty
    def state(self):
        raise NotImplementedError

    @abstractmethod
    def toggle(self):
        raise NotImplementedError
