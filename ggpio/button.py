class Button(object):

    def __init__(self, pin, pinishigh=True):
        self.pin = pin
        self.pinishigh = pinishigh

    @property
    def pressed(self):
        return self.pin.read()

    def call_when_pressed(self, callback):
        self.pin.add_edge_callback(
            callback, 'falling' if self.pinishigh else 'rising')

    def call_when_unpressed(self, callback):
        self.pin.add_edge_callback(
            callback, 'rising' if self.pinishigh else 'falling')
