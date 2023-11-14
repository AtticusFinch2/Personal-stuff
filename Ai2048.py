import Logic2048
scoreGrid = [[50,  30,  20,  20],
             [30,  20,  15,  15],
             [15,   5,   0,   0],
             [-5,  -5, -10, -15]]
MAX_INT = 2**30
def LossOf(board):
    value = 0
    for col in range(4):
        for row in range(4):
            value += scoreGrid[col][row] * board[col][row]
    return value
board = [[0,0,2,0]for x in range(4)]
print(LossOf(board))
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