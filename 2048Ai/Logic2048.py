# represent board as 2d array
# check all ranges in 2d or 1d for their first and last index matching with nothing or just spaces between them
# O(n^3) but nobody cares because n is 4 so its only 64 comparisons
TestCase = [[2, 2, 4, 4], [0, 2, 0, 2], [4, 0, 2, 4], [0, 0, 0, 2]]
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
                row[current + j] == 0 or row[current + j] == row[current]
            ):
                if row[current] == row[current + j]:
                    # we collapse
                    #print(f"collapse at:{current, j}")
                    ans[current] = row[current] * 2
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




def generateLUTleft():
    lut = {}
    def p(n):
        return 0 if n==0 else 2**n
    for a in range(14):
        for b in range(14):
            for c in range(14):
                for d in range(14):
                    lut[f"{p(a)}{p(b)}{p(c)}{p(d)}"] = pushLeftRow([p(a),p(b),p(c),p(d)])
    return lut
def generateLUTright():
    lut = {}
    def p(n):
        return 0 if n==0 else 2**n
    for a in range(14):
        for b in range(14):
            for c in range(14):
                for d in range(14):
                    lut[f"{p(a)}{p(b)}{p(c)}{p(d)}"] = pushRightRow([p(a),p(b),p(c),p(d)])
    return lut
lut_left = generateLUTleft()
lut_right = generateLUTright()
#ex_board = [[0,2,2,4] for _ in range(4)]
def pushRight(board):
    ns = [[] for _ in range(4)]
    for r in range(4):
        row = board[r]
        ns[r] = lut_right[f"{row[0]}{row[1]}{row[2]}{row[3]}"]
    return ns
def pushLeft(board):
    ns = [[] for _ in range(4)]
    for r in range(4):
        row = board[r]
        ns[r] = lut_left[f"{row[0]}{row[1]}{row[2]}{row[3]}"]
    return ns
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

