from turtle import Turtle
from bricks import Bricks

class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(310, 310)
        self.num = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.num}", align='center', font=('Arial', 15, 'bold'))

    def write_my_score(self, current_turtle):
        
        # calculate the score based on the ycor of the bricks
        if current_turtle.ycor() == 285:
            self.num += 4
        if current_turtle.ycor() == 250:
            self.num += 3
        if current_turtle.ycor() == 214:
            self.num += 2
        if current_turtle.ycor() == 180:
            self.num += 1
        
        self.write_score()
