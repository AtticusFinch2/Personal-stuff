TestCase = [[2, 2, 4, "T"], [0, 2, 0, 2], [4, 0, 2, 4], [0, 0, 0, 2]]
import copy
import random
def pushLeftRow(row1):
    row = copy.deepcopy(row1)
    ans = [0, 0, 0, 0]
    for current in range(4):
        if row[current] != 0:
            j = 1
            ans[current] = row[current]
            while j <= 3 - current and (
                row[current + j] == 0 or (row[current + j] != "T" and row[current] != "T")
            ):
                if (row[current + j] != "T" and row[current] != "T"):
                    # we collapse
                    #print(f"collapse at:{current, j}")
                    ans[current] = row[current] + row[current+j]
                    ans[current+j] = 0
                    row[current+j] = 0
                    #print(row,ans)
                    break
                j += 1
            for behind in range(current):  # collapse all spaces behind
                if ans[behind] == 0:
                    ans[behind] = ans[current]
                    ans[current] = 0
                    #print(f"backpedal at:{behind, current}, ans:{ans}, row:{row}")
                    break
        #print(row, ans)
        row[current] = ans[current]
    return ans
def pushRightRow(row1):
    row = copy.deepcopy(row1)
    row.reverse()
    ans = pushLeftRow(row)
    ans.reverse()
    return ans


def pushLeft(board):
    ans = [[0,0,0,0]for _ in range(4)]
    for i in range(4):
        ans[i] = pushLeftRow(board[i])
    return ans


def pushRight(board):
    ans = [[0,0,0,0]for _ in range(4)]
    for i in range(4):
        ans[i] = pushRightRow(board[i])
    return ans


def transposeSquare(twoDarr):
    ans = [[0, 0, 0, 0] for x in range(4)]
    for row in range(4):
        for col in range(4):
            ans[row][col] = twoDarr[col][row]
    return ans


def pushUp(board):
    tp = transposeSquare(board)
    ans = pushLeft(tp)
    ans = transposeSquare(ans)
    return ans


def pushDown(board):
    tp = transposeSquare(board)
    ans = pushRight(tp)
    ans = transposeSquare(ans)
    return ans

def isTerminal(board):
    if pushRight(board) == pushLeft(board) and pushUp(board) == pushDown(board):
        return True
    return False


generatable_tiles = [2,2,2,2,2,2,2,2,2,4]
def generateRand(board):
    zeroes = []
    for col in range(4):
        for row in range(4):
            if board[row][col] == 0:
                zeroes.append((row, col))
    numOfZeros = len(zeroes)
    if numOfZeros == 0:
        return board
    spawned = random.randrange(0, numOfZeros)
    (zx, zy) = zeroes[spawned]
    b = copy.deepcopy(board)
    b[zx][zy] = generatable_tiles[random.randrange(0, 10)]
    return b



import pygame
from dataclasses import dataclass

# window setup
xScene = 800
yScene = 800
framerate = 15
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
class Model:
    running: bool = True

class ModelData:
    def __init__(
        self,
        running=True,
        screen=pygame.display.set_mode((xScene, yScene)),
        board = [[0,0,0,0]for x in range(4)]
    ):
        self.running = running
        self.x = -10
        self.y = -10
        self.screen = screen
        self.squareColor = [[pygame.color.Color(100,100,100) for x in range(rows)] for y in range(cols)]
        self.board = board
        self.click = False




def main():
    pygame.init()
    model = ModelData()
    generateRand(model)
    clock = pygame.time.Clock()
    running = True
    global fontbig, fontsmall
    fontbig = pygame.font.Font(None, 150)
    fontsmall = pygame.font.Font(None, 100)
    dt = 0
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
                doNotUse = keyhandler(keys, model)
                print(doNotUse)
                if doNotUse == "GAME OVER":
                    running = False
        # fill the screen with a color to wipe away anything from last frame
        model.screen.fill("purple")
        (model.x, model.y) = pygame.mouse.get_pos()

        bgDrawer(model)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        # I don't use this, but it is useful to have if i want to make smooth movements later on
        dt = clock.tick(framerate) / 1000

    pygame.quit()
generatable_tiles = [1,1,1,1,1,1,1,1,1,2] + ["T" for _ in range(10)] #amount proportional to weight
def generateRand(model):
    zeroes = []
    for col in range(4):
        for row in range(4):
            if model.board[row][col] == 0:
                zeroes.append((row, col))
    numOfZeros = len(zeroes)
    if numOfZeros == 0:
        if isTerminal(model.board):
            return "GAME OVER"
        return "NO SPACES"
    spawned = random.randrange(0, numOfZeros)
    (zx, zy) = zeroes[spawned]
    print(f"before:{model.board}")
    model.board[zx][zy] = generatable_tiles[random.randrange(0, 20)]
    print(f"after:{model.board}")


def keyhandler(keys, model):
    temp = model.board
    if keys[pygame.K_UP]:
        model.board = pushUp(model.board)
    elif keys[pygame.K_DOWN]:
        model.board = pushDown(model.board)
    elif keys[pygame.K_RIGHT]:
        model.board = pushRight(model.board)
    elif keys[pygame.K_LEFT]:
        model.board = pushLeft(model.board)
    else:
        return "NO KEY"
    if temp == model.board:
        if pushUp(model.board) == pushDown(model.board) and pushRight(
                model.board) == pushLeft(model.board) and pushLeft(model.board) == pushUp(
                model.board):
            return "GAME OVER"
        return "didNothing"
    #print(model.board)
    generateRand(model)
    print(model.board)


cfv = { # color from value
    2: pygame.Color(238, 228, 218),
    4: pygame.Color(237, 224, 200),
    8: pygame.Color(242, 177, 121),
    16: pygame.Color(245, 149, 99),
    32: pygame.Color(246, 124, 95),
    64: pygame.Color(246, 94, 59),
    128: pygame.Color(237, 207, 114),
    256: pygame.Color(237, 204, 97),
    512: pygame.Color(237, 200, 80),
    1024: pygame.Color(237, 197, 63),
    2048: pygame.Color(237, 194, 46)
}




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

            if model.board[row][col] != 0:
                c = pygame.Color(0, 250, 0) if model.board[row][col] == "T" else pygame.Color(238, 228, 218)
                pygame.draw.rect(model.screen, c, theCell, 0, 0, boxradius,
                                 boxradius, boxradius, boxradius)
                text = (
                    fontsmall.render(f"{model.board[row][col]}", False, pygame.Color(0, 0, 0))
                )
                textPos = text.get_rect(
                    center = (
                        topLeftX+boxW/2,
                        topLeftY+boxH/2,
                    )
                )
                model.screen.blit(text, textPos)
            else:
                pygame.draw.rect(model.screen, bgColor, theCell, 0, 0, boxradius,boxradius,boxradius,boxradius)






main()
