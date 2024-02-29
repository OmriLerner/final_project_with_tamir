from pyfirmata import Arduino, SERVO


class servo():
    def __init__(self, port, pin, init_angle):
       self.port = port
       self.pin = pin
       #set servo
       self.board = Arduino(port)
       self.board.digital[pin].mode=SERVO
       #move to init angle
       self.board.digital[pin].write(init_angle)

    def rotate(self, angle):
        self.board.digital[self.pin].write(angle)