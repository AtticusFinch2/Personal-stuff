import pygame
import random
from collections import defaultdict
from dataclasses import dataclass, field

# window setup
xScene = 800
yScene = 800
framerate = 60
boxW = 200
boxH = 200
borderW = 5
boxradius = 10
cols = int(xScene / boxW)
rows = int(yScene / boxH)
dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
borderColor = pygame.Color(122, 122, 110)
bgColor = pygame.Color(245, 245, 220)
@dataclass
class square48:
    pos: (int, int) = (-1,-1)
    value: int = 0
class square48New:
    def __init__(
            self,
            pos,
            value
    ):
        self.pos = pos
        self.value = value

@dataclass
class Model:
    running: bool = True
    grid_on: ... = field(default_factory=list)
    mouse_pos: ... = (-10, -10)

class ModelData:
    def __init__(
        self,
        running=True,
        screen=pygame.display.set_mode((xScene, yScene)),
        sqd = {square48New((2,2),2)}
    ):
        self.running = running
        self.x = -10
        self.y = -10
        self.screen = screen
        self.squareColor = [[pygame.color.Color(100,100,100) for x in range(rows)] for y in range(cols)]
        self.squareDict = sqd
        self.click = False
        self.lastClick = 0
        self.curTime = 0




def main():
    pygame.init()
    model = ModelData()
    clock = pygame.time.Clock()
    running = True
    global font
    font = pygame.font.Font(None, 36)
    dt = 0
    player_pos = pygame.Vector2(
        model.screen.get_width() / 2, model.screen.get_height() / 2
    )
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                model.click = True
            if event.type == pygame.MOUSEBUTTONUP:
                model.click = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                running = False
        # fill the screen with a color to wipe away anything from last frame
        model.screen.fill("purple")
        (model.x, model.y) = pygame.mouse.get_pos()
        col = int(model.x / boxW)
        row = int(model.y / boxH)
        keys = pygame.key.get_pressed()
        bgDrawer(model)
        #keyhandler(keys, model)
        # drawUI(col, row, model)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        # I don't use this, but it is useful to have if i want to make smooth movements later on
        dt = clock.tick(framerate) / 1000

    pygame.quit()




'''def keyhandler(keys, model):
    model.isSubtractMode = True if keys[pygame.K_SPACE] else False
    if keys[pygame.K_UP]:'''






def bgDrawer(
    model,
):  # changes squareColor array into a grid with each color on that square
    for col in range(cols):
        for row in range(rows):
            pygame.draw.rect(
                model.screen,
                borderColor,
                pygame.Rect((boxW * col, boxH * row), (boxW, boxH)),
                width=borderW+boxradius,
            )  # green borders, draw over with red if there is wall
            topLeftX = boxW * col + borderW
            topLeftY = boxH * row + borderW
            theCell = pygame.Rect(
                (topLeftX, topLeftY), (boxW - (2 * borderW)-1, boxH - (2 * borderW)-1),
            )
            pygame.draw.rect(model.screen, bgColor, theCell, 0, 0, boxradius,boxradius,boxradius,boxradius)





def drawUI(col, row, model):
    topLeft = (0, int(4 * model.screen.get_height() / 5))
    theCell = pygame.Rect(
        topLeft, (model.screen.get_width(), int(model.screen.get_height() / 5))
    )
    pygame.draw.rect(model.screen, pygame.Color(0, 0, 0), theCell)
    text = (
        font.render(f"({col},{row})", False, pygame.Color(255, 0, 0))
    )
    textPos = pygame.Rect(
        (
            topLeft[0] + int(model.screen.get_width() / 2 - 50),
            topLeft[1] + int(model.screen.get_height() / 10),
        ),
        (model.screen.get_width(), int(model.screen.get_height() / 3)),
    )
    model.screen.blit(text, textPos)


main()
