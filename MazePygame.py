import pygame
import random as rand
from collections import defaultdict
from dataclasses import dataclass, field
# pygame setup
xScene = 1000
yScene = 720
boxW = 32
boxH = 32
borderW = 1
cols = int(xScene/boxW)+1
rows = int(yScene/boxH)+1

@dataclass
class Model:
  running : bool = True
  grid_on : ... = field(default_factory=list)
  mouse_pos : ... = (-10,-10)

class ModelData():
  def __init__(self, running = True, edges = defaultdict(set),
               mouse_pos = (-10,-10)):
    self.running = running
    self.mouse_pos = mouse_pos
    self.cellValue = [[0 for x in range(rows)] for y in range(cols)]
    self.stateSquare = [["Unclicked" for x in range(rows)] for y in range(cols)]
    self.edges = defaultdict(set)
    self.squareColor = [[defaultNotClickedColor for x in range(rows)] for y in range(cols)]
    self.isSubtractMode = False
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
global BLACK
BLACK = pygame.color.Color('black')  # usually a global

defaultNotClickedColor = pygame.Color(100,100,100)
defaultClickedColor = pygame.Color(0,100,0)
defaultHoveringColor = pygame.Color(50,50,50)

def main():
    pygame.init()
    screen = pygame.display.set_mode((xScene, yScene))
    clock = pygame.time.Clock()
    running = True
    global font
    font = pygame.font.Font(None, 36)
    dt = 0
    ticker=0
    LastClick = 0
    curTime =0
    click=False
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    model = ModelData()
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
        (x,y) = pygame.mouse.get_pos()
        col = int(x / boxW)
        row = int(y / boxH)
        curTime = curTime+1
        if click and curTime>LastClick+5:
            print(col, row, (x,y)) # debug
            if model.isSubtractMode:
                model.cellValue[col][row] -= 1
            else:
                model.cellValue[col][row] +=1
            if model.stateSquare[col][row] == "Clicked":
                model.stateSquare[col][row] = "Unclicked"
                model.squareColor[col][row] = defaultNotClickedColor
            else:
                model.stateSquare[col][row] = "Clicked"
                model.squareColor[col][row] = defaultClickedColor
            boxDrawer(screen, model)
            LastClick = curTime
        else:
            if model.stateSquare[col][row] == "Clicked":
                model.squareColor[col][row] = defaultHoveringColor
                boxDrawer(screen, model)
                model.squareColor[col][row] = defaultClickedColor
                model.stateSquare[col][row] = "Clicked"
            else:
                model.squareColor[col][row] = defaultHoveringColor
                boxDrawer(screen, model)
                model.squareColor[col][row] = defaultNotClickedColor
                model.stateSquare[col][row] = "Unclicked"
        wallDrawer(screen, model)


        keys = pygame.key.get_pressed()
        keyhandler(keys, model)
        drawUI(screen, col, row, model)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        # I don't use this, but it is useful to have if i want to make smooth movements later on
        dt = clock.tick(15) / 1000

    pygame.quit()
def keyhandler(keys, model):
    model.isSubtractMode = True if keys[pygame.K_SPACE] else False
def boxDrawer(screen, model): #changes squareColor array into a grid with each color on that square
    for col in range(cols):
        for row in range(rows):
            pygame.draw.rect(screen, pygame.Color(0, 100, 0), pygame.Rect((boxW*col,boxH*row), (boxW,boxH)), width=borderW)#green borders, draw over with red if there is wall
            topLeftX = boxW*col+borderW
            topLeftY = boxH*row+borderW
            theCell = pygame.Rect((topLeftX,topLeftY), (boxW-(2*borderW),boxH-(2*borderW)))
            pygame.draw.rect(screen, model.squareColor[col][row], theCell)
            text = font.render(f"{model.cellValue[col][row]}", False, BLACK)
            textPos = theCell
            screen.blit(text, textPos)

def wallDrawer(screen, model):
    for col in range(cols):
        for row in range(rows):
            for i in range(4):
                if (col + dirs[i][0], row + dirs[i][1]) not in model.edges[(col, row)]:
                    current = (col,row)
                    dir =dirs[i]
                    if i > 1:
                        topLeft = ((boxW * (col+1))-borderW, (boxH * (row+1))-borderW)
                        endPos = (topLeft[0] + boxW * (dir[0]), topLeft[1] + boxH * (dir[1]))
                    else:
                        topLeft = (boxW*col, boxH*row)
                        endPos = (topLeft[0] + (boxW+borderW)*(dir[0]), topLeft[1] + (boxH+borderW)*(dir[1]))
                    pygame.draw.line(screen, pygame.Color(100, 0, 0), topLeft, endPos, width=borderW)

def drawUI(screen, col, row, model):
    topLeft = (0, int(4*screen.get_height()/5))
    theCell = pygame.Rect(topLeft, (screen.get_width(), int(screen.get_height()/5)))
    pygame.draw.rect(screen, pygame.Color(0, 0, 0), theCell)
    text = font.render(f"({col},{row})", False, pygame.Color(255,0,0)) if model.isSubtractMode else font.render(f"({col},{row})", False, pygame.Color(255,255,255))
    textPos = pygame.Rect((topLeft[0]+int(screen.get_width()/2-50), topLeft[1]+int(screen.get_height()/10)), (screen.get_width(), int(screen.get_height()/3)))
    screen.blit(text, textPos)
main()