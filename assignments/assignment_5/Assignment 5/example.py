# CMPT 140 lab #5
# 2017-11-08
# example of using graphics.py to draw some simple shapes
from graphics import *
import time # needed for the sleep function
import os

os.chdir("C:\\Users\\samle\\OneDrive\\Documents\\twu\\cmpt140 (2024)\\hw\\hw5\\demo")

# example #1
# draw a circle in the middle of the window
win = GraphWin("Example 1: circle", 500, 500)
c = Circle(Point(250,250), 50)
c.draw(win)
win.getMouse() # Pause to view result
win.close()    # Close window when done

# example 2
# draw a rectangle, located in the middle of the window
# with one edge touching the bottom of the window
# notice:
# - 0,0 is on the top left
win = GraphWin("Example 2: rectangle", 500, 500)
r = Rectangle(Point(225,500),Point(275,100))
r.draw(win)
win.getMouse() # Pause to view result
win.close()    # Close window when done

# example 3
# draw two rectangle, located in the middle of the window
# with one edge touching the bottom of the window
# the two rectangle with different heights
# notice:
# - 0,0 is on the top left
win = GraphWin("Example 3: rectangle x2", 500, 500)
r1 = Rectangle(Point(200,500),Point(250,200))
r1.draw(win)
r2 = Rectangle(Point(250,500),Point(300,150))
r2.draw(win)
win.getMouse() # Pause to view result
win.close()    # Close window when done

# example 4
# draw a horizontal line somewhere near the bottom of the window
win = GraphWin("Example 4: line", 500, 500)
l = Line(Point(5,490),Point(495,490))
l.draw(win)
win.getMouse() # Pause to view result
win.close()    # Close window when done

# example 5
# draw a circle in the middle of the window, wait for one second,
# then "move" the cirle to one side
win = GraphWin("Example 5: move circle", 500, 500)
c = Circle(Point(250,250), 50)
c.draw(win)
time.sleep(1) # wait for one second
win.delete("all") # clear the window
c = Circle(Point(250,450), 50)
c.draw(win)
win.getMouse() # Pause to view result
win.close()    # Close window when done

