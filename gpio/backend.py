from contextlib import contextmanager
from importlib import import_module


@contextmanager
def backend(backend, *backendargs, **backendkw):
    """TODO: Docstring for backend.

    :backend: TODO
    :returns: TODO

    """
    usedbackend = import_module('backends.' + backend)
    usedbackend.init(*backendargs, **backendkw)
    try:
        yield usedbackend
    finally:
        usedbackend.cleanup()
