import pygame, sys
from pathlib import Path

class Controller:
    def __init__(self, width, height, backgroundColor):
        self.width = width
        self.height = height
        self.size = width, height
        self.backgroundColor = backgroundColor

    def main_loop(self):
        screen = pygame.display.set_mode(self.size)

        resourcesFolder = Path(__file__).joinpath("../resources").resolve()

        up = pygame.image.load(resourcesFolder.joinpath('up.png'))
        upRect = up.get_rect()

        down = pygame.image.load(resourcesFolder.joinpath('down.png'))
        downRect = down.get_rect()

        upRect.update(self.width/2 - upRect.width - 10, self.height/2 - upRect.height/2, upRect.width, upRect.height)
        downRect.update(self.width/2 + 10, self.height/2 - downRect.height/2, downRect.width, downRect.height)

        exited = False
        pressingUp = False
        pressingDown = False
        while not exited:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: exited = True

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    if upRect.collidepoint(mousePos):
                        pressingUp = True
                    elif downRect.collidepoint(mousePos):
                        pressingDown = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    mousePos = pygame.mouse.get_pos()
                    if upRect.collidepoint(mousePos):
                        pressingUp = False
                    elif downRect.collidepoint(mousePos):
                        pressingDown = False

            if pressingUp:
                print("Pressing up")
            if pressingDown:
                print("pressing down")         


            screen.fill(self.backgroundColor)
            screen.blits([(down, downRect), (up, upRect)])
            pygame.display.flip()

