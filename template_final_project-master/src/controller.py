import pygame
from src.player import Player
from src.cloud import Cloud 
from src.pipes import Pipes

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GREEN = (3, 252, 11)


class Controls:
    def __init__(self):
        pygame.init()
        pygame.event.pump()
            
    def startloop(self):
        pass  
    
    def mainloop(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        cloudOne = Cloud()
        cloudTwo = Cloud()
        pipeOne = Pipes()
        pipeTwo = Pipes()
        #bird = Player()
        
        while(True):
            #1. Handle events
            self.screen.fill((0, 255, 255))
            
            cloudOne.draw(self.screen)
            cloudTwo.draw(self.screen)
            
            pipeOne.drawPipes(self.screen)
            pipeOne.updatePosition()
            
            pipeTwo.drawPipes(self.screen)
            pipeTwo.updatePosition()
            
            if 200 < pipeOne.xpos < 201:
                pipeTwo = Pipes()
            
            if pipeOne.xpos < -50:
                pipeOne = Pipes()
               
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
               # elif event.key == pygame.K_SPACE:
                 #   bird.move()
                    

            #2. detect collisions and update models

            #3. Redraw next frame

            #4. Display next frame
    
    def endloop(self):
        pass