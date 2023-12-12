import copy
import numpy as np

# we store a board as 7x6 numPy array and
ex_board = np.array([[0, 0, 0, 1, 2, 1] for _ in range(6)])


def placeMove(board, colPlaced, player):
    if board[colPlaced][0] != 0:
        return board
    new_board = copy.deepcopy(board)
    for i in range(6):
        if new_board[colPlaced][i] != 0:
            new_board[colPlaced][i - 1] = player
    return new_board


def placeMoveNonCopy(board, colPlaced, player):
    if board[colPlaced][0] != 0:
        return board
    for i in range(6):
        if board[colPlaced][i] != 0:
            board[colPlaced][i - 1] = player
    return board


def placeMoveFast(board, colPlaced, player):  # returns where it goes, not new board
    if board[colPlaced][0] != 0:  # can't make move
        return (colPlaced, -1)
    for i in range(6):
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
