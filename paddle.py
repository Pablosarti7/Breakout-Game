from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("purple")
        self.shape('square')
        self.shapesize(stretch_len=8, stretch_wid=0.5)
        self.penup()
        self.setposition(0, -300)

    def right(self):
        self.forward(20)

    def left(self):
        self.backward(20)