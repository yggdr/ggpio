class Button(object):

    def __init__(self, pin, pinishigh=True):
        self.pin = pin
        self.pinishigh = pinishigh

    def pressed(self):
        return self.pin.read()
