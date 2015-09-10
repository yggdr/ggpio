class LED(object):

    def __init__(self, pin, colours, pinishigh=True):
        self.colours = colours
        self.pinishigh = pinishigh
        self.pin = pin

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

    def ison(self):
        """Whether LED is on
        :returns: True or False
        """
        return bool(self.pin.state) if self.pinishigh else not bool(self.pin.state)

    def toggle(self):
        """Toggle state of LED
        :returns: TODO

        """
        if self.ison():
            self.off()
        else:
            self.on()
