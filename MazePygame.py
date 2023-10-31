import pygame
import random as rand
from collections import defaultdict
from dataclasses import dataclass, field

# window setup
xScene = 1000
yScene = 720
boxW = 32
boxH = 32
borderW = 1
cols = int(xScene / boxW) + 1
rows = int(yScene / boxH) + 1
dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
global BLACK
BLACK = pygame.color.Color("black")  # usually a global
defaultNotClickedColor = pygame.Color(100, 100, 100)
defaultClickedColor = pygame.Color(0, 100, 0)
defaultHoveringColor = pygame.Color(50, 50, 50)


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
        edges=defaultdict(set),
    ):
        self.running = running
        self.x = -10
        self.y = 10
        self.screen = screen
        self.cellHidden = [["Hidden" for x in range(rows)] for y in range(cols)]
        self.stateSquare = [["Unclicked" for x in range(rows)] for y in range(cols)]
        self.edges = edges
        self.squareColor = [
            [defaultNotClickedColor for x in range(rows)] for y in range(cols)
        ]
        self.isSubtractMode = False
        self.click = False
        self.lastClick = 0
        self.curTime = 0


def main():
    pygame.init()
    edges = defaultdict(set)
    edges[(2, 2)] = {(1, 2), (2, 1)}
    edges[(1, 2)] = {(2, 2)}
    edges[(2, 1)] = {(2, 2)}
    model = ModelData(edges=edges)
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
        mousehandler(model)
        wallDrawer(model)

        keys = pygame.key.get_pressed()
        keyhandler(keys, model)
        drawUI(col, row, model)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        # I don't use this, but it is useful to have if i want to make smooth movements later on
        dt = clock.tick(60) / 1000

    pygame.quit()


def mousehandler(model):
    col = int(model.x / boxW)
    row = int(model.y / boxH)
    model.curTime += 1
    if model.click and model.curTime > model.lastClick + 5:
        print(col, row, (model.x, model.y))  # debug
        if model.isSubtractMode:
            model.cellHidden[col][row] = "Hidden"
        else:
            model.cellHidden[col][row] += "Unhidden"
        if model.stateSquare[col][row] == "Clicked":
            model.stateSquare[col][row] = "Unclicked"
            model.squareColor[col][row] = defaultNotClickedColor
        else:
            model.stateSquare[col][row] = "Clicked"
            model.squareColor[col][row] = defaultClickedColor
        boxDrawer(model)
        model.lastClick = model.curTime
    else:
        if model.stateSquare[col][row] == "Clicked":
            model.squareColor[col][row] = defaultHoveringColor
            boxDrawer(model)
            model.squareColor[col][row] = defaultClickedColor
            model.stateSquare[col][row] = "Clicked"
        else:
            model.squareColor[col][row] = defaultHoveringColor
            boxDrawer(model)
            model.squareColor[col][row] = defaultNotClickedColor
            model.stateSquare[col][row] = "Unclicked"


def keyhandler(keys, model):
    model.isSubtractMode = True if keys[pygame.K_SPACE] else False


def boxDrawer(
    model,
):  # changes squareColor array into a grid with each color on that square
    for col in range(cols):
        for row in range(rows):
            pygame.draw.rect(
                model.screen,
                pygame.Color(0, 100, 0),
                pygame.Rect((boxW * col, boxH * row), (boxW, boxH)),
                width=borderW,
            )  # green borders, draw over with red if there is wall
            topLeftX = boxW * col + borderW
            topLeftY = boxH * row + borderW
            theCell = pygame.Rect(
                (topLeftX, topLeftY), (boxW - (2 * borderW), boxH - (2 * borderW))
            )
            pygame.draw.rect(model.screen, model.squareColor[col][row], theCell)


# dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
def wallDrawer(model):
    for col in range(cols):
        for row in range(rows):
            if model.cellHidden[col][row] == "Unhidden":
                for i in range(4):
                    if (col + dirs[i][0], row + dirs[i][1]) not in model.edges[(col, row)]:
                        match i:
                            case 0:
                                startPos = (
                                    (boxW * col),
                                    (boxH * row),  # top left
                                )
                                endPos = (
                                    startPos[0] + boxW,
                                    startPos[1] + 0,
                                )
                            case 1:
                                startPos = (
                                    (boxW * col),
                                    (boxH * row),  # top left
                                )
                                endPos = (
                                    startPos[0] + 0,
                                    startPos[1] + boxH,
                                )
                            case 2:
                                startPos = (
                                    (boxW * (col + 1) - borderW),
                                    (boxH * (row + 1) - borderW),  # bottom right
                                )
                                endPos = (
                                    startPos[0] - boxW,
                                    startPos[1] + 0,
                                )
                            case 3:
                                startPos = (
                                    (boxW * (col + 1) - borderW),
                                    (boxH * (row + 1) - borderW),  # bottom right
                                )
                                endPos = (
                                    startPos[0] + 0,
                                    startPos[1] - boxH,
                                )

                        pygame.draw.line(
                            model.screen,
                            pygame.Color(100, 0, 0),
                            startPos,
                            endPos,
                            width=borderW,
                        )


def drawUI(col, row, model):
    topLeft = (0, int(4 * model.screen.get_height() / 5))
    theCell = pygame.Rect(
        topLeft, (model.screen.get_width(), int(model.screen.get_height() / 5))
    )
    pygame.draw.rect(model.screen, pygame.Color(0, 0, 0), theCell)
    text = (
        font.render(f"({col},{row})", False, pygame.Color(255, 0, 0))
        if model.isSubtractMode
        else font.render(f"({col},{row})", False, pygame.Color(255, 255, 255))
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
