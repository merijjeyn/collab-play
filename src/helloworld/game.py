import sys, pygame
from pathlib import Path
from .network import Network
from .constants import *

MAX_PLAYER_SPEED = 2

class Game:
    def __init__(self, width, height, backgroundColor, gameName):
        self.width = width
        self.height = height
        self.size = width, height
        self.backgroundColor = backgroundColor
        self.gameName = gameName

        self.network = Network(gameName)
        self.network.start_host_connection(self.player_action)

        self.leftTeamActions = {}
        self.rightTeamActions = {}
        self.leftTeam = set()
        self.rightTeam = set()

    def player_action(self, player, type, key=None):
        if type == 'join_game':
            if len(self.leftTeam) <= len(self.rightTeam):
                self.leftTeam.add(player)
            else:
                self.rightTeam.add(player)
        else:
            if player in self.leftTeam:
                actions = self.leftTeamActions
            elif player in self.rightTeam:
                actions = self.rightTeamActions

            if type == KEYDOWN:
                actions[player] = key
            elif type == KEYUP and player in actions:
                del actions[player]

    def calc_collab_actions(self, team, actions):
        if len(team) == 0:
            return [0, 0]

        speed = 0
        speedIncreasePerPlayer = MAX_PLAYER_SPEED / len(team)
        for action in actions.values():
            if action == DIRUP:
                speed += speedIncreasePerPlayer
            elif action == DIRDOWN:
                speed -= speedIncreasePerPlayer
            else:
                raise Exception("Unidentified action")

        return [0, speed]


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

        font = pygame.font.SysFont('Arial', 16)
        pausedText = font.render('Paused', True, (0,0,0))
        pausedRect = pausedText.get_rect()

        # Set initial conditions
        ballRect.update(self.width/2, self.height/2, ballRect.width, ballRect.height)
        leftPlayerRect.update(10, self.height/2 - leftPlayerRect.height/2, leftPlayerRect.width, leftPlayerRect.height)
        rightPlayerRect.update(self.width - rightPlayerRect.width - 10, self.height/2 - rightPlayerRect.height/2, rightPlayerRect.width, rightPlayerRect.height)
        pausedRect.update(self.width/2 - pausedRect.width/2, self.height/2 - pausedRect.height/2, pausedRect.width, pausedRect.height)

        ballSpeed = [1, 1]

        isPaused = True
        exited = False
        while not exited:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: exited = True

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                    isPaused = not isPaused

            screen.fill(self.backgroundColor)

            # Render names
            playerFont = pygame.font.SysFont('Verdana', 12)
            for i, player in enumerate(self.leftTeam):
                playerText = playerFont.render(player, True, (0,255,0))
                playerRect = playerText.get_rect()
                playerRect.update(self.width/2 - playerRect.width, i*(playerRect.height + 5), playerRect.width, playerRect.height)
                screen.blit(playerText, playerRect)

            for i, player in enumerate(self.rightTeam):
                playerText = playerFont.render(player, True, (255,165,0))
                playerRect = playerText.get_rect()
                playerRect.update(self.width/2, i*(playerRect.height + 5), playerRect.width, playerRect.height)
                screen.blit(playerText, playerRect)

            
            if not isPaused:
                leftSpeed = self.calc_collab_actions(self.leftTeam, self.leftTeamActions)
                rightSpeed = self.calc_collab_actions(self.rightTeam, self.rightTeamActions)

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
            else:
                screen.blit(pausedText, pausedRect)

            screen.blits([(ball, ballRect), (leftPlayer, leftPlayerRect), (rightPlayer, rightPlayerRect)])
            pygame.display.flip()
