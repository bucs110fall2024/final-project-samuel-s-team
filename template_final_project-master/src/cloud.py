import pygame
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

class Cloud(pygame.sprite.Sprite):
    
    def __init__(self,x,y, img="assets/cloud.png"):
        """
        Initializes the Cloud Class
        Args:
            x (int): x-position of the cloud 
            y (_type_): y-position of the cloud 
            img ("assets/cloud.png") - Cloud iamge 
        """
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self, screen):
        """
        Draws the clouds onto the screen
        Args:
            screen : The pygame screen is sent to this method for the clouds to be put on it 
        """
        screen.blit(self.image, self.rect)
        