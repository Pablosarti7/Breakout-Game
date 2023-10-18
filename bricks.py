from turtle import Turtle

class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=4.6, stretch_wid=1.3)
        self.penup()
        self.goto(-300, 285)
        self.hideturtle()
        
    def first_rwo_of_bricks(self, n):
        self.showturtle()
        self.goto(-300 + n * 100, 285) # top have 285 y cor

    def second_rwo_of_bricks(self, n):
        self.showturtle()
        self.color('green')
        self.goto(-300 + n * 100, 250)

    def third_rwo_of_bricks(self, n):
        self.showturtle()
        self.color('yellow')
        self.goto(-300 + n * 100, 214)

    def fourth_rwo_of_bricks(self, n):
        self.showturtle()
        self.color('red')
        self.goto(-300 + n * 100, 180)

    def create_brick_rows(self, array:list):
        for n in range(7):
            first_brick = self.clone()
            first_brick.first_rwo_of_bricks(n)
            array.append(first_brick)

        for n in range(7):
            second_brick = self.clone()
            second_brick.second_rwo_of_bricks(n)
            array.append(second_brick)

        for n in range(7):
            third_brick = self.clone()
            third_brick.third_rwo_of_bricks(n)
            array.append(third_brick)

        for n in range(7):
            fourth_brick = self.clone()
            fourth_brick.fourth_rwo_of_bricks(n)
            array.append(fourth_brick)

        return array