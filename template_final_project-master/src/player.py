import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, name):
        super().__init__()
        self.name = name 
        self.size = 'small'
        self.image = pygame.image.load(f'assets/')
        self.rect = self.image.get_rect()
        self.rect.x = 0 
        self.rect.y = 0
        self.is_jumping_up = False
        self.is_jumping_down = False
        
    def jump(self):
        if self.is_jumping_up:
            pass   