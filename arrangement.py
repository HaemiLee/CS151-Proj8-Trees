#Haemi Lee
#Version 2
#Fall 2018
#Holds functions for arrangement of trees or flowers

import lsystem as lsys
import turtle_interpreter 


def plant( x, y, scale=1, angle=22.5, iterations=2):
	"""creates a plant Lsystem with given color, location, scale, angle and iteration"""
	
	terp = turtle_interpreter.TurtleInterpreter()


	terp.orient(300)
	terp.goto( x, y)

	dist = scale*10
	ang = angle
	its = iterations

	terp.orient(90)
	lsys1 = lsys.Lsystem()
	lsys1.setBase( "X")
	lsys1.addRule( ["X", "bF-[[X]+X]+F[+FX]-FX+<yL>-<gL><rB>"] )
	lsys1.addRule( ["F", "FF"] )

	lsys1String = lsys1.buildString( its )

	terp.drawString( lsys1String, dist, ang )
	# terp.hold()

def tree( x, y, scale=1, angle=22.5, iterations=2):
	"""creates an apple tree Lsystem with given location, scale, angle and iteration"""
	
	terp = turtle_interpreter.TurtleInterpreter()


	terp.orient(300)
	terp.goto( x, y)

	dist = scale*10
	ang = angle
	its = iterations

	terp.orient(90)
	lsys1 = lsys.Lsystem()
	lsys1.setBase( "X")
	lsys1.addRule( ["X", "bF[-[[FX]+FX<gL><rB>]-F[+FX<gL><rB>]-X<gL><rB>]+[[FX]-FX<gL><rB>]+F[-FX<gL><rB>]+X<gL><rB>"] )
	lsys1.addRule( ["F", "FF"] )

	lsys1String = lsys1.buildString( its )

	terp.drawString( lsys1String, dist, ang )
	# terp.hold()

def weed( x, y, scale=1, angle=22.5, iterations=2, heading=90):
	"""creates a weed Lsystem with given location, scale, angle and iteration"""
	
	terp = turtle_interpreter.TurtleInterpreter()


	terp.orient(heading)
	terp.goto( x, y)

	dist = scale*10
	ang = angle
	its = iterations

	terp.orient(heading)
	lsys1 = lsys.Lsystem()
	lsys1.setBase( "F")
	lsys1.addRule( ["F", "gFF-[X+Y]+[X-Y]"] )
	lsys1.addRule( ["X", "-bFY"] )
	lsys1.addRule( ["Y", "+bFX"] )

	lsys1String = lsys1.buildString( its )

	terp.drawString( lsys1String, dist, ang )
	# terp.hold()

def flower( x, y, scale=1, angle=25.7, iterations=3):
	"""creates a flower Lsystem with given location, scale, angle and iteration"""
	
	terp = turtle_interpreter.TurtleInterpreter()


	terp.orient(300)
	terp.goto( x, y)

	dist = scale*10
	ang = angle
	its = iterations

	terp.orient(90)
	lsys1 = lsys.Lsystem()
	lsys1.setBase( "X")
	lsys1.addRule( ["X", "bF[+FX<gL>]F[-FX<gL>]FX<pL>+<yL>+<pL>"] )
	lsys1.addRule( ["F", "FF"] )

	lsys1String = lsys1.buildString( its )

	terp.drawString( lsys1String, dist, ang )
	# terp.hold()


def arrangement():
	'''creates an arrangement of trees/flowers/plants'''
	terp = turtle_interpreter.TurtleInterpreter()
	tree(0,-50, .80, 22.5, 4)
	t=-325
	s=-50
	for i in range (2):
		plant( t, s, .25, 25.7, 4)
		t=t+600

	a=-350
	b=-50
	for i in range(9):
		weed(a,b, .20, 22.5, 5, 180)
		a=a+100
	x=-300
	y=-200
	for i in range (5):
		flower( x, y, .25, 25.7, 4)
		x=x+200
		y=y
	m=-350
	n=-300
	for i in range(8):
		weed(m,n, .20, 22.5, 5)
		m=m+100

	terp.hold()

