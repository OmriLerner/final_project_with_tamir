from pyfirmata import Arduino, SERVO

port = 'COM6'
board = Arduino(port)

class servo():
    def __init__(self, pin, init_angle):
       self.port = port
       self.pin = pin
       #set servo
       board.digital[self.pin].mode=SERVO
       #move to init angle
       board.digital[self.pin].write(init_angle)


    def rotate(self, angle):
        board.digital[self.pin].write(angle)

    def read_servo(self):
        return board.digital[self.pin].read()
# class motor():
#     def __init__(self, board):
#        self.board = board
#        self.motor1 = self.board.get_pin("d:6:o")
#        self.motor2 = self.board.get_pin("d:5:o")


#     def clockwise(self):
#         self.motor1.write(1)
#         self.motor2.write(0)

#     def counterclockwise(self):
#         self.motor1.write(0)
#         self.motor2.write(1)
        
