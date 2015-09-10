from ggpio import backend, Button, LED, Keypad, Application
from ggpio.sensors import HallEffect
from time import sleep


with backend('rpigpio', 'bcm') as G:
    app = Application()
    b1 = Button(pin=G.InputPin(4))
    led1 = LED(pin=G.OutputPin(5))
    window_bath = HallEffect(pin=G.InputPin(6))
    window_main = HallEffect(pin=G.InputPin(7))
    windowlist = [window_bath, window_main]
    rowpins = (G.InputPin(11), G.InputPin(12), G.InputPin(13), G.InputPin(14))
    colpins = (G.OutputPin(15), G.OutputPin(16), G.OutputPin(17), G.OutputPin(18))
    doorpad = Keypad(rowpins=rowpins, colpins=colpins, layout='4x4')
    doorsensor = HallEffect(pin=G.InputPin(22))

    @app.register
    def windowwatcher():
        while True:
            sleep(.1)
            for window in windowlist:
                if window.sensed:
                    led1.off()
                else:
                    led1.on()

    @app.register
    def b1pressedled1lights():
        while True:
            sleep(.1)
            if b1.pressed:
                led1.off()
            else:
                led1.on()

    @app.register
    def b1alternatepressed():
        b1.call_when_pressed(led1.off)
        b1.call_when_unpressed(led1.on)

    @app.register
    def doorpadactivatewhendooropened():
        def alert():
            led1.on()
            print('Wrong doorcode')

        while True:
            sleep(.1)
            if not doorsensor.sensed():
                if '12345' != doorpad.read(5):
                    alert()

    app.run()
