import sys, pygame
from venv import create

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
                        self.create_menu()
                    elif joinRect.collidepoint(mousePos):
                        # Join game
                        self.join_menu()
                        # controller = Controller(self.width, self.height, self.backgroundColor)
                        # controller.main_loop()


            screen.fill(self.backgroundColor)

            pygame.draw.rect(screen, (255,0,0), createRect)  
            pygame.draw.rect(screen, (255,0,0), joinRect)  

            screen.blits([(createGameText, createRect), (joinGameText, joinRect)])
            pygame.display.flip()

            

    def create_menu(self):
        screen = pygame.display.set_mode(self.size)

        questionText = self.font.render('Game Name?', True, (0,0,0))
        questionRect = questionText.get_rect()

        createText = self.font.render('Create', True, (0,0,0))
        createRect = createText.get_rect()

        inputRect = pygame.Rect(200, 200, 300, 32)
        gameName = ''

        questionRect.update(self.width/2 - questionRect.width - 20, self.height/2 - questionRect.height - 20, questionRect.width, questionRect.height)
        createRect.update(self.width/2 - createRect.width/2, self.height/2 + 20, createRect.width, createRect.height)
        inputRect.update(self.width/2 + 20, self.height/2 - inputRect.height - 20, inputRect.width, inputRect.height)


        colorPassive = (150, 150, 150)
        colorActive = (200, 200, 200)
        inputActive = False

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
                    break

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if createRect.collidepoint(event.pos):
                        # Create game
                        Game(self.width, self.height, self.backgroundColor, gameName).main_loop()

                    if inputRect.collidepoint(event.pos):
                        inputActive = True
                    else:
                        inputActive = False

                elif event.type == pygame.KEYDOWN and inputActive:
                    if event.key == pygame.K_BACKSPACE:
                        gameName = gameName[:-1]
                    else:
                        gameName += event.unicode
            
            screen.fill(self.backgroundColor)

            pygame.draw.rect(screen, (255, 0, 0), createRect)
            
            if inputActive:
                pygame.draw.rect(screen, colorActive, inputRect)
            else:
                pygame.draw.rect(screen, colorPassive, inputRect)

            inputText = self.font.render(gameName, True, (0,0,0))
            screen.blits([(questionText, questionRect), (createText, createRect), (inputText, inputRect)])
            pygame.display.flip()


    def join_menu(self):
        screen = pygame.display.set_mode(self.size)

        gameQueryText = self.font.render('Game Name?', True, (0,0,0))
        gameQueryRect = gameQueryText.get_rect()

        gameInputRect = pygame.Rect(200, 200, 300, 32)
        gameName = ''

        usernameQueryText = self.font.render('Username?', True, (0,0,0))
        usernameQueryRect = usernameQueryText.get_rect()

        usernameInputRect = pygame.Rect(200, 200, 300, 32)
        username = ''

        joinText = self.font.render('Join', True, (0,0,0))
        joinRect = joinText.get_rect()

        gameQueryRect.update(self.width/2 - gameQueryRect.width - 10, 
                self.height/2 - usernameQueryRect.height/2 - gameQueryRect.height - 10, 
                gameQueryRect.width, gameQueryRect.height)
        gameInputRect.update(self.width/2 + 10, 
                self.height/2 - usernameQueryRect.height/2 - gameInputRect.height - 10, 
                gameInputRect.width, gameInputRect.height)
        usernameQueryRect.update(self.width/2 - usernameQueryRect.width - 10, 
                self.height/2 - usernameQueryRect.height/2, 
                usernameQueryRect.width, usernameQueryRect.height)
        usernameInputRect.update(self.width/2 + 10, 
                self.height/2 - usernameInputRect.height/2, 
                usernameInputRect.width, usernameInputRect.height)
        joinRect.update(self.width/2 - joinRect.width/2, 
                self.height/2 + usernameQueryRect.height/2 + 10, 
                joinRect.width, joinRect.height)


        colorPassive = (150, 150, 150)
        colorActive = (200, 200, 200)

        gameInputActive = False
        usernameInputActive = False

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
                    break

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if joinRect.collidepoint(event.pos):
                        # Join game
                        Controller(self.width, self.height, self.backgroundColor, gameName, username).main_loop()
                    
                    if gameInputRect.collidepoint(event.pos):
                        gameInputActive = True
                    else:
                        gameInputActive = False
                    
                    if usernameInputRect.collidepoint(event.pos):
                        usernameInputActive = True
                    else:
                        usernameInputActive = False
                
                elif event.type == pygame.KEYDOWN:
                    if gameInputActive:
                        if event.key == pygame.K_BACKSPACE:
                            gameName = gameName[:-1]
                        else:
                            gameName += event.unicode
                    if usernameInputActive:
                        if event.key == pygame.K_BACKSPACE:
                            username = username[:-1]
                        else:
                            username += event.unicode
                

            screen.fill(self.backgroundColor)

            pygame.draw.rect(screen, (255,0,0), joinRect)
            if gameInputActive:
                pygame.draw.rect(screen, colorActive, gameInputRect)
            else:
                pygame.draw.rect(screen, colorPassive, gameInputRect)
            
            if usernameInputActive:
                pygame.draw.rect(screen, colorActive, usernameInputRect)
            else:
                pygame.draw.rect(screen, colorPassive, usernameInputRect)

            gameInputText = self.font.render(gameName, True, (0,0,0))
            usernameInputText = self.font.render(username, True, (0,0,0))

            screen.blits([
                (gameQueryText, gameQueryRect), 
                (gameInputText, gameInputRect), 
                (usernameQueryText, usernameQueryRect), 
                (usernameInputText, usernameInputRect), 
                (joinText, joinRect)
            ])
            pygame.display.flip()

            

