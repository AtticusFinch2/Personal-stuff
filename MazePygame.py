import pygame
import random as rand
from collections import defaultdict
# pygame setup
pygame.init()
xScene = 1280
yScene = 720
screen = pygame.display.set_mode((xScene, yScene))
clock = pygame.time.Clock()
running = True
dt = 0
boxW = 32
boxH = 32
cols = int(xScene/boxW)+1
rows = int(yScene/boxH)+1
borderW = 1
squareColor = [[pygame.Color(0,0,0) for x in range(rows)] for y in range(cols)]
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
edges = defaultdict(set)
edges[(1,1)] = {(0,1)}
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
def boxDrawer(): #changes squareColor array into a grid with each color on that square
    for col in range(cols):
        for row in range(rows):
            pygame.draw.rect(screen, pygame.Color(0, 100, 0), pygame.Rect((boxW*col,boxH*row), (boxW,boxH)), width=borderW)
            topLeftX = boxW*col+borderW
            topLeftY = boxH*row+borderW
            pygame.draw.rect(screen, squareColor[col][row], pygame.Rect((topLeftX,topLeftY), (boxW-(2*borderW),boxH-(2*borderW))))
def wallDrawer():
    for col in range(cols):
        for row in range(rows):
            for i in range(4):
                if (col + dirs[i][0], row + dirs[i][1]) not in edges[(col, row)]:
                    current = (col,row)
                    dir =dirs[i]
                    if i > 1:
                        topLeft = ((boxW * (col+1))-borderW, (boxH * (row+1))-borderW)
                        endPos = (topLeft[0] + boxW * (dir[0]), topLeft[1] + boxH * (dir[1]))
                    else:
                        topLeft = (boxW*col, boxH*row)
                        endPos = (topLeft[0] + (boxW+borderW)*(dir[0]), topLeft[1] + (boxH+borderW)*(dir[1]))
                    pygame.draw.line(screen, pygame.Color(100, 0, 0), topLeft, endPos, width=borderW)
stateSquare = [["Unclicked" for x in range(rows)] for y in range(cols)]
ticker=0
LastClick = 0
curTime =0
click=False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if event.type == pygame.MOUSEBUTTONUP:
            click = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    boxDrawer()
    wallDrawer()
    (x,y) = pygame.mouse.get_pos()
    col = int(x / boxW)
    row = int(y / boxH)
    curTime = curTime+1
    if click and curTime>LastClick+3:
        print(col, row, (x,y))
        if stateSquare[col][row] == "Clicked":
            stateSquare[col][row] = "Unclicked"
            squareColor[col][row] = pygame.Color(0, 0, 0)
        else:
            stateSquare[col][row] = "Clicked"
            squareColor[col][row] = pygame.Color(100, 100, 100)
        boxDrawer()
        LastClick = curTime
        print(LastClick)
    else:
        if stateSquare[col][row] == "Clicked":
            squareColor[col][row] = pygame.Color(50, 50, 50)
            boxDrawer()
            squareColor[col][row] = pygame.Color(100,100,100)
            stateSquare[col][row] = "Clicked"
        else:
            squareColor[col][row] = pygame.Color(50, 50, 50)
            boxDrawer()
            squareColor[col][row] = pygame.Color(0, 0, 0)
            stateSquare[col][row] = "Unclicked"
    wallDrawer()


    keys = pygame.key.get_pressed()

    '''if keys[pygame.K_w]:
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

