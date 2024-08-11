from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-320, 250)
        self.hideturtle()
        self.score = 0
        self.t = 0
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=("Courier", 20, "normal"))
        self.score += 1
        self.t += 10
        return self.t

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 25, "normal"))
