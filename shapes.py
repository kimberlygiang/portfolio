from turtle import *
import math
import random

Diddy = Turtle()

my_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

shape = input('Shape:')

setup(500,300)
x_pos = 0
y_pos = 0

Diddy.penup()
Diddy.setposition(x_pos,y_pos)

def square(): 
	Diddy.pencolor(random.choice(my_colors))
	Diddy.pendown()
	for x in range (5):
		Diddy.forward(50)
		Diddy.left(90)
	Diddy.penup()

def Square_Tessellation():
	for x in range(6):
		square()
		Diddy.penup
		Diddy.right(90)
		Diddy.forward(50)
		Diddy.left(90)
		Diddy.forward(50)

if shape == "Square_Tessellation":
	Square_Tessellation()

if shape == "square":
	square()

def triangle():
	Diddy.pencolor(random.choice(my_colors))
	Diddy.penup()
	Diddy.goto(100,0)
	Diddy.pendown()
	Diddy.forward(50)
	Diddy.left(135)
	Diddy.forward(50)
	Diddy.goto(100,0)

if shape == "triangle":
	triangle()

def hexagon():
	Diddy.pencolor(random.choice(my_colors))
	angle = 60
	Diddy.pendown()
	for x in range (7):
		Diddy.forward(50)
		Diddy.left(angle)

if shape == "hexagon":
	hexagon()

def tessellation():
	Diddy.goto(-250,-150)
	for x in range (6):
		hexagon()
		Diddy.penup()
		Diddy.forward(50)
		Diddy.left(60)
		Diddy.forward(50)
		Diddy.left(60)
		Diddy.forward(50)
		Diddy.left(180)

if shape == "tessellation":
	tessellation()

exitonclick()





