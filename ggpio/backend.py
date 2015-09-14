from contextlib import contextmanager
from importlib import import_module


@contextmanager
def backend(backend, *backendargs, **backendkw):
    """Context manager for selected backend.

    :backend: The backend to use, e.g. "rpigpio"
    :returns: Module object with the proper Pin classes

    """
    usedbackend = import_module('.backends.' + backend, 'ggpio')
    usedbackend.init(*backendargs, **backendkw)
    try:
        yield usedbackend
    finally:
        usedbackend.cleanup()
