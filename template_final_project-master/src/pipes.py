import pygame
class Pipes:
    def __init__(self, xpos, ypos, topHeight, bottomHeight):
        """
        Initializes the Pipe object
        args:
        - xpos : int - starting x coordinate
        - ypox : int - starting y coordinate
        - topHeight : int - starting height of the top tube 
        - bottomHeight : int - starting height of the bottom tube 
        """
        self.xpos = xpos
        self.ypos = ypos 
        self.topPipe = topHeight 
        self.bottomPipe = bottomHeight 
        self.width = 50
    
    def newXPos(self):
        """ 
        Returns the newly formed xposition of the tubes 
        args: None
        return: xpos
        """
    def newYPos(self):
        """
        Returns the newly formed y-position of the tubes 
        args: None
        return: ypos
        """
    
    def newtopHeight(self):
        """
        Returns the newformed top tube position
        args: None 
        return: topHeight 
        """
          
    def bottomHeight(self):
        """
        Initializes the ship object
        args: None
        return: bottomHeight 
        """