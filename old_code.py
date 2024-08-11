from turtle import Screen, Turtle
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

box = Turtle()
all_turtles = []

def draw_boundries():
    box_boundry = 280
    box.hideturtle()
    box.color("white")
    box.penup()
    box.goto(-box_boundry,box_boundry)
    box.pendown()
    box.goto(box_boundry,box_boundry)
    box.goto(box_boundry,-box_boundry)
    box.goto(-box_boundry,-box_boundry)
    box.goto(-box_boundry,box_boundry)

def turn_right():
    all_turtles[0].setheading(0)

def turn_up():
    all_turtles[0].setheading(90)

def turn_left():
    all_turtles[0].setheading(180)

def turn_down():
    all_turtles[0].setheading(270)

def new_turtle():
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    all_turtles.append(new_turtle)

draw_boundries()

for i in range(10):
    new_turtle()
    all_turtles[i].goto((i * -20), 0)

side_of_wall = 260
play = True
while play:
    if all_turtles[0].xcor() > side_of_wall or all_turtles[0].ycor() > side_of_wall or all_turtles[0].xcor() < -side_of_wall or all_turtles[0].ycor() < -side_of_wall:
        play = False
    screen.update()
    screen.listen()
    screen.onkey(key="w", fun=turn_up)
    screen.onkey(key="s", fun=turn_down)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="d", fun=turn_right)
    time.sleep(0.1)
    for turtles in reversed(all_turtles):
        if all_turtles.index(turtles) == 0:
            turtles.forward(20)
        else:
            position = all_turtles.index(turtles) - 1
            turtles.goto(all_turtles[position].pos())

screen.exitonclick()