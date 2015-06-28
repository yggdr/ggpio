from gpio import backend, Button, LED
from time import sleep


with backend('rpigpio', 'bcm') as G:
    from G import InputPin, OutputPin
    b1 = Button(InputPin(3))
    led1 = LED(OutputPin(4))
    while True:
        sleep(.1)
        if b1.pressed():
            led1.off()
        else:
            led1.on()
