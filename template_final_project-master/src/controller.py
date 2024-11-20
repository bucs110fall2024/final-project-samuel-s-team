import pygame
from face import Face
from cloud import Cloud 

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class Controls:
    def __init__(self):
        pygame.init()
        pygame.event.pump()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill((0, 255, 255))
        pygame.display.update()
            
    def startloop(self):
        pass  
    
    
    
    def mainloop(self):
    
        while(True):
      #1. Handle events
      
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

      #2. detect collisions and update models

      #3. Redraw next frame

      #4. Display next frame
    pygame.display.flip()
    
    def endloop(self):
        pass