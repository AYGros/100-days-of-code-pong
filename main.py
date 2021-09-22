import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
#game setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

#actual game functionality
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    #detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #detect right paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #detect paddle miss and back wall hit
    if ball.xcor() > 360:
        ball.restart()

    if ball.xcor() < -360:
        ball.restart()

screen.exitonclick()