import Logic2048
import copy
scoreGrid = [[50,  30,  20,  20],
             [30,  20,  15,  15],
             [15,   5,   0,   0],
             [-5,  -5, -10, -15]]
scoreGrid2 = [[4**16, 4**15, 4**14, 4**13],
             [4**9,  4**10,  4**11, 4**12],
             [4**8,  4**7,  4**6,  4**5],
             [4**1,  4**2,  4**3,  4**4]]
example_board = [[0,0,2,2] for x in range(4)]
MAX_INT = 2**30
def LossOf(board):
    value = 0
    for col in range(4):
        for row in range(4):
            value += scoreGrid[col][row] * (board[col][row]**2)
    return value

def bestMove(board):
    boards = [Logic2048.pushUp(board), Logic2048.pushDown(board), Logic2048.pushLeft(board), Logic2048.pushRight(board)]
    moves = ["up", "down", "left", "right"]
    results = [(LossOf(boards[x]), boards[x], moves[x]) for x in range(4)]
    results.sort(key=sortFirst)
    return results
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
                nz+=1
    ans = [copy.deepcopy(board) for x in range(nz)]#*2)]
    for child in range(0,nz,2):
        ans[child][zero_pool[child][0]][zero_pool[child][1]] = 2
    #for child in range(nz, nz*2):
    #    ans[child][zero_pool[child-nz][0]][zero_pool[child-nz][1]] = 4
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
    #e = 16-emptyTilesHeuristic(board)
    #s = smoothnessHeuristic(board)
    m = monotonyHeuristic(board)
    b = bigNumberHeuristic(board)
    return -1*(m+b)
def minimax2(node, depth, calcMini=True):
    if depth == 0 or isTerminal(node):
        return heuristicCombination(node)
    if calcMini:
        value = 0
        children = miniOptions(node)
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
def sortFirst(triple):
    return triple[0]
def bestMoveHeuristic(board, depth):
    boards = [Logic2048.pushUp(board), Logic2048.pushDown(board), Logic2048.pushLeft(board), Logic2048.pushRight(board)]
    moves = ["up", "down", "left", "right"]
    results = [(minimax2(boards[x], depth), boards[x], moves[x]) for x in range(4)]
    results.sort(key=sortFirst)
    return results
#print(bestMoveHeuristic(example_board, 0))