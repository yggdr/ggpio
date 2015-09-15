from RPi import GPIO as _GPIO
from .pin import BasicPin, BasicInputPin, BasicOutputPin


class Pin(BasicPin):

    """Docstring for Pin. """

    def __init__(self, gpio, direction, pud=_GPIO.PUD_OFF):
        """TODO: to be defined1.

        :gpio: GPIO pin number
        :direction: Is this an input or an output?
        :pud: Use internal pull-up or pull-down resistor?

        """
        super(Pin, self).__init__(gpio, direction)

        if self.direction.lower() == 'in':
            direction = _GPIO.IN
        elif self.direction.lower() == 'out':
            direction = _GPIO.OUT
        else:
            raise ValueError('Direction must be one of "in" or "out".')

        _GPIO.setup(self.gpio, direction, pud)


class InputPin(BasicInputPin, Pin):

    """Docstring for InputPin. """

    def __init__(self, gpio, pud=None):
        self.pud = pud
        if not self.pud:
            pud = _GPIO.PUD_OFF
        elif self.pud.lower() == 'up':
            pud = _GPIO.PUD_UP
        elif self.pud.lower() == 'down':
            pud = _GPIO.PUD_DOWN
        else:
            raise ValueError(
                'pud must be "up", "down", or an object evaluating to False.')

        super(InputPin, self).__init__(gpio, pud=pud)

    def read(self):
        return _GPIO.input(self.gpio)

    def add_edge_detection(self, type_):
        """Set up channel to detect state change

        :type_: TODO
        :returns: TODO

        """
        TYPE = {'falling': _GPIO.FALLING, 'rising': _GPIO.RISING, 'both':
                _GPIO.BOTH}
        if type_.lower() not in TYPE:
            raise ValueError("'type_' must be one of {0}".format(TYPE.keys()))
        _GPIO.add_event_detect(self.gpio, TYPE[type_.lower()])

    def remove_edge_detection(self):
        """Remove edge detection for this channel
        :returns: TODO

        """
        _GPIO.remove_event_detect(self.gpio)

    def edge_detected(self):
        """Whether an edge of the previously specified type was detected
        :returns: TODO

        """
        return _GPIO.event_detected(self.gpio)

    def add_edge_callback(self, callback, type_=None):
        """Adds a callback to execute as soon as an edge was detected

        :callback: TODO
        :type_: TODO
        :returns: TODO

        """
        if type_:
            self.add_edge_detection(type_)
        _GPIO.add_event_callback(self.gpio, callback)


class OutputPin(BasicOutputPin, Pin):

    """Docstring for InputPin. """

    def __init__(self, gpio):
        super(OutputPin, self).__init__(gpio, 'out')

    def high(self):
        _GPIO.output(self.gpio, _GPIO.HIGH)

    def low(self):
        _GPIO.output(self.gpio, _GPIO.LOW)

    @property
    def state(self):
        return _GPIO.input(self.gpio)

    def toggle(self):
        _GPIO.output(self.gpio, not self.state)


def init(numberscheme='bcm'):
    """docstring for init"""
    if numberscheme.lower() == 'bcm':
        _GPIO.setmode(_GPIO.BCM)
    elif numberscheme.lower() == 'board':
        _GPIO.setmode(_GPIO.BOARD)
    else:
        raise ValueError('numberscheme must be "bcm" or "board".')


def cleanup():
    """docstring for cleanup"""
    _GPIO.cleanup()
