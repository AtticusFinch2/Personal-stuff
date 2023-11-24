import Logic2048
import copy
scoreGrid = [[50,  30,  20,  20],
             [30,  20,  15,  15],
             [15,   5,   0,   0],
             [-5,  -5, -10, -15]]
scoreGrid2 = [[4**15, 4**14, 4**13, 4**12],
             [4**8,  4**9,  4**10, 4**11],
             [4**7,  4**6,  4**5,  4**4],
             [4**0,  4**1,  4**2,  4**3]]
example_board = [[0,0,2,0] for x in range(4)]
MAX_INT = 2**30
def LossOf(board):
    value = 0
    for col in range(4):
        for row in range(4):
            value += scoreGrid[col][row] * board[col][row]
    return value

def bestMove(board):
    results = [Logic2048.pushUp(board), Logic2048.pushDown(board), Logic2048.pushLeft(board), Logic2048.pushRight(board)]
    moves = ["up", "down", "left", "right"]
    min_loss = LossOf(results[0])
    min_loss_move = "CAN'T MAKE BEST MOVE"
    for i in range(4):
        curLoss = LossOf(results[i])
        if results[i] != board and curLoss <= min_loss:
            min_loss_move = moves[i]
            min_loss = curLoss
    return min_loss_move
def isTerminal(board):
    for y in board:
        for x in y:
            if x==0: return False
    return True
def miniOptions(board):
    zero_pool = []
    nz=0
    for y in range(4):
        for x in range(4):
            if board[x][y] == 0:
                zero_pool.append((x,y))
                nz+=1
    ans = [copy.deepcopy(board) for x in range(nz*2)]
    for child in range(nz):
        ans[child][zero_pool[child][0]][zero_pool[child][1]] = 2
    for child in range(nz, nz*2):
        ans[child][zero_pool[child-nz][0]][zero_pool[child-nz][1]] = 4
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
    results = [Logic2048.pushUp(board), Logic2048.pushDown(board), Logic2048.pushLeft(board), Logic2048.pushRight(board)]
    moves = ["up", "down", "left", "right"]
    min_loss = minimax(results[0], depth)
    min_loss_move = "CAN'T MAKE BEST MOVE"
    for i in range(4):
        curLoss = minimax(results[i], depth)
        if results[i] != board and curLoss <= min_loss:
            min_loss_move = moves[i]
            min_loss = curLoss
    return min_loss_move

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
                            ans += current * ((current - board[newX][newY])**2)  # this is the formula I made up
    return ans
def monotonyHeuristic(board):#make sure we go up in value as we go down and to the right
    ans=0
    for y in range(4):
        for x in range(4):
            if board[x][y] != 0:
                current = board[x][y]
                newX = x + 1
                newY = y + 1
                if [newX < 4, newY < 4] == [True, True]:  # make sure in bounds
                    if board[newX][y] > current:
                        ans += board[newX][y] * current
                    if board[x][newY] > current:
                        ans += board[x][newY] * current
    return ans
print(emptyTilesHeuristic(example_board), smoothnessHeuristic(example_board), monotonyHeuristic(example_board))

def heuristicCombination(board):
    e = emptyTilesHeuristic(board) * 100
    s = smoothnessHeuristic(board) // 20
    m = monotonyHeuristic(board)
    return -1*(e+s+m)

def bestMoveHeuristic(board, depth):
    results = [Logic2048.pushUp(board), Logic2048.pushDown(board), Logic2048.pushLeft(board), Logic2048.pushRight(board)]
    moves = ["up", "down", "left", "right"]
    min_loss = minimax(results[0], depth, loss_func=heuristicCombination)
    min_loss_move = "CAN'T MAKE BEST MOVE"
    for i in range(4):
        curLoss = minimax(results[i], depth)
        if results[i] != board and curLoss <= min_loss:
            min_loss_move = moves[i]
            min_loss = curLoss
    return min_loss_move