import pygame
import pygame_menu
import pygame_menu.baseimage
import pygame_menu.locals
import pygame_menu.themes
from src.player import Player
from src.cloud import Cloud 
from src.pipes import Pipes

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class Controls:
    def __init__(self):
        pygame.init()
        pygame.event.pump()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.cloudOne = Cloud(50, 50)
        self.cloudTwo = Cloud(325, 25)
        self.pipeOne = Pipes()
        self.pipeTwo = Pipes()
        self.bird = Player(70, SCREEN_HEIGHT / 2 )
        self.score = 0
        self.font = pygame.font.Font(None, 72) 
        self.collision_occured = False
        
        self.state = "START"
        
    def startgame(self):
        self.resetgame()
        self.state = "GAME"
        
    def startloop(self):
        self.screen.fill((0, 255, 255))
        self.menu = pygame_menu.Menu("Angry Flap", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, theme = pygame_menu.themes.THEME_GREEN )
        
        self.menu.add.button(
            "Start", self.startgame, align=pygame_menu.locals.ALIGN_CENTER
        )

        while self.state == "START":
            self.menu.update(pygame.event.get())
            self.menu.draw(self.screen)
            pygame.display.flip()
            
    def resetgame(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.cloudOne = Cloud(50, 50)
        self.cloudTwo = Cloud(325, 25)
        self.pipeOne = Pipes()
        self.pipeTwo = Pipes()
        self.bird = Player(70, SCREEN_HEIGHT / 2 )
        self.score = 0
        self.font = pygame.font.Font(None, 72) 
        self.collision_occured = False
        
    
    def endgame(self):
            self.state = "OUT"
             
    def endloop(self):
        self.gameOver = "Final Score " , str(self.score)
        self.screen.fill((0, 255, 255))
       
        self.menu = pygame_menu.Menu("GAME OVER", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, theme = pygame_menu.themes.THEME_GREEN )
        self.menu.add.label(f"Final Score: {self.score} ", font_size=28)
        
        self.menu.add.button(
            "Start Over", self.startgame, align=pygame_menu.locals.ALIGN_CENTER
        )
        
        self.menu.add.button(
            "End Game", self.endgame, align = pygame_menu.locals.ALIGN_CENTER
        
        )
        while self.state == "END":
            self.menu.update(pygame.event.get())
            self.menu.draw(self.screen)
            pygame.display.flip()
        
    def gameloop(self):
         while self.state == "GAME":
            #1. Handle events
            self.screen.fill((0, 255, 255))
            
            
            self.cloudOne.draw(self.screen)
            self.cloudTwo.draw(self.screen)
            
            self.pipeOne.drawPipes(self.screen)
            self.pipeOne.updatePosition()
            
            self.pipeTwo.drawPipes(self.screen)
            self.pipeTwo.updatePosition()
            
            self.bird.display(self.screen)
            
            self.bird.moveDown()
            
            if 200 < self.pipeOne.xpos < 201:
                self.pipeTwo = Pipes()
                
            
            if self.pipeOne.xpos < -50:
                self.pipeOne = Pipes()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.moveUp()
            
            #2. detect collisions and update models
            if self.bird.getRect().colliderect(self.pipeOne.rectOne()) or self.bird.getRect().colliderect(self.pipeOne.rectTwo()):
                self.state  ="END"
               
            
            if self.bird.getRect().colliderect(self.pipeTwo.rectOne()) or self.bird.getRect().colliderect(self.pipeTwo.rectTwo()):
                self.state = "END"
            
            if self.bird.getY() >= 500 or self.bird.getY() <= -50:
                self.state = "END"
            
            if self.bird.getRect().colliderect(self.pipeOne.scorePoint()) or self.bird.getRect().colliderect(self.pipeTwo.scorePoint()):
                if self.collision_occured == False: 
                    self.score += 1
                    self.collision_occured = True
            
            if not self.bird.getRect().colliderect(self.pipeOne.scorePoint()) and not self.bird.getRect().colliderect(self.pipeTwo.scorePoint()):
                    self.collision_occured = False 
            #3. Redraw next frame
           
            number = self.font.render(str(self.score), True, (255, 255, 255))  
            text_rect = number.get_rect()
            text_rect.topleft = (10, 10) 
            self.screen.blit(number, text_rect)
            
            pygame.display.update()
            
    def mainloop(self):
        while True: 
            if self.state == "GAME":
                self.score = 0
                self.gameloop()
            elif self.state == "END":
                self.endloop()
            elif self.state == "START":
               self.startloop()
            elif self.state == "OUT":
                break
    
    