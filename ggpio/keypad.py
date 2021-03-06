from collections import namedtuple
import time
from .errors import TimeoutError

_infinity = float('inf')


class Keypad(object):
    """docstring for Keypad"""

    presets = {'1x' + str(i - 1): list(range(1, i)) for i in range(3, 9)}
    presets.update({
        '3x4': (
            ('1', '2', '3'),
            ('4', '5', '6'),
            ('7', '8', '9'),
            ('*', '0', '#')
        ),
        '4x4': (
            ('1', '2', '3', 'A'),
            ('4', '5', '6', 'B'),
            ('7', '8', '9', 'C'),
            ('*', '0', '#', 'D')
        )
    })

    def __init__(self, rowpins, colpins, layout, scanning=True, rowsareinput=True,
                 outishigh=True):
        self.rowsareinput = rowsareinput
        inputpins, outputpins = (
            rowpins, colpins) if self.rowsareinput else (colpins, rowpins)
        self.pins = namedtuple('Pins', ['rows', 'cols', 'input', 'output'])(
            rows=rowpins, cols=colpins, input=inputpins, output=outputpins)
        self.layout = self.presets.get(layout, layout)
        self.scanning = scanning
        self.outishigh = outishigh

        if len(self.layout) != len(self.pin.rows):
            raise ValueError("Layout doesn't fit")
        for row in self.layout:
            if len(row) != len(self.pin.cols):
                raise ValueError("Layout doesn't fit")

        self._setuppins()

    def _setuppins(self):
        for pin in self.pins.output:
            if self.outishigh:
                pin.high()
            else:
                pin.low()

    def _scan(self, start_time, wait_for=_infinity):
        while True:
            for opin in self.pins.output:
                if time.time() - start_time > wait_for:
                    raise TimeoutError('Key entry took longer than specified')
                opin.toggle()
                for ipin in self.pins.input:
                    if not ipin.read():
                        while not ipin.read():
                            time.sleep(.01)
                            if time.time() - start_time > wait_for:
                                raise TimeoutError(
                                    'Key entry took longer than specified')
                        i1 = self.pins.input.index(ipin)
                        i2 = self.pins.output.index(opin)
                        return self.layout[i1, i2] if self.rowsareinput else self.layout[i2, i1]
                opin.toggle()

    def read(self, numpresses, wait_for=_infinity, error_on_timeout=False):
        readstr = ''
        start_time = time.time()
        try:
            for i in range(numpresses):
                readstr += self._scan(start_time, wait_for=wait_for)
        except TimeoutError:
            if error_on_timeout:
                raise
            return None
        finally:
            # Always reset the pins
            self._setuppins()
        return readstr
