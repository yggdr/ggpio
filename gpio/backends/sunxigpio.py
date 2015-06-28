import SUNXI_GPIO as _GPIO

def init():
    """docstring for init"""
    _GPIO.init()

def setuppin(id, direction, pullupdown=None):
    """docstring for setuppin"""
    if direction.lower() == 'in':
        dir = _GPIO.IN
    elif direction.lower() == 'out':
        dir = _GPIO.OUT
    else:
        raise ValueError

    if pullupdown is not None:
        raise NotImplemented('pullupdown not supported yet with SUNXI_GPIO')

    _GPIO.setmode(id, dir, pullupdown)

def cleanup():
    """docstring for cleanup"""
    _GPIO.cleanup()

def high(id):
    """docstring for high"""
    _GPIO.output(id, _GPIO.HIGH)

def low(id):
    """docstring for low"""
    _GPIO.output(id, _GPIO.LOW)

def read(id):
    """docstring for read"""
    return _GPIO.input(id)
