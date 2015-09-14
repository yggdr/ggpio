from .basic import BasicBinaryInput


class Button(BasicBinaryInput):
    """Just a wrapper for a nicer interface"""

    @property
    def pressed(self):
        return self.sensed()

    def call_when_pressed(self, callback):
        self.add_callback(callback)

    def call_when_unpressed(self, callback):
        self.add_callback(callback, False)
