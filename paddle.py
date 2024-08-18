from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.turtlesize(5, 1)
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)
