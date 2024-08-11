from turtle import Turtle


class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(0, -280)

    def move(self):
        self.forward(10)

    def reset(self):
        self.goto(0, -280)

    def detection(self, car):
        if self.distance(car) < 30 and self.ycor() <= car.ycor():
            return True
