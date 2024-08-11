import turtle
from turtle import Screen, Turtle
from car import Car

turtle.colormode(255)

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(height=600, width=800)
screen.tracer(0)
is_on = True
list_turtle = []
while is_on:
    c = Car()
    screen.tracer(1)
    c.move_car(0.5)

screen.update()

screen.exitonclick()
