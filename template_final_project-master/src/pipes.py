import pygame
import random 
GREEN = (3, 252, 11)
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
SPEED = .05

class Pipes:
    def __init__(self):
            
        self.topPipe = random.randint(0, 250)
        self.bottomPipe = random.randint(self.topPipe + 250, 500)
        self.width = 50
        self.xpos = SCREEN_WIDTH - self.width
            
        
    def updatePosition(self):
        self.xpos -= SPEED
            
            
    def drawPipes(self, screen):
        self.rect1 =  pygame.draw.rect(screen, GREEN, (self.xpos, 0, self.width, self.topPipe))
        self.rect2 = pygame.draw.rect(screen, GREEN, (self.xpos, self.bottomPipe, self.width, SCREEN_HEIGHT - self.bottomPipe))
    
    def xPosition(self):
        return self.xpos
          
    def rectOne(self):
        return pygame.Rect((self.xpos, 0, self.width, self.topPipe))
        
    def rectTwo(self):
        return pygame.Rect((self.xpos, self.bottomPipe, self.width, SCREEN_HEIGHT - self.bottomPipe))
        
        