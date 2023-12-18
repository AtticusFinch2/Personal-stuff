import pygame
import c4logic
import numpy as np
import time
import cProfile
from dataclasses import dataclass

# window setup
xScene = 700
yScene = 600
framerate = 60
cols = 7
rows = 6
boxW = int(xScene / cols)
boxH = int(yScene / rows)
borderW = 5
boxradius = 10
dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
borderColor = pygame.Color(122, 122, 110)
bgColor = pygame.Color(245, 245, 220)


@dataclass
class Model:
    running: bool = True


class ModelData:
    def __init__(
        self,
        screen=pygame.display.set_mode((xScene, yScene)),
        board=np.array([[0, 0, 0, 0, 0, 0] for _ in range(7)]),
    ):
        self.x = -10
        self.y = -10
        self.screen = screen
        self.turn = 1
        self.board = board
        self.click = False
        self.hoverSq = (-1, -1)
        self.player = 1
        self.ai_on = True
        self.taken = 10


def main():
    pygame.init()
    model = ModelData()
    clock = pygame.time.Clock()
    running = True
    ticker = 0
    global fontbig, fontsmall
    fontbig = pygame.font.Font(None, 150)
    fontsmall = pygame.font.Font(None, 100)
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        (model.x, model.y) = pygame.mouse.get_pos()
        hover_handler(model)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                model.click = True
            if event.type == pygame.MOUSEBUTTONUP:
                model.click = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    running = False
                if keys[pygame.K_SPACE]:
                    movehandler(model)
        # fill the screen with a color to wipe away anything from last frame
        model.screen.fill(pygame.Color(0, 0, 250))

        drawHandler(model)
        drawWinner(model)
        # flip() the display to put your work on screen
        pygame.display.flip()
        if ticker >= 5 and model.player == 2: #increase to slow it down
            ai_handler(model)
            ticker = 0
        else:
            ticker += 1

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        # I don't use this, but it is useful to have if i want to make smooth movements later on
        dt = clock.tick(framerate) / 1000


def hover_handler(model):
    col = int(model.x / boxW)
    row = int(model.y / boxH)
    if col >= cols:
        col = cols - 1
    elif row >= rows:
        row = rows - 1
    if model.board[col][row] > 0:
        model.hoverSq = (-1, -1)
    else:
        model.hoverSq = (col, row)


def flip(player):
    if player == 1:
        return 2
    return 1


def movehandler(model):
    move = c4logic.placeMoveFast(model.board, model.hoverSq[0])
    if move[0] != -1:
        print(f"You played {move}")
        model.board[move[0]][move[1]] = model.player
        model.player = flip(model.player)


cfv = {
    0: pygame.Color(0, 0, 0),
    1: pygame.Color(250, 0, 0),
    2: pygame.Color(200, 200, 0),
    3: pygame.Color(50, 0, 0),
    4: pygame.Color(50,50,0)
}


def drawHandler(model):
    for c in range(cols):
        for r in range(rows):
            pygame.draw.circle(
                model.screen,
                cfv[model.board[c][r]],
                ((boxW * c + (boxW / 2)), (boxW * r + (boxW / 2))),
                boxW // 2.5,
            )
    move = c4logic.placeMoveFast(model.board, model.hoverSq[0])
    pygame.draw.circle(
        model.screen,
        cfv[model.player+2],
        (
            (boxW * move[0] + (boxW / 2)),
            (boxW * move[1] + (boxW / 2)),
        ),
        boxW // 2.5,
    )


cfw = {1:"Red", 2:"Yellow"}  # color from winner
def drawWinner(model):
    winner = c4logic.wins(model.board)
    if winner > 0:
        print(model.board)
        topLeft = (0, 0)
        theCell = pygame.Rect(
            topLeft, (model.screen.get_width(), model.screen.get_height())
        )
        pygame.draw.rect(model.screen, pygame.Color(0, 0, 0), theCell)
        text = fontsmall.render(
            f"{cfw[winner]} won!", False, pygame.Color(250, 250, 250)
        )
        textPos = text.get_rect(center=(xScene / 2, yScene / 2))
        model.screen.blit(text, textPos)


def ai_handler(model):
    if model.ai_on:
        with (cProfile.Profile() as pr):
            pr.enable()
            start_time = time.time()
            moves = c4logic.best_move(model.board, model.player, 5)
            model.board = moves[0][2]
            end_time = time.time()
            model.taken = end_time - start_time
            print(
                f"Ai's Move: Column moved = {moves[0][1]}, Loss: {moves[0][0]}, Time taken on this move:{model.taken}")
            pr.disable()
            pr.print_stats()
        model.player = flip(model.player)



main()
