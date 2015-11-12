==============
 General GPIO
==============

Wrap around several (in the future anyway) low-level GPIO python modules to make
development and porting easier.

Current backend targets, in decreasing importance, are:
* RPi.GPIO (Raspberry Pi, https://pypi.python.org/pypi/RPi.GPIO)
* SUNXI_GPIO (Cubiboard A10, https://github.com/ruisebastiao/pySUNXI)
* Linux's sysfs (all supported platforms (?))

The provided Application class is only meant as a demonstration of how to implement ``ggpio`` into a multithreaded application.


.. image:: https://d2weczhvl823v0.cloudfront.net/yggdr/ggpio/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

