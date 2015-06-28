from ..setpinmixin import setPinMixin

class HallEffect(setPinMixin):
    """docstring for HallEffect"""
    def __init__(self, pin):
        self.setpin(pin)

    def sensed(self):
        pass
