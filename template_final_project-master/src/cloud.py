import pygame
import random
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

class Cloud(pygame.sprite.Sprite):
    
    def __init__(self, img="assets/cloud.png"):
        """
        Initializes the Cloud object
        Args:
            xpos: int -  Initializes the x- position of the cloud 
            ypos: int - Initializes the y- position of the cloud 
        """
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH - 450, SCREEN_HEIGHT - 50)
        self.rect.y = random.randint(SCREEN_HEIGHT - 450, SCREEN_HEIGHT- 50)
    
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        