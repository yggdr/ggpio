from collections import namedtuple


class Keypad(object):
    """docstring for Keypad"""

    presets = {
        '1x2': (
            ('1', '2'),
        ),
        '1x3': (
            ('1', '2', '3'),
        ),
        '1x4': (
            ('1', '2', '3', '4'),
        ),
        '1x5': (
            ('1', '2', '3', '4', '5'),
        ),
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
    }

    def __init__(self, rowpins, colpins, layout, scanning=True, rowsareinput=True,
                 outishigh=True):
        self.rowsareinput = rowsareinput
        inputpins = rowpins if self.rowsareinput else colpins
        outputpins = colpins if self.rowsareinput else rowpins
        self.pins = namedtuple('Pins', ['rows', 'cols', 'input', 'output'])(
            rows=rowpins, cols=colpins, input=inputpins, output=outputpins)
        self.layout = self.presets[layout] if layout in self.presets else layout
        self.scanning = scanning
        self.outishigh = outishigh

        if len(self.layout) != len(self.pin.rows):
            raise ValueError("Layout doesn't fit")
        for row in self.layout:
            if len(row) != len(self.pin.cols):
                raise ValueError("Layout doesn't fit")

        for pin in self.pins.output:
            if self.outishigh:
                pin.high()
            else:
                pin.low()

    def scan(self):
        retval = None
        while True:
            for opin in self.pins.output:
                opin.toggle()
                for ipin in self.pins.input:
                    if not ipin.read():
                        i1 = self.pins.input.index(ipin)
                        i2 = self.pins.output.index(opin)
                        if self.rowsareinput:
                            retval = self.layout[i1, i2]
                        else:
                            retval = self.layout[i2, i1]
                        while not ipin.read():
                            pass
                opin.toggle()
                if retval is not None:
                    return retval

    def read(self, numpresses):
        readstr = ''
        for i in range(numpresses):
            readstr += self.scan()
        return readstr
