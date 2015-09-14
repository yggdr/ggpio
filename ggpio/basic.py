class BasicBinaryInput(object):
    """Basic input that just reads high or low on a pin"""

    def __init__(self, pin, pinishigh=True):
        """Set up the Sensor

        :pin: Pin object to use
        :pinishigh: True (default) means setting the Pin to high activates the
        output

        """
        self.pin = pin
        self.pinishigh = pinishigh

    def add_callback(self, callback, on_sensing=True):
        """Set up a function to call when the sensor detects

        :callback: function to call on detection
        :on_sensting: Whether the function should be called when the sensor detects
        (True), or stops detecting (False)
        :returns: TODO

        """
        self.pin.add_edge_callback(
            callback, 'rising' if self.pinishigh ^ on_sensing else 'falling')

    def sensed(self):
        """Whether the sensor detects something

        :returns: TODO

        """
        return not self.pin.read() if self.pinishigh else self.pin.read()


class BasicBinaryOutput(object):
    """Create objects that just set a Pin to high or low, like a simple LED"""

    def __init__(self, pin, pinishigh=True):
        """

        :pin: Pin object to use
        :pinishigh: True (default) means setting the Pin to high activates the
        output

        """
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

    def toggle(self):
        """Toggle state of the output object
        :returns: TODO

        """
        try:
            self.pin.toggle()
        except NotImplementedError:
            if self.ison():
                self.off()
            else:
                self.on()

    def ison(self):
        """Whether object is on
        :returns: True or False
        """
        return bool(self.pin.state) if self.pinishigh else not bool(self.pin.state)
