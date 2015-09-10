class Application(object):

    """Standard Application for concurrently running GPIO"""

    def __init__(self):
        """TODO: to be defined1. """
        self._registry = []

    def register(self, f):
        self._registry.append(f)
        return f

    def run(self):
        # Some form of (threaded) event loop here...
        pass
