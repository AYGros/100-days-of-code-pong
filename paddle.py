from turtle import Turtle


STEP = 80


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.setpos(position)


    def up(self):
        new_y = self.ycor() + STEP
        self.sety(new_y)

    def down(self):
        self.sety(self.ycor() - STEP)
