from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.set_my_heading()

    def set_my_heading(self):
        random_num = random.randint(225, 325) # move down
        self.setheading(random_num)

    def move(self):
        self.forward(12)

    def bounce_ball(self):
        angle = 360 - self.heading()
        self.setheading(angle)

    def reset_ball(self):
        self.goto(0, 0)
        random_num = random.randint(225, 325)
        self.setheading(random_num)