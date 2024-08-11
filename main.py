from turtle import Screen
from tim import Tim
from level import Level
from car import Car
from random import randint
import  time

# list of color
list_color = ["yellow", "green", "blue", "red", "black"]
screen = Screen()
screen.title("Turtle Crossing")
screen.setup(height=600, width=800)
screen.tracer(0)
# initialize the turtle at the bottom of the screen
t = Tim()
# while loop to make things move
lis_cars = []
index_y = [-225, -150, 0, 150, 225]
# listen to the screen for input from the keyboard
screen.listen()
screen.onkey(t.move, "Up")
is_on = True
r = 0.1
velocity = 0
while is_on:
    time.sleep(r)
    difficulty = Level()
    number_car_generated = randint(0, 4)
    for car in range(number_car_generated):
        index_x = randint(410, 430)
        c = Car(list_color[number_car_generated], index_x+5, index_y[number_car_generated])
        lis_cars.append(c)
    screen.update()

    for mvt in range(0, len(lis_cars)):
        lis_cars[mvt].move_car(velocity)
        if lis_cars[mvt].ycor() < -400:
            lis_cars.remove(lis_cars[mvt])
    screen.update()
    for det in range(0, len(lis_cars)):
        if t.detection(lis_cars[det]):
            is_on = False
            velocity = difficulty.game_over()

    if t.ycor() > 280:
        difficulty.increase_level()
        t.reset()
        lis_cars = []


    screen.update()

screen.exitonclick()
