from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

paddle = Paddle()

screen.listen()

screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")




screen.exitonclick()