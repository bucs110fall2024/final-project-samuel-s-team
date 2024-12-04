import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GRAVITY = 0.001
UP_SPEED = 0.01
JUMP_DURATION = 100
TERMINAL_VELOCITY = 1


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img="assets/bird.png"):
        """
        Initializes the Player Object
        Args:
            image: str - path to img file
        """
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (60, 60))
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
        """
        Updates and draws the player on the screen while handling the gravity and acceleration of the player
        Args:
            screen (_type_): _description_
        """
        if self.up:
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
        """
        Makes the player jump by reversing the gravity
        """
        self.up = True
        self.acceleration = -UP_SPEED

    def moveDown(self):
        """
        Makes the player go down by making the gravity positive
        """
        self.y += self.speed

    def getY(self):
        """
        Returns the y-position of the player
        Returns:
           self.y (int): Current y position of the player
        """
        return self.y

    def getRect(self):
        """
        Returns the rectangle that is used to check for collision
        Returns:
            pygame.Rect: Rectangle that represents the position of the player
        """
        return pygame.Rect(self.x, self.y, 60, 60)
