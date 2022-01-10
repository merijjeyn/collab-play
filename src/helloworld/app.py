import sys, pygame
from pygame.constants import K_DOWN, K_UP
pygame.init()

PLAYER_SPEED = 2
BACKGROUND_COLOR = 255, 255, 255

class Game:

    def main_loop(self):
        size = width, height = 960, 480
        screen = pygame.display.set_mode(size)

        ball = pygame.image.load("src/helloworld/resources/ball.png")
        ball = pygame.transform.scale(ball, (30,30))
        ballRect = ball.get_rect()

        leftPlayer = pygame.image.load("src/helloworld/resources/left_player.png")
        leftPlayerRect = leftPlayer.get_rect()

        rightPlayer = pygame.image.load("src/helloworld/resources/right_player.png")
        rightPlayerRect = rightPlayer.get_rect()

        # Set initial conditions
        ballRect.update(width/2, height/2, ballRect.width, ballRect.height)
        leftPlayerRect.update(10, height/2 - leftPlayerRect.height/2, leftPlayerRect.width, leftPlayerRect.height)
        rightPlayerRect.update(width - rightPlayerRect.width - 10, height/2 - rightPlayerRect.height/2, rightPlayerRect.width, rightPlayerRect.height)


        leftSpeed = [0, 0]
        rightSpeed = [0, 0]
        ballSpeed = [1,1]

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w: leftSpeed[1] = -1 * PLAYER_SPEED
                    elif event.key == pygame.K_s: leftSpeed[1] = PLAYER_SPEED
                    elif event.key == pygame.K_UP: rightSpeed[1] = -1 * PLAYER_SPEED
                    elif event.key == pygame.K_DOWN: rightSpeed[1] = PLAYER_SPEED

                elif event.type == pygame.KEYUP:
                    if event.key in [pygame.K_w, pygame.K_s]: leftSpeed[1] = 0
                    elif event.key in [pygame.K_UP, pygame.K_DOWN]: rightSpeed[1] = 0

            # Move players
            if leftPlayerRect.top + leftSpeed[1] > 0 and leftPlayerRect.bottom + leftSpeed[1] < height:
                leftPlayerRect = leftPlayerRect.move(leftSpeed)
            if rightPlayerRect.top + rightSpeed[1] > 0 and rightPlayerRect.bottom + rightSpeed[1] < height:
                rightPlayerRect = rightPlayerRect.move(rightSpeed)

            # Move ball
            ballRect = ballRect.move(ballSpeed)
            if ballRect.colliderect(rightPlayerRect) or ballRect.colliderect(leftPlayerRect):
                ballSpeed[0] *= -1
            if ballRect.bottom > height or ballRect.top < 0:
                ballSpeed[1] *= -1

            # end condition
            if ballRect.left < 0:
                print('RIGHT PLAYER WON')
                sys.exit()
            elif ballRect.right > width:
                print('LEFT PLAYER WON')
                sys.exit()
                
            screen.fill(BACKGROUND_COLOR)
            screen.blits([(ball, ballRect), (leftPlayer, leftPlayerRect), (rightPlayer, rightPlayerRect)])
            pygame.display.flip()

            

def main():
    return Game()

# For debug
if __name__ == '__main__':
    Game().main_loop()
