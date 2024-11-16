#***********************************************************************/
# CMPT 140 (2024 Fall) Turtle driver
#
# Description:
# draw maze, start turtle and guide turtle through the maze
#
# Author: Samuel Leung, samuel.leung@twu.ca
# Date: Oct, 2024
#
# Input: maze specification (csv file) - see https://rosettacode.org/wiki/Maze_generation#Python
# Output: draws maze on screen
#*********************************************************************/
import turtle
from SuperTurtle import *
from draw_maze import *

tt = turtle.Turtle()

# please change the following two lines of codes so that they point to the
# files on your local computer
maze_fname = "C:\\Users\\samle\\OneDrive\\Documents\\twu\\cmpt140 (2024)\\hw\\hw7\\maze db\\maze_example_small.csv"
maze_solution_fname = "C:\\Users\\samle\\OneDrive\\Documents\\twu\\cmpt140 (2024)\\hw\\hw7\\maze db\\maze_example_small_solution.csv"

block_width, block_height = (20,20) # set wall / road width

x_org, y_org = 0,0 # origin/starting point i.e. lower-left corner of maze

draw_maze(tt, maze_fname, block_width, block_height, x_org, y_org,"grey")

# create SuperTurtle object
st = SuperTurtle(tt)

# memorize the maze solution route
st.memorize_route(maze_solution_fname)

# offset for positioning the turtle
# 1. skip the first row/column which is the wall
# 2. position the turtle to the middle of the road
x_offset, y_offset = block_width*1.5, block_height*1.5

# ask turtle to move according to the memorized route
st.go(x_offset,y_offset)

# pause so that you can view the maze w/ turtle
input()

