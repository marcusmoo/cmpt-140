# CMPT 140 Homework Assignment #5
# 2024-10-18
# starting template
#
# write a function to draw a 
from graphics import *
import time
import os # this package help you change working directory

# please change the following to point to your directory
os.chdir("C:\\Users\\Marcus.Menic\\Desktop\\Assignment 5")

# draw the body and arm of the animated man
# 
# input: win the 
def drawManBodyArm(win):
   h = win.getHeight()
   w = win.getWidth()
   head = Circle(Point(w//2,h//4-h//8),h//8) #?????
   head.draw(win)

   center = Point(w//2,h//2+h//8)

   body = Line(Point(w//2,h//4),center)
   body.draw(win)
   
   arm = Line(Point(w//2-w//4,h//4+h//10),Point(w//2+w//4,h//4+h//10))
   arm.draw(win)

   return(h,w,center)


#************************************
# draw a man in run position 1
#
# input: win GraphWin object i.e. the window (canvas) to draw to
# 
def drawMan1(win):
   h,w,center = drawManBodyArm(win)

   left_leg = Line(center, Point(w//4, h - h//4))
   right_leg = Line(center, Point(w - w//4, h - h//4))
   left_leg.draw(win)
   right_leg.draw(win)
# 

def drawMan2(win):
   h,w,center = drawManBodyArm(win)
   
   left_leg = Line(center, Point(w//2 - 20, h - 30))
   right_leg = Line(center, Point(w//2 + 20, h - 30))
   left_leg.draw(win)
   right_leg.draw(win)

def drawMan3(win):
   h, w, center = drawManBodyArm(win)

   left_leg = Line(center, Point(w//2, h - 30))
   right_leg = Line(center, Point(w//2, h - 30))
   left_leg.draw(win)
   right_leg.draw(win)

speed = 0.025
running = True



if __name__=="__main__":
   # create the canvas for drawing
   win = GraphWin("My Rectangle x2", 200, 200)

   while running:
      drawMan1(win)
      time.sleep(speed)
      win.delete("all")
      drawMan2(win)
      time.sleep(speed)
      win.delete("all")
      drawMan3(win)
      time.sleep(speed)
      win.delete("all")
      drawMan2(win)
      time.sleep(speed)
      win.delete("all")
