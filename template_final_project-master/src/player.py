import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT= 500 
GRAVITY = 0.45
UP_SPEED = 50



class Player(pygame.sprite.Sprite):
    
    def __init__(self,x,y, img="assets/bird.png"):
        """
        Initializes the Player Object 
        Args:
            image: str - path to img file
        """
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (70, 70 ))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        
    
    def display(self, screen):
         screen.blit(self.image, self.rect)
           
    def move(self):
        self.rect.y -= UP_SPEED
    
    def moveDown(self):
        self.rect.y += GRAVITY
        
        
        
    def checkContact(self):
        """
        Checks for contact of the face with the tube 
        Args: None
        Returns:
            contact: boolean - If the face makes contact with the tubes or the ground it returns True or if not it returns False
        """
        pass