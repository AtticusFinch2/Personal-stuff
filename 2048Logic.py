# represent board as 2d array
# check all ranges in 2d or 1d for their first and last index matching with nothing or just spaces between them
# O(n^3) but nobody cares because n is 4 so its only 64 comparisons
TestCase = [[2, 2, 4, 4], [0, 2, 0, 4], [4, 0, 2, 4], [0, 0, 0, 2048]]


def pushLeftRow(row):
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
                    # print(f"collapse at:{current, j}")
                    ans[current] = row[current] * 2
                j += 1
            for behind in range(current):  # collapse all spaces behind
                if ans[behind] == 0:
                    ans[behind] = ans[current]
                    ans[current] = 0
                    # print(f"backpedal at:{behind, current}, ans:{ans}, row:{row}")
                    break
        row[current] = ans[current]
        # print(ans, row)
    return ans


def pushRightRow(row):
    row.reverse()
    ans = pushLeftRow(row)
    ans.reverse()
    return ans


def pushRight(board):
    ans = [[0, 0, 0, 0] for x in range(4)]
    for row in range(4):
        ans[row] = pushRightRow(board[row])
    return ans


def pushLeft(board):
    ans = [[0, 0, 0, 0] for x in range(4)]
    for row in range(4):
        ans[row] = pushLeftRow(board[row])
    return ans


def transposeSquare(twoDarr):
    ans = [[0, 0, 0, 0] for x in range(4)]
    for row in range(4):
        for col in range(4):
            ans[row][col] = twoDarr[col][row]
    return ans


def pushUp(board):
    ans = [[0, 0, 0, 0] for x in range(4)]
    tp = transposeSquare(board)
    ans = pushLeft(tp)
    ans = transposeSquare(ans)
    return ans


def pushDown(board):
    ans = [[0, 0, 0, 0] for x in range(4)]
    tp = transposeSquare(board)
    ans = pushRight(tp)
    ans = transposeSquare(ans)
    return ans


print(pushRight(TestCase))
