import pygame
import pygame.camera
from src.player import Player
from src.cloud import Cloud 
from src.pipes import Pipes

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

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
        bird = Player(70, SCREEN_HEIGHT / 2 )
        score = 0
        font = pygame.font.Font(None, 72) 
       
        
        collision_occured = False
        
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
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.moveUp()
            
            #2. detect collisions and update models
            if bird.getRect().colliderect(pipeOne.rectOne()) or bird.getRect().colliderect(pipeOne.rectTwo()):
                print(score)
                break
            
            if bird.getRect().colliderect(pipeTwo.rectOne()) or bird.getRect().colliderect(pipeTwo.rectTwo()):
                print(score)
                break
            
            if bird.getY() >= 500 or bird.getY() <= -50:
                print(score)
                break
            
            if bird.getRect().colliderect(pipeOne.scorePoint()) or bird.getRect().colliderect(pipeTwo.scorePoint()):
                if collision_occured == False: 
                    score += 1
                    collision_occured = True
            
            if not bird.getRect().colliderect(pipeOne.scorePoint()) and not bird.getRect().colliderect(pipeTwo.scorePoint()):
                    collision_occured = False 
            #3. Redraw next frame
           
            number = font.render(str(score), True, (255, 255, 255))  
            text_rect = number.get_rect()
            text_rect.topleft = (10, 10) 
            screen.blit(number, text_rect)
            
            pygame.display.update()
           
            
                
            
            

            #4. Display next frame
    
    def endloop(self):
        pass