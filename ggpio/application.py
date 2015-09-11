import threading


class Application(object):

    """Simple Application for concurrently running GPIO"""

    def __init__(self):
        """TODO: to be defined1. """
        self.registry = []
        self.running = []

    def register(self, f):
        self._registry.append(threading.Thread(target=f, name=f.__name__))
        return f

    def run(self):
        # Some form of (threaded) event loop here...
        for job in self.registry:
            job.start()
            self.running.append(job)
