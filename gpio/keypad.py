from .setpinmixin import setPinMixin

class Keypad(setPinMixin):
    """docstring for Keypad"""
    def __init__(self, pins, pinsarerows=True, pinsarehigh=True):
        self.pinsarehigh = pinsarehigh
        self.pinsarerows = pinsarerows
        self.pins = []
        for row in pins:
            self.pins.append(map(self.setpin, row))
