import pygame
import abLogic
import time
import cProfile
from dataclasses import dataclass
import copy
import random
from collections import defaultdict

import numpy as np
MAX_INT = 2**30
branching = 3
initDepth = 5
edgeListActual = []
valueAtNode = defaultdict()

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
        board=[[] for d in range(initDepth)],
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
        if ticker >= 5 and model.player == 2:  # increase to slow it down, change the == statement to change who plays
            ai_handler(model)
            ticker = 0
        else:
            ticker += 1

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        # I don't use this, but it is useful to have if i want to make smooth movements later on
        dt = clock.tick(framerate) / 1000