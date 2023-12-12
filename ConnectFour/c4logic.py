import copy
import random
import numpy as np
# we store a board as 6x7 numPy array and
ex_board = np.array([[0,0,0,0,1,2,1]for _ in range(6)])


def placeMove(board, colPlaced, player):
    if board[colPlaced][0] !=0:
        return board
    new_board = copy.deepcopy(board)
    for i in range(7):
        if new_board[colPlaced][i] != 0:
            new_board[colPlaced][i-1] = player
    return new_board


def placeMoveFast(board, colPlaced, player):  # Not memory safe but doesn't use deepcopy
    if board[colPlaced][0] != 0:
        return board
    for i in range(7):
        if board[colPlaced][i] != 0:
            board[colPlaced][i - 1] = player
    return board


def wins(board):
    # rows
    for row in range(board.shape[0]):
        for col in range(board.shape[1] - 3):
            if board[row, col] == board[row, col + 1] == board[row, col + 2] == board[row, col + 3] != 0:
                return True

    # cols
    for col in range(board.shape[1]):
        for row in range(board.shape[0] - 3):
            if board[row, col] == board[row + 1, col] == board[row + 2, col] == board[row + 3, col] != 0:
                return True

    # diagonals (from top-left to bottom-right)
    for row in range(board.shape[0] - 3):
        for col in range(board.shape[1] - 3):
            if board[row, col] == board[row + 1, col + 1] == board[row + 2, col + 2] == board[row + 3, col + 3] != 0:
                return True

    # diagonals pt.2 electric boogaloo (from top-right to bottom-left)
    for row in range(board.shape[0] - 3):
        for col in range(3, board.shape[1]):
            if board[row, col] == board[row + 1, col - 1] == board[row + 2, col - 2] == board[row + 3, col - 3] != 0:
                return True

    return False