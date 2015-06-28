from .setpinmixin import setPinMixin


class Button(setPinMixin):

    def __init__(self, pin, pinishigh):
        self.pin = pin
        self.pinishigh = pinishigh

    def pressed(self):
        return self.pin.read
