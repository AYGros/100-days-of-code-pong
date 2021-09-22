from turtle import Turtle

START_X = 350
START_Y = 0
STEP = 80


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(START_X, START_Y)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")


    def up(self):
        new_y = self.ycor() + STEP
        self.sety(new_y)

    def down(self):
        self.sety(self.ycor() - STEP)
