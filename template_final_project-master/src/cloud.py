import pygame
import random
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

class Cloud(pygame.sprite.Sprite):
    
    def __init__(self,x,y, img="assets/cloud.png"):
        """
        Initializes the Cloud object
        Args:
            xpos: int -  Initializes the x- position of the cloud 
            ypos: int - Initializes the y- position of the cloud 
        """
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        