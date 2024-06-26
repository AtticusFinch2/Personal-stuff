import copy
import numpy as np

# we store a board as 7x6 numPy array and
ex_board = np.array([[0, 0, 0, 1, 2, 1] for _ in range(6)])
ex_board_empty = np.array([[0, 0, 0, 0, 0, 0] for _ in range(6)])
board_ex = np.array(
    [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 2, 2],
        [0, 0, 0, 0, 2, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 2],
        [0, 0, 0, 1, 1, 1],
    ]
)


def placeMove(board, colPlaced, player):
    if board[colPlaced][0] != 0:
        return board
    new_board = np.copy(board)
    for i in range(board.shape[1]):
        if new_board[colPlaced][i] != 0:
            new_board[colPlaced][i - 1] = player
            break
        if i == board.shape[1] - 1:
            new_board[colPlaced][i] = player
    return new_board


def placeMoveNonCopy(board, colPlaced, player):
    if board[colPlaced][0] != 0:
        return board
    for i in range(board.shape[1]):
        if board[colPlaced][i] != 0:
            board[colPlaced][i - 1] = player
    return board


def placeMoveFast(board, colPlaced):  # returns where it goes, not new board
    if board[colPlaced][0] != 0:  # can't make move
        return (colPlaced, -1)
    for i in range(board.shape[1]):
        if board[colPlaced][i] != 0:
            return (colPlaced, i - 1)
    return (colPlaced, 5)


def wins(board):
    for row in range(board.shape[0]):  # check rows
        for col in range(board.shape[1] - 3):
            if (
                1
                == board[row, col]
                == board[row, col + 1]
                == board[row, col + 2]
                == board[row, col + 3]
                != 0
            ):
                return 1
            if (
                2
                == board[row, col]
                == board[row, col + 1]
                == board[row, col + 2]
                == board[row, col + 3]
                != 0
            ):
                return 2
    for col in range(board.shape[1]):  # cols
        for row in range(board.shape[0] - 3):
            if (
                1
                == board[row, col]
                == board[row + 1, col]
                == board[row + 2, col]
                == board[row + 3, col]
                != 0
            ):
                return 1
            if (
                2
                == board[row, col]
                == board[row + 1, col]
                == board[row + 2, col]
                == board[row + 3, col]
                != 0
            ):
                return 2
    for row in range(board.shape[0] - 3):  # diagonals (from top-left to bottom-right)
        for col in range(board.shape[1] - 3):
            if (
                1
                == board[row, col]
                == board[row + 1, col + 1]
                == board[row + 2, col + 2]
                == board[row + 3, col + 3]
                != 0
            ):
                return 1
            if (
                2
                == board[row, col]
                == board[row + 1, col + 1]
                == board[row + 2, col + 2]
                == board[row + 3, col + 3]
                != 0
            ):
                return 2
    for row in range(
        board.shape[0] - 3
    ):  # diagonals pt.2 electric boogaloo (from top-right to bottom-left)
        for col in range(3, board.shape[1]):
            if (
                1
                == board[row, col]
                == board[row + 1, col - 1]
                == board[row + 2, col - 2]
                == board[row + 3, col - 3]
                != 0
            ):
                return 1
            if (
                2
                == board[row, col]
                == board[row + 1, col - 1]
                == board[row + 2, col - 2]
                == board[row + 3, col - 3]
                != 0
            ):
                return 2
    return 0


def legalMoves(board):
    for col in range(board.shape[1]):
        if board[col][0] == 0:
            return True
    return False


switch = {1: 2, 2: 1, 0: 0}


