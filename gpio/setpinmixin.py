class setPinMixin(object):

    def pin():
        doc = "The pin property."

        def fget(self):
            return self._pin

        def fset(self, value):
            self._pin = Pin(value) if isinstance(value, int) else value

        def fdel(self):
            del self._pin
        return locals()
    pin = property(**pin())
