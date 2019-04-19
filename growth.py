#Haemi Lee
#Version 2
#Fall 2018
#Holds functions that shows growth of Lsystem by increasing iterations
import lsystem as lsys
import turtle_interpreter 


def springWreath( x, y, scale=1, angle=22.5, iterations=2):
	"""creates a wreath Lsystem with given location, scale, angle and iteration"""
	
	terp = turtle_interpreter.TurtleInterpreter()


	terp.orient(300)
	terp.goto( x, y)

	dist = scale*10
	ang = angle
	its = iterations

	terp.orient(90)
	lsys1 = lsys.Lsystem()
	lsys1.setBase( "X")
	lsys1.addRule( ["X", "<pV>-<vW>[+<gF>X][-X]<yF>X<gL><rB>"] )
	lsys1.addRule( ["F", "+FF"] )
	lsys1.addRule( ["V", "-FF"] )
	lsys1.addRule( ["W", "FF"] )


	lsys1String = lsys1.buildString( its )

	terp.drawString( lsys1String, dist, ang )
	# terp.hold()

def wreathGrowth():
	'''shows wreath growing by increasing the iterations'''
	terp = turtle_interpreter.TurtleInterpreter()
	x=-300
	y=0
	iterations = 3
	for i in range(3):
		springWreath(x, y, .5, 25.7, iterations)
		x=x+250
		iterations = iterations + 2
	terp.hold()

def block( x, y, scale=1, angle=90, iterations=2):
	"""creates a block pattern Lsystem with given location, scale, angle and iteration"""
	
	terp = turtle_interpreter.TurtleInterpreter()


	terp.orient(300)
	terp.goto( x, y)

	dist = scale*10
	ang = angle
	its = iterations

	terp.orient(90)
	lsys1 = lsys.Lsystem()
	lsys1.setBase( "X")
	lsys1.addRule( ["X", "yXFYX+F+gYFXY-F-pXFYX"] )
	lsys1.addRule( ["Y", "vYFZXY-F-XFYZX+F+YFXY"] )
	lsys1.addRule( ["Z", "X+FY+X"] )


	lsys1String = lsys1.buildString( its )

	terp.drawString( lsys1String, dist, ang )
	# terp.hold()

def blockGrowth():
	'''shows block Lsystem growing by increasing the iterations'''
	terp = turtle_interpreter.TurtleInterpreter()
	x=-300
	y=0
	iterations = 2
	for i in range(3):
		block(x, y, .40, 90, iterations)
		x=x+300
		iterations = iterations + 1
	terp.hold()

def pinkFlower( x, y, scale=1, angle=36, iterations=3):
	"""creates a pink flower Lsystem with given location, scale, angle and iteration"""
	
	terp = turtle_interpreter.TurtleInterpreter()


	terp.orient(300)
	terp.goto( x, y)

	dist = scale*10
	ang = angle
	its = iterations

	terp.orient(90)
	lsys1 = lsys.Lsystem()
	lsys1.setBase( "pF++vF++F++F++F")
	lsys1.addRule( ["F", "FYF+FYF-F++F"] )
	lsys1.addRule( ["Y", " FF"] )



	lsys1String = lsys1.buildString( its )

	terp.drawString( lsys1String, dist, ang )
	# terp.hold()

def pinkFlowerGrowth():
	'''shows pinkFLower growing by increasing the iterations'''
	terp = turtle_interpreter.TurtleInterpreter()
	x=-300
	y=0
	iterations = 2
	for i in range(3):
		pinkFlower(x, y, .80, 36, iterations)
		x=x+250
		iterations = iterations + 1
	terp.hold()



wreathGrowth()
# blockGrowth()
# pinkFlowerGrowth()
# pinkFlower(100, 0, 1, 36, 3)
# block(100, 0, 1, 90, 3)
# springWreath(100, 0, 1, 25.7, 7)