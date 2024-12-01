import pygame
import pygame.camera
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
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        cloudOne = Cloud(50, 50)
        cloudTwo = Cloud(325, 25)
        pipeOne = Pipes()
        pipeTwo = Pipes()
        bird = Player(SCREEN_WIDTH / 5, SCREEN_HEIGHT / 2 )
       
        
        while(True):
            #1. Handle events
            screen.fill((0, 255, 255))
            
            cloudOne.draw(screen)
            cloudTwo.draw(screen)
            
            pipeOne.drawPipes(screen)
            pipeOne.updatePosition()
            
            pipeTwo.drawPipes(screen)
            pipeTwo.updatePosition()
            
            bird.display(screen)
            
            bird.moveDown()
            
            if 200 < pipeOne.xpos < 201:
                pipeTwo = Pipes()
            
            if pipeOne.xpos < -50:
                pipeOne = Pipes()
               
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.move()
            
                
                    

            #2. detect collisions and update models
            

            #3. Redraw next frame

            #4. Display next frame
    
    def endloop(self):
        pass