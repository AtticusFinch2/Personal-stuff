import pygame
from dataclasses import dataclass, field
import NonoLogic
from collections import defaultdict
import json

# window setup
xScene = 1200
yScene = 800
framerate = 60
boxW = 40
boxH = 40
borderW = 3
dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
xOffset = xScene//2
yOffset = yScene//2
hintKerning = 10

# PUT YOUR NONOGRAM W AND H HERE
nonoW = 10
nonoH = 5


class ModelData:
    def __init__(
        self,
        running=True,
        screen=pygame.display.set_mode((xScene, yScene)),
    ):
        self.running = running
        self.x = -10
        self.y = 10
        self.screen = screen
        self.click = False
        self.lastClick = 0
        self.curTime = 0
        self.hiddenBoard = [[0 for i in range(nonoW)] for i in range(nonoH)]
        self.userBoard = [[0 for i in self.hiddenBoard[0]] for j in self.hiddenBoard]
        self.leftHints = [NonoLogic.row_to_hint(row) for row in self.hiddenBoard]  # (len, type)
        self.topHints = [NonoLogic.row_to_hint(row) for row in NonoLogic.transpose(self.hiddenBoard)]  # (len, type)
        self.keyState = 1



def main():
    pygame.init()
    model = ModelData()

    running = True
    global fontsmall
    fontsmall = pygame.font.Font(None, 36)
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
            if event.type == pygame.KEYDOWN:
                keyhandler(keys, model)
        # fill the screen with a color to wipe away anything from last frame
        model.screen.fill("white")
        (model.x, model.y) = pygame.mouse.get_pos()
        drawhandler(model)
        mousehandler(model)

        pygame.display.flip()

    pygame.quit()


def keyhandler(keys, m):
    m.keyState = 0
    if keys[pygame.K_1]:
        m.keyState = 1
    if keys[pygame.K_2]:
        m.keyState = 2
    if keys[pygame.K_3]:
        m.keyState = 3
    if keys[pygame.K_p]:  # print painted board
        print(f"board:{m.userBoard}, \nlefthints: {m.leftHints} tophints {m.topHints}")
        filename = input("What do you want to save this board as: ")
        if not filename.endswith('.json'):
            filename += '.json'
        filename = "NonoPuzzles/" + filename
        with open(filename, 'w') as f:
            json.dump(m.userBoard, f)
        print(f"Data has been written to {filename}")
    if keys[pygame.K_r]:
        m.hiddenBoard = [[0 for i in range(nonoW)] for i in range(nonoH)]
        m.userBoard = [[0 for i in m.hiddenBoard[0]] for j in m.hiddenBoard]
        updateHints(m)

def mousehandler(m):
    boundingGrid = ((xOffset, yOffset), (xOffset+boxW*len(m.userBoard[0]), yOffset+boxH*len(m.userBoard)))
    insideGrid = m.x < boundingGrid[1][0] and m.y < boundingGrid[1][1] and m.x > xOffset and m.y > yOffset
    if insideGrid:
        # draw crosshairs
        col = (m.x-xOffset)//boxW
        row = (m.y-yOffset)//boxH
        pygame.draw.rect(
            m.screen,
            pygame.Color(50, 50, 255),
            pygame.Rect((0, yOffset+boxH*row), (xOffset+boxW*len(m.userBoard[0])+borderW, boxH+borderW)),
            width=borderW,
        )
        pygame.draw.rect(
            m.screen,
            pygame.Color(50, 50, 255),
            pygame.Rect((xOffset + boxW * col, 0), (boxW+borderW, yOffset + boxH * len(m.userBoard) + borderW)),
            width=borderW,
        )

        # clicking
        m.curTime += 1
        if m.click and m.curTime > m.lastClick + 10:
            m.lastClick = m.curTime
            # user has clicked
            m.userBoard[row][col] = m.keyState
            updateHints(m)


stateColor = { # color from value
    1: pygame.Color(50, 50, 50),
    3: pygame.Color(0, 100, 0),
    2: pygame.Color(0, 0, 0),
    0: pygame.Color(255, 255, 255),
}
whiteTextStates = {2}
def drawSquare(row, col, model):
    pygame.draw.rect(
        model.screen,
        stateColor[model.userBoard[row][col]],
        pygame.Rect(((boxW * col)+xOffset, (boxH * row)+yOffset), (boxW + borderW, boxH + borderW)),
        #width=borderW,
    )
    pygame.draw.rect(
        model.screen,
        pygame.Color(0, 0, 0),
        pygame.Rect(((boxW * col) + xOffset, (boxH * row) + yOffset), (boxW + borderW, boxH + borderW)),
        width=borderW,
    )

def drawHintLeft(hint, row, model):

    for i in range(len(hint)):
        rect = pygame.Rect((xOffset-hintKerning-(boxW)*(i+1)+borderW, yOffset+(boxH)*row+borderW), (boxW-borderW, boxH-borderW))
        pygame.draw.rect(
            model.screen,
            stateColor[hint[i][1]],
            rect,
            # width=borderW,
        )
        text = (
            fontsmall.render(f"{hint[i][0]}", False, pygame.Color(255,255,255) if hint[i][1] in whiteTextStates else pygame.Color(0, 0, 0))
        )
        textPos = rect
        model.screen.blit(text, textPos)


def drawHintTop(hint, col, model):

    for i in range(len(hint)):
        rect = pygame.Rect((xOffset+(boxW)*col+borderW, yOffset-hintKerning-(boxH)*(i+1)+borderW), (boxW-borderW, boxH-borderW))
        pygame.draw.rect(
            model.screen,
            stateColor[hint[i][1]],
            rect,
            # width=borderW,
        )
        text = (
            fontsmall.render(f"{hint[i][0]}", False, pygame.Color(255,255,255) if hint[i][1] in whiteTextStates else pygame.Color(0, 0, 0))
        )
        textPos = rect
        model.screen.blit(text, textPos)


def drawhandler(m):
    # draw current board
    for gridRow in range(len(m.userBoard)):
        for gridCol in range(len(m.userBoard[0])):
            drawSquare(gridRow, gridCol, m)
    # draw hints
    #    left side
    longestHint = max([len(hint) for hint in m.leftHints])
    pygame.draw.rect(
        m.screen,
        pygame.Color(0, 0, 100),
        pygame.Rect((xOffset-boxW*longestHint-hintKerning, yOffset), (boxW*longestHint + borderW, boxH*len(m.userBoard) + borderW)),
    )
    for row in range(len(m.leftHints)):
        hint = m.leftHints[row]
        drawHintLeft(hint, row, m)
    # draw hints
    #    top side
    longestHint = max([len(hint) for hint in m.topHints])
    pygame.draw.rect(
        m.screen,
        pygame.Color(0, 0, 100),
        pygame.Rect((xOffset, yOffset -hintKerning - boxW * longestHint),
                    (boxW*len(m.userBoard[0]) + borderW, boxH * longestHint + borderW)),
    )
    for row in range(len(m.topHints)):
        hint = m.topHints[row]
        drawHintTop(hint, row, m)  # '''


def updateHints(m):
    m.leftHints = [NonoLogic.row_to_hint(row) for row in m.userBoard]  # (len, type)
    m.topHints = [NonoLogic.row_to_hint(row) for row in NonoLogic.transpose(m.userBoard)]  # (len, type)


if __name__ == '__main__':
  main()