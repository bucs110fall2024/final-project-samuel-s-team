import pygame
class Cloud:
    def __init__(self, xpos, ypos):
        """
        Initializes the Cloud object
        Args:
            xpos: int -  Initializes the x- position of the cloud 
            ypos: int - Initializes the y- position of the cloud 
        """
        self.xpos = xpos
        self.ypos = ypos
        self.size = "small"
    
    def xposition(self):
        """
        Changes the xposition of the cloud 
        Args: None 
        Returns:
            xpos: int - The new x position of the cloud 
        """
        return self.xpos
    
    def yposiion(self):
        """
        Changes the x - position of the cloud
        Args: None 
        Returns:
            ypos: int - The new y position of the cloud 
        """
        return self.ypos