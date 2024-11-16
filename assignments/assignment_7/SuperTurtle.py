#*******************************************************************************
# Class implementing turtle that can read a direction (route) file to go through 
# a maze
#
# author: Samuel Leung
# date: Nov 10, 2024
from Point import *
class SuperTurtle:

    # constructor
    def __init__(self,input_tt):
        # turtle object
        self._tt = input_tt
        # route is a list, each item in a list is a list of two items: 
        # x and y coordinate
        self._route = []
    
    # read route
    # @param route_fname - file name containing the routes
    def memorize_route(self,route_fname):
        # open file
        try:
            f = open(route_fname,"r") # the "r" indicates read only mode
        except:
            print("file ("+route_fname+") not found.")
            return
        
        # clear any previously "memorized" route
        self._route = []

        # TODO: read file, assume file is a CSV file with first row as header 
        # row followed by x, y coordinates in format: 
        # [x-coordinate], [y-coordinate]
        # Please store the x/y coordinates as objects of the Point class.

    # move the turtle based on the route and starting position
    # 
    # @param x_org: x-coordinate of the starting position 
    # @param y_org: y-coordinate of the starting position
    def go(self,x_org,y_org):
        self._tt.penup()
        self._tt.setpos(x_org,y_org)

        # TODO: call class methods to set the x/y origin
        # (i.e. set starting position)

        # TODO: move turtle according to the "memorized" route
        self._tt.pendown()
        
