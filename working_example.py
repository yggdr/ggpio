from time import sleep
from ggpio import Application, BasicBinaryOutput, BasicBinaryInput, backend, Button

with backend('rpigpio') as G:
    app = Application()
    led = BasicBinaryOutput(G.OutputPin(29))
    button = Button(G.InputPin(28, 'up'))

    @app.register
    def buttonedge():
        def toggle(channel):
            if button.pressed:
                led.on()
            else:
                led.off()
        button.add_callback(toggle, 'both')
    app.run()
