from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from score import Score
from turtle import Turtle
import time


window = Screen()
window.bgcolor("black")
window.title("Breakout Game")
window.tracer(0)

# creating all instances
paddle = Paddle()
ball = Ball()
bricks = Bricks()
score = Score()
        
# calling the function that creates all of the brick rows
turtles = bricks.create_brick_rows([])

# keyboard commands
window.onkey(paddle.right, "Right")
window.onkey(paddle.left, "Left")
window.listen()

game_on = True
while game_on:
    time.sleep(0.1)
    window.update()
    ball.move()

    # if ball touches the paddle, bounce back
    if ball.distance(paddle) < 60 and ball.ycor() < -285:
        ball.bounce_ball()

    # if the ball hits the walls bounce
    if ball.xcor() > 340 or ball.xcor() < -340:
        angle = 180 - ball.heading()
        if angle < 0:
            angle += 360
        ball.setheading(angle)

    # if the ball hits top bounce back
    if ball.ycor() > 340:
        ball.bounce_ball()

    # if ball is out of range at the bottom reset ball to the home position
    if ball.ycor() < -340:
        ball.reset_ball()

    # detect when the ball hits a brick
    for i, tur in enumerate(turtles):
        if ball.distance(turtles[i]) < 40:
            turtles[i].hideturtle()
            turtles.remove(tur)
            score.write_my_score(tur)
            ball.bounce_ball()
    
    # write down game over
    if len(turtles) == 0:
        game_over = Turtle()
        game_over.color('white')
        game_over.hideturtle()
        game_over.penup()
        game_over.write("Game Over", align='center', font=('Arial', 40, 'bold'))
        game_on = False

window.mainloop()

