import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT= 500
GRAVITY = .0001
UP_SPEED = .001
JUMP_DURATION = 200
TERMINAL_VELOCITY = 1

class Player(pygame.sprite.Sprite):
    
    def __init__(self,x,y, img="assets/bird.png"):
        """
        Initializes the Player Object 
        Args:
            image: str - path to img file
        """
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.x = y
        self.y = x
        self.rect.x = x
        self.rect.y = y
        self.speed = 0
        self.acceleration = GRAVITY
        self.upTimer = 0
        self.up = False
        
    
    def display(self, screen):
        if self.up == True: 
            self.upTimer += 1
            
        if self.upTimer == JUMP_DURATION:
            self.upTimer = 0
            self.acceleration = GRAVITY
            self.up = False
            
        
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.image, self.rect)
        if self.speed < TERMINAL_VELOCITY:
            self.speed += self.acceleration
           
    def moveUp(self):
        self.up = True
        #self.speed = TERMINAL_VELOCITY
        self.acceleration = -UP_SPEED
    
    def moveDown(self):
        self.y += self.speed
        
    def getY(self):
        return self.y
    
    def getX(self):
        return self.x
     
    def getRect(self): 
        return pygame.Rect(self.x, self.y, 70, 70)
    