def static_value(board, player):
    ans = 0
    for col in range(board.shape[0]):  # check cols
        for row in range(board.shape[1] - 3):
            a = [
                board[col, row],
                board[col, row + 1],
                board[col, row + 2],
                board[col, row + 3],
            ]
            p1 = a.count(player)
            p2 = a.count(switch[player])
            # ans += (-1*(p2>0 and p1==0)*(p2**6))
            if p2 > 0 and p1 == 0:  # if enemy row detected
                ans -= p2**6
            elif p2 > 0:
                ans = ans
            else:
                ans += p1**6

    for col in range(board.shape[0] - 3):  # rows
        for row in range(board.shape[1]):
            a = [
                board[col, row],
                board[col + 1, row],
                board[col + 2, row],
                board[col + 3, row],
            ]
            p1 = a.count(player)
            p2 = a.count(switch[player])
            # ans += (-1 * (p2 > 0 and p1 == 0) * (p2 ** 6)) + ((not p2 > 0 and not p1 == 0) * (p1 ** 6))
            if p2 > 0 and p1 == 0:  # if enemy row detected
                ans -= p2**6
            elif p2 > 0:
                ans = ans
            else:
                ans += p1**6

    for col in range(board.shape[0] - 3):  # diagonals (from top-left to bottom-right)
        for row in range(board.shape[1] - 3):
            a = [
                board[col, row],
                board[col + 1, row + 1],
                board[col + 2, row + 2],
                board[col + 3, row + 3],
            ]
            p1 = a.count(player)
            p2 = a.count(switch[player])
            # ans += (-1 * (p2 > 0 and p1 == 0) * (p2 ** 6))
            if p2 > 0 and p1 == 0:  # if enemy row detected
                ans -= p2**6
            elif p2 > 0:
                ans = ans
            else:
                ans += p1**6
    for col in range(
        board.shape[0] - 3
    ):  # diagonals pt.2 electric boogaloo (from top-right to bottom-left)
        for row in range(3, board.shape[1]):
            a = [
                board[col, row],
                board[col + 1, row - 1],
                board[col + 2, row - 2],
                board[col + 3, row - 3],
            ]
            p1 = a.count(player)
            p2 = a.count(switch[player])
            # ans += (-1 * (p2 > 0 and p1 == 0) * (p2 ** 6))
            if p2 > 0 and p1 == 0:  # if enemy row detected
                ans -= p2**6
            elif p2 > 0:
                ans = ans
            else:
                ans += p1**6

    return ans


MAX_INT = 2**30


def convert(player):
    if player:
        return 1
    else:
        return 2


adjust = {1: 1, 2: -1, 0: 0}
WinnerInt = 1000000


def minimax(node, depth, player, globalMover, maximax = -MAX_INT, minimin = MAX_INT):
    if depth == 0:
        return static_value(node, player)  # * adjust[player]
    winner = wins(node)
    if winner != 0:
        return WinnerInt * adjust[winner]
    value = MAX_INT * -1 * adjust[player]
    children = [
        np.array(placeMove(node, col, player))
        for col in [4,5,3,6,2,1,0]
        if node[col][0] == 0
    ]
    for child in children:
        x = minimax(child, depth - 1, switch[player], globalMover, maximax=maximax, minimin=minimin)
        if player == globalMover:
            value = min(value, x)
            minimin = min(minimin, x)
            if minimin <= maximax:
                break
        else:
            value = max(value, x)
            maximax = max(maximax, x)
            if maximax >= minimin:
                break
    return value  # * adjust[player]


def sortFirst(triple):
    return triple[0]


def best_move(board, player, depth):  # returns value of each move
    moves = []
    adjust[player] = -1
    adjust[switch[player]] = 1
    for move in range(7):
        placement = placeMoveFast(board, move)
        new_board = copy.deepcopy(board)
        new_board[placement[0]][placement[1]] = player
        if board[move][0] == 0:
            moves.append(
                (minimax(new_board, depth - 1, switch[player], player), move, new_board)
            )
    moves.sort(key=sortFirst)
    return moves[0]


import time

starttime2 = time.time()
if __name__ == "__main__":
    import cProfile

    with cProfile.Profile() as pr:
        pr.enable()
        # for _ in range(2000):
        print(best_move(board_ex, 1, 5))
        pr.disable()
        pr.print_stats(sort="tottime")
endtime2 = time.time()
