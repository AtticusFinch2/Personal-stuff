import pygame
import copy
import random as rand
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
running = True
dt = 0
cols = 10
rows = 5
boxW = 100
boxH = 100
borderW = 5
squareColor = [[pygame.Color(0,0,0) for x in range(rows)] for y in range(cols)]
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
def drawer():
    for col in range(cols):
        for row in range(rows):
            pygame.draw.rect(screen, pygame.Color(0, 100, 0), pygame.Rect((boxW*col,boxH*row), (boxW,boxH)), width=borderW)
            pygame.draw.rect(screen, squareColor[col][row], pygame.Rect((boxW*col+borderW,boxH*row+borderW), (boxW-(2*borderW),boxH-(2*borderW))))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        else:
            click = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    drawer()
    (x,y) = pygame.mouse.get_pos()
    if click:
        col = int(x/boxW)
        row = int(y/boxH)
        print(col, row, (x,y))
        squareColor[col][row] = pygame.Color(int(255*rand.random()),int(255*rand.random()),int(255*rand.random()))


    '''pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt'''

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

