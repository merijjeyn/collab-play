import sys, pygame

from .game import Game
from .controller import Controller

class Menu:
    def __init__(self, width, height, backgroundColor, font):
        self.width = width
        self.height = height
        self.size = width, height
        self.backgroundColor = backgroundColor
        self.font = font
    
    def main_menu(self):
        screen = pygame.display.set_mode(self.size)

        createGameText = self.font.render("Create Game", True, (0,0,0))
        createRect = createGameText.get_rect()

        joinGameText = self.font.render("Join Game", True, (0,0,0))
        joinRect = joinGameText.get_rect()
        
        # Set positions
        createRect.update(self.width/2 - createRect.width/2, self.height/2 - createRect.height, createRect.width, createRect.height)
        joinRect.update(self.width/2 - joinRect.width/2, self.height/2 + joinRect.height, joinRect.width, joinRect.height)

        
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): sys.exit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    if createRect.collidepoint(mousePos):
                        # Create game
                        game = Game(self.width, self.height, self.backgroundColor)
                        game.main_loop()
                    elif joinRect.collidepoint(mousePos):
                        # Join game
                        controller = Controller(self.width, self.height, self.backgroundColor)
                        controller.main_loop()


            screen.fill(self.backgroundColor)

            pygame.draw.rect(screen, (255,0,0), createRect)  
            pygame.draw.rect(screen, (255,0,0), joinRect)  

            screen.blits([(createGameText, createRect), (joinGameText, joinRect)])
            pygame.display.flip()

            




