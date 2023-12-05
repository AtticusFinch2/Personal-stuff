import pygame
import random
import math
from dataclasses import dataclass, field

xScene = 1000
yScene = 500
framerate = 30
rows = 4
cols = 4
startGridPos = (750, 100)
squareW = 30
blue = pygame.color.Color(0, 100, 0)
yell = pygame.color.Color(100, 100, 0)


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
    ):
        self.running = running
        self.screen = screen
        self.points = 50
        self.squares = [[0 for y in range(4)] for x in range(4)]
        self.squares[1][1] = 1
        self.squares[2][1] = 1
        self.squares[2][2] = 1
        self.squares[1][2] = 1
        self.curTime = 0
        self.lastClick = 0


def main():
    pygame.init()
    model = ModelData()
    running = True
    clock = pygame.time.Clock()
    global font
    font = pygame.font.Font(None, 36)
    click = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                click = False
        keys = pygame.key.get_pressed()
        model.screen.fill("white")
        (x, y) = pygame.mouse.get_pos()
        drawCircle(model)
        drawGrid(model)
        mh(model, x, y, click)
        model = kh(model, keys)
        drawPoints(model)
        pygame.display.flip()
        clock.tick(framerate)


def drawCircle(model):
    pygame.draw.circle(
        model.screen, pygame.color.Color(0, 0, 0), (250, 250), 100, width=3
    )


def getColorSquare(model, col, row):
    if model.squares[col][row]:
        return yell
    return blue


def drawGrid(model):
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(
                model.screen,
                getColorSquare(model, col, row),
                pygame.rect.Rect(
                    (
                        startGridPos[0] + (col * (squareW + 2)),
                        startGridPos[1] + (row * (squareW + 2)),
                    ),
                    (squareW, squareW),
                ),
            )


def mh(model, x, y, click):
    model.curTime += 1
    if click and model.curTime > model.lastClick + 5:
        model.lastClick = model.curTime
        print("click", x, y)
        (deltX, deltY) = (250-x, 250-y)
        if math.sqrt( deltX*deltX + deltY*deltY)<= 100:
            model.points += 5
            print("circle")
        elif (
            x > startGridPos[0]
            and y > startGridPos[1]
            and x < startGridPos[0] + (5 * 2) + (5 * squareW)
            and y < startGridPos[1] + (5 * squareW) + (5 * 2)
        ):
            print("grid")
            for col in range(cols):
                for row in range(rows):
                    tl = (
                        startGridPos[0] + (col * (squareW + 2)),
                        startGridPos[1] + (row * (squareW + 2)),
                    )
                    br = (tl[0] + squareW, tl[1] + squareW)
                    if x > tl[0] and x < br[0] and y > tl[1] and y < br[1]:
                        model.squares[col][row] = not model.squares[col][row]
                        model.points += 10
                        print(model.points)


def drawPoints(model):
    text = font.render(f"Score is:{model.points}", False, pygame.Color(255, 0, 0))
    textPos = pygame.Rect((450, 300), (100, 20))
    model.screen.blit(text, textPos)


def kh(model, keys):
    if keys[pygame.K_r]:
        return ModelData()
    else:
        return model


main()
