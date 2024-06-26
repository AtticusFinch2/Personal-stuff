import Logic2048
import copy
import time
import random

scoreGrid = [[50,  30,  20,  20],
             [30,  20,  15,  15],
             [15,   5,   0,   0],
             [-5,  -5, -10, -15]]
scoreGrid2 = [[3**16, 3**15, 3**14, 3**13],
             [3**9,  3**10,  3**11, 3**12],
             [3**8,  3**7,  3**6,  3**5],
             [3**1,  3**2,  3**3,  3**4]]
example_board = [[0,0,2,2] for _ in range(4)]
MAX_INT = 2**30
def LossOf(board):
    value = 0
    for col in range(4):
        for row in range(4):
            value += scoreGrid2[col][row] * (board[col][row]**3)
    return value
def sortFirst(triple):
    return triple[0]

def bestMove(board):
    boards = [Logic2048.pushUp(board), Logic2048.pushDown(board), Logic2048.pushLeft(board), Logic2048.pushRight(board)]
    moves = ["up", "down", "left", "right"]
    results = [(LossOf(boards[x]), boards[x], moves[x]) for x in range(4)]
    results.sort(key=sortFirst)
    return results
def bestMove2DepthFake(board):
    boards1 = [Logic2048.pushUp(board), Logic2048.pushDown(board), Logic2048.pushLeft(board), Logic2048.pushRight(board)]
    boards2 = [[Logic2048.pushUp(b), Logic2048.pushDown(b), Logic2048.pushLeft(b), Logic2048.pushRight(b)] for b in boards1]
    boards = boards2[0] + boards2[1] + boards2[2] + boards2[3]
    moves = ["up" for _ in range(4)] + ["down" for _ in range(4)] + ["left"for _ in range(4)] + ["right"for _ in range(4)]
    results = [(LossOf(boards[x]), boards[x], moves[x]) for x in range(4)]
    results.sort(key=sortFirst)
    return results
#print(bestMove2DepthFake(example_board))
def isTerminal(board):
    '''for y in board:
        for x in y:
            if x==0: return False
    return True'''
    if Logic2048.pushRight(board) == Logic2048.pushLeft(board) and Logic2048.pushUp(board) == Logic2048.pushDown(board):
        return True
    return False
def miniOptions(board):
    zero_pool = []
    nz=0
    for y in range(4):
        for x in range(4):
            if board[x][y] == 0:
                zero_pool.append((x,y))
                nz += 1
    ans = [copy.deepcopy(board) for x in range(nz*2)]
    for child in range(0,nz):
        ans[child][zero_pool[child][0]][zero_pool[child][1]] = 2
    for child in range(nz, nz*2):
        ans[child][zero_pool[child-nz][0]][zero_pool[child-nz][1]] = 4
    return ans
