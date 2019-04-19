#Haemi Lee
#Version 2
#Fall 2018
#Holds Turtle Interpreter class

import turtle
import random
import sys

class TurtleInterpreter: 
	
	def __init__(self, dx = 800, dy = 800):
		turtle.setup(width = dx, height = dy )
		turtle.tracer(False)
  	
	def drawString(self, dstring, distance, angle):
		""" Interpret the characters in string dstring as a series
    of turtle commands. Distance specifies the distance
    to travel for each forward command. Angle specifies the
    angle (in degrees) for each right or left command."""
		stack = []
		colorstack = []

		for c in dstring:
			if c == 'F':
				turtle.forward(distance)
			elif c == 'L':
				turtle.pendown()
				turtle.begin_fill()
				for i in range(2):
					turtle.forward(distance)
					turtle.left(60)
					turtle.forward(distance)f
					turtle.left(120)
				turtle.end_fill()
				turtle.penup()
			elif c == 'B':
				turtle.pendown()
				turtle.begin_fill()
				turtle.circle(distance*0.25)
				turtle.end_fill()
				turtle.penup()
			elif c == "-":
				turtle.right(angle)
			elif c == "+":
				turtle.left(angle)
			elif c == '[':
				stack.append(turtle.position())
				stack.append(turtle.heading())
			elif c == ']':
				turtle.penup()
				turtle.setheading(stack.pop())
				turtle.goto(stack.pop())
				turtle.pendown()
			elif c == '<':
				#push the current turtle color onto a color stack.
				colorstack.append( turtle.color()[0] )
			elif c == '>':
				#pop the current turtle color off the color stack and set the turtle's color to that value.
				turtle.color(colorstack.pop())
			elif c == 'g':
				#green
				turtle.color(0.15, 0.5, 0.2)
			elif c == 'y':
				#yellow
				turtle.color(0.8, 0.8, 0.3)
			elif c == 'r':
				#red
				turtle.color(0.7, 0.2, 0.3)
			elif c == 'b':
				#brown
				turtle.color(0.46, 0.18, 0.05)
			elif c == 'p':
				#pink
				turtle.color(0.85, 0.35, 0.6)
			elif c == 'v':
				#violet
				turtle.color(0.75, 0.34, 0.85)


		turtle.update()

	def hold(self):
		'''Holds the screen open until user clicks or presses 'q' key'''
		turtle.hideturtle()
		turtle.update()

		turtle.onkey(turtle.bye, 'q')

		turtle.listen()

		turtle.exitonclick()

	def place(self, xpos, ypos, angle=None):
		'''pick up the pen, place the turtle at location 
		(xpos, ypos), orient the turtle if the angle argument is 
		not None, and then put down the pen'''
		turtle.penup()
		turtle.goto(xpos, ypos)
		turtle.setheading(angle)
		turtle.pendown()

	def orient(self, angle):
		'''use the setheading function to set turtle's heading to the given angle'''
		turtle.setheading(angle)

	def goto(self, xpos, ypos):
		'''pick up the turtle, send the turtle to (xpos, ypos), and then put the pen down'''
		turtle.penup()
		turtle.goto(xpos, ypos)
		turtle.pendown()

	def color(self, c):
		'''call turtle.color() with the argument c to set the turtle's color'''
		turtle.color(c)

	def width(self, w):
		'''call turtle.width() with the argument w to set the turtle's width'''
		turtle.width(w)







