import sys, pygame
from .game import Game
from .menus import Menu
from pathlib import Path
pygame.init()

PLAYER_SPEED = 2
BACKGROUND_COLOR = 255, 255, 255
SIZE = WIDTH, HEIGHT = 960, 480

    

def main():
    resourcesFolder = Path(__file__).joinpath("../resources").resolve()
    font = pygame.font.Font(resourcesFolder.joinpath('INDUBITA.ttf'), 32)

    Menu(WIDTH, HEIGHT, BACKGROUND_COLOR, font).main_menu()
    # Game(WIDTH, HEIGHT, BACKGROUND_COLOR).main_loop()

# For debug
# if __name__ == '__main__':
    # Game().main_loop()