def miniOptionsFast(board):
    zero_pool = []
    nz=0
    for y in range(4):
        for x in range(4):
            if board[x][y] == 0:
                zero_pool.append((x,y))
                nz+=1
    ans = [copy.deepcopy(board) for x in range(nz//2)]
    for child in range(nz//2):
        ans[child][zero_pool[child*2][0]][zero_pool[child*2][1]] = 2
    return ans
def maxOptions(board):
    return [Logic2048.pushUp(board), Logic2048.pushDown(board), Logic2048.pushLeft(board), Logic2048.pushRight(board)]


def minimax(node, depth, calcMini=True, loss_func=LossOf):
    if depth == 0 or isTerminal(node):
        return loss_func(node)
    value = MAX_INT
    children = miniOptions(node) if calcMini else maxOptions(node)
    for child in children:
        value = min(value, minimax(child, depth - 1, not calcMini))
    return value

def bestMoveDepth(board, depth):
    boards = [Logic2048.pushUp(board), Logic2048.pushDown(board), Logic2048.pushLeft(board), Logic2048.pushRight(board)]
    moves = ["up", "down", "left", "right"]
    results = [(minimax(boards[x], depth), boards[x], moves[x]) for x in range(4)]
    results.sort(key=sortFirst)
    return results

def emptyTilesHeuristic(board):#simply counting the empty tiles
    nz = 0
    for y in board:
        for x in y:
            if x == 0:
                nz += 1
    return nz

dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
def smoothnessHeuristic(board):  # penalize big differences between 2 given tiles
    ans = 0
    for y in range(4):
        for x in range(4):
            if board[x][y] != 0:
                current = board[x][y]
                for d in dirs:
                    newX = x+d[0]
                    newY = y+d[1]
                    if [newX>=0, newY>=0, newX<4, newY<4] == [True, True, True, True]:  # make sure in bounds
                        if board[newX][newY] != 0:
                            ans -= (current - board[newX][newY])  # this is the formula I made up
    return ans
def monotonyHeuristic(board):#make sure we go up in value as we go down and to the right
    ans=0
    for y in range(4):
        for x in range(4):
            if board[x][y] != 0:
                current = board[x][y]
                newX = x + 1
                newY = y + 1
                if newX < 4:  # make sure in bounds
                    if board[newX][y] < current:
                        ans -= (current - board[newX][y])**2
                if newY < 4:
                    if board[x][newY] < current:
                        ans -= (current - board[x][newY])**2
    return ans
def bigNumberHeuristic(board):
    sumN = 0
    for col in range(4):
        for row in range(4):
            sumN += board[row][col] ** 2
    return sumN
def biggestNum(board):
    maxN = 0
    for col in range(4):
        for row in range(4):
            maxN = max(maxN, board[row][col])
    return maxN
#print(emptyTilesHeuristic(example_board), smoothnessHeuristic(example_board), monotonyHeuristic(example_board), bigNumberHeuristic(example_board))
def heuristicCombination(board):
    e = 16-emptyTilesHeuristic(board)
    #s = smoothnessHeuristic(board)
    m = monotonyHeuristic(board)
    b = bigNumberHeuristic(board)
    return -1*(e+m+b)
def minimax2(node, depth, calcMini=True):
    if depth == 0 or isTerminal(node):
        return heuristicCombination(node)
    if calcMini:
        value = 0
        children = miniOptions(node)
        nC = len(children)  # num of Children
        if nC == 0:
            return MAX_INT
        for c in range(nC//2):
            value += minimax2(children[c], depth - 1, not calcMini)
        v1 = value // nC // 2
        value = 0
        for c in range(nC//2, nC):
            value += minimax2(children[c], depth - 1, not calcMini)
        v2 = value // nC // 2
        return ((v1*9) + v2) // 10
    else:
        value = MAX_INT
        children = maxOptions(node)
        for child in children:
            value = min(value, minimax2(child, depth - 1, not calcMini))
        return value

def bestMoveHeuristic(board, depth):
    boards = [Logic2048.pushUp(board), Logic2048.pushDown(board), Logic2048.pushLeft(board), Logic2048.pushRight(board)]
    moves = ["up", "down", "left", "right"]
    #print(boards)
    results = [(minimax2(boards[x], depth), boards[x], moves[x]) for x in range(4)]
    #print(board)
    #print(results)
    results.sort(key=sortFirst)
    return results
#print(bestMoveHeuristic(example_board, 0))
def bestMoveHeuristicFast(board, depth):
    boards = [Logic2048.pushUp(board), Logic2048.pushDown(board), Logic2048.pushLeft(board), Logic2048.pushRight(board)]
    moves = ["up", "down", "left", "right"]
    results = [(minimax2Fast(boards[x], depth), boards[x], moves[x]) for x in range(4)]
    results.sort(key=sortFirst)
    return results

def minimax2Fast(node, depth, calcMini=True):
    if depth == 0 or isTerminal(node):
        return heuristicCombination(node)
    if calcMini:
        value = 0
        children = miniOptionsFast(node)
        for child in children:
            value += minimax2(child, depth - 1, not calcMini)
        if len(children) == 0:
            return MAX_INT
        return value // len(children)
    else:
        value = MAX_INT
        children = maxOptions(node)
        for child in children:
            value = min(value, minimax2(child, depth - 1, not calcMini))
        return value


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

def doSim(n):
    endScores = []
    moveNum =0
    board = generateRand([[0,0,0,0] for x in range(4)])
    while not isTerminal(board):
        moves = bestMoveHeuristic(board, 2)
        #print(board)
        for move in moves:  # go through the moves and pick the first valid move
            if board != move[1]:
                board = move[1]
                break
        board = generateRand(board)
        moveNum += 1
    endScores.append(biggestNum(board))
    #print(board)
    return endScores
def doSimFast(n):
    endScores = []
    for gameNum in range(n):
        moveNum =0
        board = generateRand([[0,0,0,0] for x in range(4)])
        while not isTerminal(board):
            moves = bestMoveHeuristicFast(board, 2)
            for move in moves:  # go through the moves and pick the first valid move
                if board != move[1]:
                    board = move[1]
                    break
            board = generateRand(board)
            moveNum += 1
        endScores.append(biggestNum(board))
        #print(endScores[gameNum])
    return endScores
def doSimDummyFast(n):
    endScores = []
    for gameNum in range(n):
        moveNum =0
        board = generateRand([[0,0,0,0] for x in range(4)])
        while not isTerminal(board):
            moves = bestMove(board)
            for move in moves:  # go through the moves and pick the first valid move
                if board != move[1]:
                    board = move[1]
                    break
            board = generateRand(board)
            moveNum += 1
        endScores.append(biggestNum(board))
        #print(endScores[gameNum])
    return endScores
def doSim2(n):
    endScores = []
    for gameNum in range(n):
        moveNum =0
        board = generateRand([[0,0,0,0] for x in range(4)])
        while not isTerminal(board):
            moves = bestMoveDepth(board, 2)
            for move in moves:  # go through the moves and pick the first valid move
                if board != move[1]:
                    board = move[1]
                    break
            board = generateRand(board)
            moveNum += 1
        endScores.append(biggestNum(board))
        #print(endScores[gameNum])
    return endScores


def advancedStratOneIter(board):  # board -> board after x random moves
    for _ in range(30):  # x is here
        board = generateRand(board)
        if not isTerminal(board):
            possibleMoveDirs = [Logic2048.pushUp(board), Logic2048.pushDown(board), Logic2048.pushLeft(board), Logic2048.pushRight(board)]
            board = possibleMoveDirs[random.randrange(0, 4)]
        else:
            return board
    return board
def advancedStratValueOfMove(board):
    resultAll = 0
    b= copy.deepcopy(board)
    for _ in range(30):
        resultAll += heuristicCombination(advancedStratOneIter(b))
        b = board
    return resultAll / 100
def bestMoveAdvanced(board):
    boards = [Logic2048.pushUp(board), Logic2048.pushDown(board), Logic2048.pushLeft(board), Logic2048.pushRight(board)]
    moves = ["up", "down", "left", "right"]
    results = [(advancedStratValueOfMove(boards[x]), boards[x], moves[x]) for x in range(4)]
    results.sort(key=sortFirst)
    return results
def doSimAdvanced(n):
    endScores = []
    for _ in range(n):
        moveNum = 0
        board = generateRand([[0, 0, 0, 0] for x in range(4)])
        while not isTerminal(board):
            moves = bestMoveAdvanced(board)
            for move in moves:  # go through the moves and pick the first valid move
                if board != move[1]:
                    board = move[1]
                    break
            board = generateRand(board)
            moveNum += 1
        endScores.append(biggestNum(board))
    return endScores









myname = "BradenMiller"
def run_your_solver(version=3):
    match version:
        case 5:
            return doSimAdvanced(1)[0]  # new method IS REALLLLY SLOW AND REALLLLY BAD
        case 4:
            return doSimFast(1)[0]  # fast-ish but kinda bad
        case 3:
            return doSim(1)[0]  # Slowest but highest average score (use n=15)
        case 2:
            return doSim2(1)[0]  # minimax but with pretty bad weights
        case 1:
            return doSimDummyFast(1)[0]  # fast but stupid (n=2000)
def runtrials(n=50):
    for _ in range(n):
        starttime = time.time()
        maxtile = run_your_solver(3)
        endtime = time.time()
        runtime = endtime-starttime
        print(f'"REPORT","{myname}",{runtime},{maxtile}')
starttime2 = time.time()
if __name__ == '__main__':
    import cProfile
    with (cProfile.Profile() as pr):
        pr.enable()
        runtrials()
        pr.disable()
        pr.print_stats()
endtime2 = time.time()
print(endtime2-starttime2)
#print(bestMoveHeuristic([[0, 0, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 2))