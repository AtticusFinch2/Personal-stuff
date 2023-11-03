import pygame
import random
from collections import defaultdict
from dataclasses import dataclass, field
import makeGrid

# window setup
xScene = 1200
yScene = 800
framerate = 60
boxW = 40
boxH = 40
borderW = 3
cols = int(xScene / boxW)
rows = int(yScene / boxH)
dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
defaultNotClickedColor = pygame.Color(100, 100, 100)
defaultClickedColor = pygame.Color(0, 100, 0)
defaultHoveringColor = pygame.Color(50, 50, 50)
defaultDiscoveredColor = pygame.Color(100, 100, 0)
defaultStartColor = pygame.Color(100, 0, 100)


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
        end=(cols-1, rows-1),
    ):
        self.running = running
        self.x = -10
        self.y = 10
        self.screen = screen
        self.stateSquare = [["Hidden" for x in range(rows)] for y in range(cols)]
        self.edges = edges
        self.squareColor = [
            [defaultNotClickedColor for x in range(rows)] for y in range(cols)
        ]
        self.isSubtractMode = False
        self.click = False
        self.lastClick = 0
        self.curTime = 0
        self.visited = set()
        self.stack = []
        self.path = []
        self.now = 0
        self.tree = {node: set() for node in edges}
        self.timeIn = {}
        self.timeOut = {}
        self.end = end
        self.stateSquare[end[0]][end[1]] = "End"


def main():
    pygame.init()
    inpGraph = makeGrid.makeMaze(cols, rows, (0, 0))
    edges = defaultdict(set, inpGraph)
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
        # drawUI(col, row, model)
        if model.stack or model.path:
            tickhandler(model)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        # I don't use this, but it is useful to have if i want to make smooth movements later on
        dt = clock.tick(framerate) / 1000

    pygame.quit()


def mousehandler(model):
    col = int(model.x / boxW)
    row = int(model.y / boxH)
    model.curTime += 1
    if model.click and model.curTime > model.lastClick + 10:
        print(col, row, (model.x, model.y))  # debug
        if model.stateSquare[col][row] == "Unhidden":  # clicked on unhidden
            model.stateSquare[col][row] = "Hidden"
            model.squareColor[col][row] = defaultNotClickedColor
        else:
            model.stateSquare[col][row] = "Start"  # clicked on hidden
            model.squareColor[col][row] = defaultStartColor
            model.stack.append((col, row))
        boxDrawer(model)
        model.lastClick = model.curTime
    else:
        if model.stateSquare[col][row] in {"Unhidden", "Start", "End"}:  # hovered over unhidden
            temp = model.squareColor[col][row]
            model.squareColor[col][row] = defaultHoveringColor
            boxDrawer(model)
            model.squareColor[col][row] = temp
        else:  # hovered over hidden
            model.squareColor[col][row] = defaultHoveringColor
            boxDrawer(model)
            model.squareColor[col][row] = defaultNotClickedColor
            model.stateSquare[col][row] = "Hidden"


def keyhandler(keys, model):
    model.isSubtractMode = True if keys[pygame.K_SPACE] else False
    if keys[pygame.K_r]:
        model.edges = defaultdict(set, makeGrid.makeMaze(cols, rows, (0, 0)))
        model.stateSquare = [["Hidden" for x in range(rows)] for y in range(cols)]
        model.squareColor = [
            [defaultNotClickedColor for x in range(rows)] for y in range(cols)
        ]
        model.visited = set()
        model.stack = []
        model.path = []
        model.now = 0
        model.tree = {node: set() for node in model.edges}
        model.timeIn = {}
        model.timeOut = {}
        model.stateSquare[model.end[0]][model.end[1]] = "End"


def tickhandler(model):
    if model.stack:
        current = model.stack.pop()
        model.now += 1
        model.timeIn[current] = model.now
        model.visited.add(current)
        if model.stateSquare[current[0]][current[1]] not in {"Start", "End"}:
            model.stateSquare[current[0]][current[1]] = "Unhidden"
            model.squareColor[current[0]][current[1]] = defaultDiscoveredColor
        elif (current[0], current[1]) == model.end:
            model.squareColor[current[0]][current[1]] = pygame.Color(255,0,0)
            print("END DISCOVERED")
    else:  # when stack empty and parent not, this is the TimeOut run
        current = model.path.pop()
    weProcess = True
    temp = -1
    for edge in model.edges[current]:
        if edge not in model.visited:
            weProcess = False
            temp = edge
            model.tree[temp].add(current)
            model.tree[current].add(temp)
            break
    if weProcess:  # when we process current
        model.now += 1
        model.timeOut[current] = model.now
        if (current[0], current[1]) != model.end:
            model.squareColor[current[0]][current[1]] = defaultClickedColor
    else:
        model.stack.append(temp)
        model.path.append(current)


def boxDrawer(
    model,
):  # changes squareColor array into a grid with each color on that square
    for col in range(cols):
        for row in range(rows):
            pygame.draw.rect(
                model.screen,
                model.squareColor[col][
                    row
                ],  # we do this so that we can change color to form standard grid later
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
            if model.stateSquare[col][row] == "Unhidden":
                drawWallForSquare(col, row, model)


def drawWallForSquare(col, row, model):
    for i in range(4):
        if (col + dirs[i][0], row + dirs[i][1]) not in model.edges[
            (col, row)
        ]:
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
                        (boxW * (col + 1)),
                        (boxH * (row + 1)),  # bottom right
                    )
                    endPos = (
                        startPos[0] - boxW,
                        startPos[1] + 0,
                    )
                case 3:
                    startPos = (
                        (boxW * (col + 1)),
                        (boxH * (row + 1)),  # bottom right
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
