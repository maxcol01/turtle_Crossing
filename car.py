from turtle import Turtle


class Car(Turtle):

    def __init__(self, color, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(color)
        self.goto(x, y)
        self.shapesize(stretch_wid=1, stretch_len=2)

    def move_car(self, m):
        self.backward(10 + m)
