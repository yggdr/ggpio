from .setpinmixin import setPinMixin


class LED(setPinMixin):

    def __init__(self, pin, colours, pinishigh=True):
        self.colours = colours
        self.pinishigh = pinishigh
        self.pin = self.setpin(pin)

    def off(self):
        if self.pinishigh:
            self.pin.low()
        else:
            self.pin.high()

    def on(self):
        if self.pinishigh:
            self.pin.high()
        else:
            self.pin.low()
