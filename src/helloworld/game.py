import sys, pygame
from tkinter import RIGHT
from pathlib import Path
from .network import Network
from .constants import *

PLAYER_SPEED = 2

class Game:
    def __init__(self, width, height, backgroundColor):
        self.width = width
        self.height = height
        self.size = width, height
        self.backgroundColor = backgroundColor

        self.network = Network()
        self.leftTeamActions = {}
        self.rightTeamActions = {}

    def player_action(self, player, type, key):
        players = self.network.get_players_in_room()
        if player in players[LEFTTEAM]:
            actions = self.leftTeamActions
        elif player in players[RIGHTTEAM]:
            actions = self.rightTeamActions

        if type == KEYDOWN:
            actions[player] = key
        elif type == KEYUP:
            del actions[player]
      


    def main_loop(self):
        screen = pygame.display.set_mode(self.size)

        resourcesFolder = Path(__file__).joinpath("../resources").resolve()


        ball = pygame.image.load(resourcesFolder.joinpath('ball.png'))
        ball = pygame.transform.scale(ball, (30,30))
        ballRect = ball.get_rect()

        leftPlayer = pygame.image.load(resourcesFolder.joinpath('left_player.png'))
        leftPlayerRect = leftPlayer.get_rect()

        rightPlayer = pygame.image.load(resourcesFolder.joinpath('right_player.png'))
        rightPlayerRect = rightPlayer.get_rect()

        # Set initial conditions
        ballRect.update(self.width/2, self.height/2, ballRect.width, ballRect.height)
        leftPlayerRect.update(10, self.height/2 - leftPlayerRect.height/2, leftPlayerRect.width, leftPlayerRect.height)
        rightPlayerRect.update(self.width - rightPlayerRect.width - 10, self.height/2 - rightPlayerRect.height/2, rightPlayerRect.width, rightPlayerRect.height)


        leftSpeed = [0, 0]
        rightSpeed = [0, 0]
        ballSpeed = [3,3]


        exited = False
        while not exited:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: exited = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w: leftSpeed[1] = -1 * PLAYER_SPEED
                    elif event.key == pygame.K_s: leftSpeed[1] = PLAYER_SPEED
                    elif event.key == pygame.K_UP: rightSpeed[1] = -1 * PLAYER_SPEED
                    elif event.key == pygame.K_DOWN: rightSpeed[1] = PLAYER_SPEED

                elif event.type == pygame.KEYUP:
                    if event.key in [pygame.K_w, pygame.K_s]: leftSpeed[1] = 0
                    elif event.key in [pygame.K_UP, pygame.K_DOWN]: rightSpeed[1] = 0

            # Move players
            if leftPlayerRect.top + leftSpeed[1] > 0 and leftPlayerRect.bottom + leftSpeed[1] < self.height:
                leftPlayerRect = leftPlayerRect.move(leftSpeed)
            if rightPlayerRect.top + rightSpeed[1] > 0 and rightPlayerRect.bottom + rightSpeed[1] < self.height:
                rightPlayerRect = rightPlayerRect.move(rightSpeed)

            # Move ball
            ballRect = ballRect.move(ballSpeed)
            if ballRect.colliderect(rightPlayerRect) or ballRect.colliderect(leftPlayerRect):
                ballSpeed[0] *= -1
            if ballRect.bottom > self.height or ballRect.top < 0:
                ballSpeed[1] *= -1

            # end condition
            if ballRect.left < 0:
                print('RIGHT PLAYER WON')
                exited = True
            elif ballRect.right > self.width:
                print('LEFT PLAYER WON')
                exited = True
                
            screen.fill(self.backgroundColor)
            screen.blits([(ball, ballRect), (leftPlayer, leftPlayerRect), (rightPlayer, rightPlayerRect)])
            pygame.display.flip()
