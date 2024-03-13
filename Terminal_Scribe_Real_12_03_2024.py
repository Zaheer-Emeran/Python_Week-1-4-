import os
import time
from termcolor import colored

# This is the canvas class. It defines some height and width, and a
# matrix of characters to keep track of where the Terminal Scribes are moving
class Canvas:
    def __init__(self , width ,height):
        self._x = width
        self._y = height
# This is a grid that contains data about where the
# terminal scroll have visited
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    # Returns true if the given point is outside the boundaries of the Canvas
    def hits_Wall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 8 or point[1] >= self._y

    # Set the given position in the provided character in the canvas
    def setPos(self,pos,mark):
        self._canvas[pos[0]][pos[1]] = mark

    # Clear the terminal (used to create animations)
    def clear(self):
        os.system('els' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self,canvas):
        self.canvas = canvas
        self.trail = "."
        self.mark = "+"