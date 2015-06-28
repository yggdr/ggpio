from RPi import GPIO as _GPIO
import pin


class Pin(pin.Pin):

    """Docstring for Pin. """

    def __init__(self, gpio, direction, pud=None):
        """TODO: to be defined1.

        :gpio: TODO
        :direction: TODO
        :pud: TODO

        """
        super(Pin, self).__init__()
        self.pud = pud

        if self.direction.lower() == 'in':
            direction = _GPIO.IN
        elif self.direction.lower() == 'out':
            direction = _GPIO.OUT
        else:
            raise ValueError

        if self.pud is None:
            pud = _GPIO.PUD_  # TODO
        elif self.pud.lower() == 'up':
            pud = _GPIO.PUD_UP
        elif self.pud.lower() == 'down':
            pud = _GPIO.PUD_DOWN
        else:
            raise ValueError

        _GPIO.setmode(self.gpio, direction, pud)


class InputPin(pin.InputPin, Pin):

    """Docstring for InputPin. """

    def read(self):
        return _GPIO.input(self.gpio)


class OutputPin(pin.OutputPin, Pin):

    """Docstring for InputPin. """

    def high(self):
        _GPIO.output(self.gpio, _GPIO.HIGH)

    def low(self):
        _GPIO.output(self.gpio, _GPIO.LOW)


def init(numberscheme='bcm'):
    """docstring for init"""
    if numberscheme.lower() == 'bcm':
        _GPIO.setup(_GPIO.BCM)
    elif numberscheme.lower() == 'board':
        _GPIO.setup(_GPIO.BOARD)
    else:
        raise ValueError


def cleanup():
    """docstring for cleanup"""
    _GPIO.cleanup()
