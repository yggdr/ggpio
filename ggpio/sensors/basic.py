class BasicBinarySensor(object):

    """Basic sensor that just reads high or low on a pin"""

    def __init__(self, pin, pinishigh=True):
        """Set up the Sensor

        :pin: Pin object to use

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
