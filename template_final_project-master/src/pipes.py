import pygame
import random 
GREEN = (0, 255, 0)
LIGHTBLUE = (0, 225, 225)
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
SPEED = .05

class Pipes:
    def __init__(self):
            
        self.topPipe = random.randint(25,225)
        self.bottomPipe = random.randint(350, 500)
        self.width = 50
        self.xpos = SCREEN_WIDTH - self.width
        self.difference = 0
        self.checkRect = None
        
    def updatePosition(self):
        self.xpos -= SPEED
            
    def drawPipes(self, screen):
        self.difference = self.topPipe + ( SCREEN_HEIGHT - self.bottomPipe)
        pygame.draw.rect(screen, GREEN, (self.xpos, 0, self.width, self.topPipe))
        pygame.draw.rect(screen, GREEN, (self.xpos, self.bottomPipe, self.width, SCREEN_HEIGHT - self.bottomPipe))
        
        self.checkRect = pygame.Rect(self.xpos + self.width, self.topPipe, self.width, SCREEN_HEIGHT - self.difference)
        
    def xPosition(self):
        return self.xpos
          
    def rectOne(self):
        return pygame.Rect((self.xpos, 0, self.width, self.topPipe))
        
    def rectTwo(self):
        return pygame.Rect((self.xpos, self.bottomPipe, self.width, SCREEN_HEIGHT - self.bottomPipe))
    
    def scorePoint(self):
        return pygame.Rect((self.xpos + self.width, self.topPipe, self.width, SCREEN_HEIGHT - self.difference))
        
        