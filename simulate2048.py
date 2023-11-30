import Logic2048
import copy
import random
import Ai2048
import time
generatable_tiles = [2,2,2,4]
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
    board[zx][zy] = generatable_tiles[random.randrange(0, 3)]
    return board


def doSim():
    endScores = []
    for gameNum in range(10):
        board = generateRand([[0,0,0,0] for x in range(4)])
        while not Ai2048.isTerminal(board):
            moves = Ai2048.bestMoveHeuristic(board, 2)
            for move in moves:  # go through the moves and pick the first valid move
                if board != move[1]:
                    board = move[1]
                    break
            board = generateRand(board)
            #print("tick")
        endScores.append(Ai2048.biggestNum(board))
        print(endScores[gameNum])
    return endScores
var = time.time()
print(doSim())
print((time.time()-var)/1000)
