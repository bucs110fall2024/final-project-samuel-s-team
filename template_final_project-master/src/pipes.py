import pygame
import random 
GREEN = (3, 252, 11)
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
SPEED = .05

class Pipes:
    def __init__(self):
        """
        Initializes the Pipe object
        args:
        - topPipe : int - random integers
        - bottomPipe : int - random integer for the bottom pipe
        - width : int - width of the pipe 
        - xpos : int - x position of the pipe 
        """
        
        self.topPipe = random.randint(0, 250)
        self.bottomPipe = random.randint(self.topPipe + 150, 500)
        self.width = 50
        self.xpos = SCREEN_WIDTH - self.width
    
    def updatePosition(self):
        """ 
        Returns the newly formed xposition of the tubes 
        args: None
        return: xpos
        """
        self.xpos -= SPEED
        
        
    def drawPipes(self, screen):
        pygame.draw.rect(screen, GREEN, (self.xpos, 0, self.width, self.topPipe))
        pygame.draw.rect(screen, GREEN, (self.xpos, self.bottomPipe, self.width, SCREEN_HEIGHT - self.bottomPipe))
        
    
    def newtopHeight(self):
        """
        Returns the newformed top tube position
        args: None 
        return: topHeight 
        """
        pass
          
    def bottomHeight(self):
        """
        Initializes the ship object
        args: None
        return: bottomHeight 
        """
        pass