import pygame
import random 
GREEN = (0, 255, 0)
LIGHTBLUE = (0, 225, 225)
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
SPEED = .05

class Pipes:
    def __init__(self):
        """
        Initiates the Pipe Class 
        """
            
        self.topPipe = random.randint(50,225)
        self.bottomPipe = random.randint(350, 450)
        self.width = 50
        self.xpos = SCREEN_WIDTH - self.width
        self.difference = 0
        self.checkRect = None
        
    def updatePosition(self):
        """
        The x-position of the pipes are updated 
        """
        self.xpos -= SPEED
            
    def drawPipes(self, screen):
        """
        Draws the pipes and randomizes the height of the pipes 
        Args:
            screen: The pygame screen where the pipes are drawn 
        """
        self.difference = self.topPipe + ( SCREEN_HEIGHT - self.bottomPipe)
        pygame.draw.rect(screen, GREEN, (self.xpos, 0, self.width, self.topPipe))
        pygame.draw.rect(screen, GREEN, (self.xpos, self.bottomPipe, self.width, SCREEN_HEIGHT - self.bottomPipe))
        
        self.checkRect = pygame.Rect(self.xpos + self.width, self.topPipe, self.width, SCREEN_HEIGHT - self.difference)
          
    def rectOne(self):
        """
        Returns a rectangle with the x-position, width and the height of the top Pipe 
        Returns:
            pygame: The rectangle of the top pipe 
        """
        return pygame.Rect((self.xpos, 0, self.width, self.topPipe))
        
    def rectTwo(self):
        """
        Returns a rectangle with the x-position, width and the height of the top Pipe 
        Returns:
            pygame: The rectangle of the bottom pipe 
        """
        return pygame.Rect((self.xpos, self.bottomPipe, self.width, SCREEN_HEIGHT - self.bottomPipe))
    
    def scorePoint(self):
        """
        Returns a rectangle with the x-position, width and the height of the pipe that checks if the user has made it throught 
        the pipe
        Returns:
            pygame.Rect: The rectangle that is used to check if the player has made it throught the pipe 
        """
        return pygame.Rect((self.xpos + self.width, self.topPipe, self.width, SCREEN_HEIGHT - self.difference))
        
        