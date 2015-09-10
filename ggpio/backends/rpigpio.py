from RPi import GPIO as _GPIO
from .pin import BasicPin, BasicInputPin, BasicOutputPin


class Pin(BasicPin):

    """Docstring for Pin. """

    def __init__(self, gpio, direction, pud=None):
        """TODO: to be defined1.

        :gpio: GPIO pin number
        :direction: Is this an input or an output?
        :pud: Use internal pull-up or pull-down resistor?

        """
        super(Pin, self).__init__()
        self.pud = pud

        if self.direction.lower() == 'in':
            direction = _GPIO.IN
        elif self.direction.lower() == 'out':
            direction = _GPIO.OUT
        else:
            raise ValueError('Direction must be one of "in" or "out".')

        if not self.pud:
            pud = _GPIO.PUD_OFF
        elif self.pud.lower() == 'up':
            pud = _GPIO.PUD_UP
        elif self.pud.lower() == 'down':
            pud = _GPIO.PUD_DOWN
        else:
            raise ValueError(
                'pud must be "up", "down", or an object evaluating to False.')

        _GPIO.setmode(self.gpio, direction, pud)


class InputPin(BasicInputPin, Pin):

    """Docstring for InputPin. """

    def read(self):
        return _GPIO.input(self.gpio)


class OutputPin(BasicOutputPin, Pin):

    """Docstring for InputPin. """

    def high(self):
        _GPIO.output(self.gpio, _GPIO.HIGH)

    def low(self):
        _GPIO.output(self.gpio, _GPIO.LOW)

    def state(self):
        return _GPIO.input(self.gpio)


def init(numberscheme='bcm'):
    """docstring for init"""
    if numberscheme.lower() == 'bcm':
        _GPIO.setup(_GPIO.BCM)
    elif numberscheme.lower() == 'board':
        _GPIO.setup(_GPIO.BOARD)
    else:
        raise ValueError('numberscheme must be "bcm" or "board".')


def cleanup():
    """docstring for cleanup"""
    _GPIO.cleanup()