def square( x, y, scale=1, angle=90, iterations=1):
	"""creates a squareLsystem with given location, scale, angle and iteration"""
	
	terp = turtle_interpreter.TurtleInterpreter()


	terp.orient(300)
	terp.goto( x, y)

	dist = scale*10
	ang = angle
	its = iterations

	terp.orient(90)
	lsys1 = lsys.Lsystem()
	lsys1.setBase( "F")
	lsys1.addRule( ["F", "gF-F-F-F"] )

	lsys1String = lsys1.buildString( its )

	terp.drawString( lsys1String, dist, ang )
	# terp.hold()

def hexagon( x, y, scale=1, angle=60, iterations=2):
	"""creates a hexagon Lsystem with given location, scale, angle and iteration"""
	
	terp = turtle_interpreter.TurtleInterpreter()


	terp.orient(300)
	terp.goto( x, y)

	dist = scale*10
	ang = angle
	its = iterations

	terp.orient(90)
	lsys1 = lsys.Lsystem()
	lsys1.setBase( "F")
	lsys1.addRule( ["F", "rF-F-F"] )

	lsys1String = lsys1.buildString( its )

	terp.drawString( lsys1String, dist, ang )
	# terp.hold()

def triangle( x, y, scale=1, angle=120, iterations=2):
	"""creates a triangle Lsystem with given location, scale, angle and iteration"""
	
	terp = turtle_interpreter.TurtleInterpreter()


	terp.orient(300)
	terp.goto( x, y)

	dist = scale*10
	ang = angle
	its = iterations

	terp.orient(90)
	lsys1 = lsys.Lsystem()
	lsys1.setBase( "F")
	lsys1.addRule( ["F", "vF-F-F"] )

	lsys1String = lsys1.buildString( its )

	terp.drawString( lsys1String, dist, ang )
	# terp.hold()
def cross( x, y, scale=1, angle=90, iterations=2):
	"""creates a cross Lsystem with given location, scale, angle and iteration"""
	
	terp = turtle_interpreter.TurtleInterpreter()


	terp.orient(300)
	terp.goto( x, y)

	dist = scale*10
	ang = angle
	its = iterations

	terp.orient(90)
	lsys1 = lsys.Lsystem()
	lsys1.setBase( "F")
	lsys1.addRule( ["F", "bF-F-F+F-F-F+F-F-F+F-F-F"] )

	lsys1String = lsys1.buildString( its )

	terp.drawString( lsys1String, dist, ang )
	# terp.hold()

def pentagonFlower( x, y, scale=1, angle=60, iterations=2):
	"""creates a pentagon flower Lsystem with given location, scale, angle and iteration"""
	
	terp = turtle_interpreter.TurtleInterpreter()


	terp.orient(300)
	terp.goto( x, y)

	dist = scale*10
	ang = angle
	its = iterations

	terp.orient(90)
	lsys1 = lsys.Lsystem()
	lsys1.setBase( "F")
	lsys1.addRule( ["F", "vF-F++F-F-F-F++F-F-F-F++F-F-F-F++F-F-F-F++F-F-F-F++F-F"] )

	lsys1String = lsys1.buildString( its )

	terp.drawString( lsys1String, dist, ang )
	# terp.hold()

def shapeFromString():
	'''places simple Lsystem shapes'''
	terp = turtle_interpreter.TurtleInterpreter()
	pentagonFlower(-100,100,1.5, 60, 1)
	cross(100,100,1.5, 90, 1)
	square(-50,0,2,90,1)
	hexagon(50,0,2,60,2)
	triangle(0,0,3,120,1)
	terp.hold()

shapeFromString()
# plant(0,-100, 1, 22.5, 4)
# tree(0,-100, 1, 22.5, 4)
# flower(0, -300, 1, 25.7, 4)
# weed(0,-100, .5, 22.5, 5)
# arrangement()



