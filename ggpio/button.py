from .basic import BasicBinaryInput


class Button(BasicBinaryInput):
    """Just a wrapper for a nicer interface"""

    @property
    def pressed(self):
        return self.sensed()

    def add_callback(self, callback, when='pressed'):
        type_ = {'pressed': 'falling' if self.pinishigh else 'rising',
                 'released': 'rising' if self.pinishigh else 'falling',
                 'both': 'both'}
        if when not in type_:
            raise ValueError("'when' must be 'pressed', 'released', or 'both'")
        super(Button, self).add_callback(callback,type_[when])

    def call_when_pressed(self, callback):
        self.add_callback(callback)

    def call_when_unpressed(self, callback):
        self.add_callback(callback, False)
