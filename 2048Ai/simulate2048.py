import random
import Ai2048

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
    board[zx][zy] = generatable_tiles[random.randrange(0, 9)]
    return board

def doSim(n):
    endScores = []
    for gameNum in range(n):
        moveNum =0
        board = generateRand([[0,0,0,0] for x in range(4)])
        while not Ai2048.isTerminal(board):
            moves = Ai2048.bestMoveHeuristic(board, 2)
            for move in moves:  # go through the moves and pick the first valid move
                if board != move[1]:
                    board = move[1]
                    break
            board = generateRand(board)
            moveNum += 1
            #print(f"moves this game: {moveNum}, biggest num this game = {Ai2048.biggestNum(board)}")
        endScores.append(Ai2048.biggestNum(board))
        #print(endScores[gameNum])
    return endScores
def doSimFast(n):
    endScores = []
    for gameNum in range(n):
        moveNum =0
        board = generateRand([[0,0,0,0] for x in range(4)])
        while not Ai2048.isTerminal(board):
            #moves = Ai2048.bestMove(board)
            #moves = Ai2048.bestMoveDepth(board,2)
            #moves = Ai2048.bestMoveHeuristic(board, 2)
            moves = Ai2048.bestMoveHeuristicFast(board, 2)
            for move in moves:  # go through the moves and pick the first valid move
                if board != move[1]:
                    board = move[1]
                    break
            board = generateRand(board)
            moveNum += 1
            #print(f"moves this game: {moveNum}, biggest num this game = {Ai2048.biggestNum(board)}")
        endScores.append(Ai2048.biggestNum(board))
        #print(endScores[gameNum])
    return endScores
def doSimDummyFast(n):
    endScores = []
    for gameNum in range(n):
        moveNum =0
        board = generateRand([[0,0,0,0] for x in range(4)])
        while not Ai2048.isTerminal(board):
            moves = Ai2048.bestMove(board)
            #moves = Ai2048.bestMoveDepth(board,2)
            #moves = Ai2048.bestMoveHeuristic(board, 2)
            #moves = Ai2048.bestMoveHeuristicFast(board, 2)
            for move in moves:  # go through the moves and pick the first valid move
                if board != move[1]:
                    board = move[1]
                    break
            board = generateRand(board)
            moveNum += 1
            #print(f"moves this game: {moveNum}, biggest num this game = {Ai2048.biggestNum(board)}")
        endScores.append(Ai2048.biggestNum(board))
        #print(endScores[gameNum])
    return endScores
def doSim2(n):
    endScores = []
    for gameNum in range(n):
        moveNum =0
        board = generateRand([[0,0,0,0] for x in range(4)])
        while not Ai2048.isTerminal(board):
            #moves = Ai2048.bestMove(board)
            moves = Ai2048.bestMoveDepth(board, 2)
            #moves = Ai2048.bestMoveHeuristic(board, 2)
            moves = Ai2048.bestMoveHeuristicFast(board, 2)
            for move in moves:  # go through the moves and pick the first valid move
                if board != move[1]:
                    board = move[1]
                    break
            board = generateRand(board)
            moveNum += 1
            #print(f"moves this game: {moveNum}, biggest num this game = {Ai2048.biggestNum(board)}")
        endScores.append(Ai2048.biggestNum(board))
        #print(endScores[gameNum])
    return endScores
