import copy
from functools import lru_cache
# a board is stored as an int[rows][cols]
# hints are a list of lists of [num, type]

def row_to_hint(row:[int]):  # O(N)
    if row == []:
        return []
    i = 0
    while i<len(row):
        if row[i] == 0:
            i+=1
            if i==len(row):
                return []
        else: break
    # now i is at first index of a color
    cur = row[i]
    i+=1
    j=0
    hint = [[1, cur]]
    while i<len(row):
        if row[i-1] == 0 and row[i] != 0:
            hint.append( [1, row[i]] )
            j += 1
        elif hint[j][1] == row[i]:
            hint[j][0] += 1
        elif row[i] != 0:
            hint.append([1, row[i]])
            j += 1
        i+=1
    hint.reverse()
    return hint


def transpose(mat):
    ans = [[0 for y in range(len(mat))] for x in range(len(mat[0]))]
    for row in range(len(mat[0])):
        for col in range(len(mat)):
            ans[row][col] = mat[col][row]
    return ans


def checkRowSolved(row, hint):
    row = [(0 if i==99 else i) for i in row]
    return hint == row_to_hint(row)


def expand(rowLength, hintk):
    hintj = copy.deepcopy(hintk)
    hintj.reverse()
    return expandinner(rowLength, hintj, {})
def expandBindings(rowLength, hintk, bindings):
    hintj = copy.deepcopy(hintk)
    hintj.reverse()
    return expandinner(rowLength, hintj, bindings)


def expandinner(rowLength, hintj, bindings, i=None, row=None):
    hint = copy.deepcopy(hintj)
    row = [99 for _ in range(rowLength)] if row is None else copy.deepcopy(row)
    i = 0 if i is None else i
    if i < rowLength:
        if len(hint)<=0:  # the rest of the row has to be 0
            row[i] = 0
            if i in bindings and bindings[i] != 0:
                return []
            return expandinner(rowLength, hint, bindings, i=i+1, row=row)
        else:
            row[i] = 0
            if i in bindings and bindings[i] != 0:
                zeroBranch = []
            else:
                zeroBranch = expandinner(rowLength, hint, bindings, i=i+1, row=row)  # branch if current box is 0
            if hint[0][0] <= rowLength-i:
                for i2 in range(hint[0][0]):  # if we have a hint, make all boxes in the range of the hint its value
                    index = i + i2
                    if index in bindings and bindings[index] != hint[0][1]:
                        return zeroBranch
                    row[index] = hint[0][1]
                if rowLength - index >= 2 and len(hint) >= 2:  # if we have space and our next hint is the same type,
                    if hint[1][1] == hint[0][1]:
                        index += 1
                        if index in bindings and bindings[index] != 0:
                            return zeroBranch
                        row[index] = 0  # put white space
                hint.pop(0)  # we have used the firstmost hint
                valueBranch = expandinner(rowLength, hint, bindings, i=index+1, row=row)  # branch if current box is topmost hint
                return zeroBranch+valueBranch
            return zeroBranch
    # if code reaches this point, we are at a leaf.
    # now we need to determine whether the leaf is valid under the original hints
    if len(hint) > 0:  # we could replace this with if hint: but i wanted to make my code more readable
        return []  # we are using this value as our return for no valid solutions, since it will just get added above.
    return [row]


def collapse(possibilities):
    if possibilities == []:
        return {}
    ans = {}
    for i in range(len(possibilities[0])):
        current = possibilities[0][i]
        bound = True
        for j in range(len(possibilities)):
            if possibilities[j][i] != current:
                bound = False
        if bound:
            ans[i] = current  # index : type
    return ans


def refine(bindings, possibilities):
    if bindings == {}:
        return possibilities
    ans = []
    for possibility in possibilities:
        valid = True
        for key in bindings:
            if possibility[key] != bindings[key]:
                valid = False
        if valid:
            ans.append(possibility)
    return ans


def getAllRequiredLeft(h, w, oldboard, hints):
    bindings_left = []
    for y in range(h):
        binding = {x: oldboard[y][x] for x in range(w) if oldboard[y][x] != 99}
        #print(f"input:{[oldboard[y][x] for x in range(w)]} \nbindings: {binding}")
        #print(f"the thing {refine(binding, expand(w, hints[y]))}")
        bindings_left.append(collapse(expandBindings(w, hints[y], binding)))
    return bindings_left


def getAllRequiredTop(h, w, oldboard, hints):
    bindings_top = []
    for x in range(w):
        binding = {y: oldboard[y][x] for y in range(h) if oldboard[y][x] != 99}
        bindings_top.append(collapse(expandBindings(h, hints[x], binding)))
    return bindings_top


def getStuckRowCol(oldboard):
    stuckRow = set()
    stuckCol = set()
    for y in range(len(oldboard)):
        for x in range(len(oldboard[0])):
            if oldboard[y][x] == 99:
                stuckRow.add(y)
                stuckCol.add(x)
    return list(stuckRow), list(stuckCol)


def check(board, lefthints, tophints, transposedboard):
    for row in range(len(lefthints)):
        if not checkRowSolved(board[row], lefthints[row]):
            return False
    for col in range(len(tophints)):
        if not checkRowSolved(transposedboard[col], tophints[col]):
            return False
    return True

def solveStuck(board, left_hints, top_hints):
    sr, sc = getStuckRowCol(board)
    return solveStuck_inner(sr, sc, board, left_hints, top_hints)
def solveStuck_inner(stuckRow, stuckCol, oldboard, lefthints, tophints):
    w = len(oldboard[0])
    h = len(oldboard)
    if stuckRow:
        current = stuckRow.pop()
        current_hints = lefthints[current]
        binding = {x: oldboard[current][x] for x in range(w) if oldboard[current][x] != 99}
        #print(binding, current_hints)
        permutations = expandBindings(w, current_hints, binding)
        #print(permutations, current, "ROW")
        board = copy.deepcopy(oldboard)
        for branch in permutations:
            board[current] = branch
            newSR = copy.deepcopy(stuckRow)
            newSC = copy.deepcopy(stuckCol)
            newANS = solveStuck_inner(newSR, newSC, board, lefthints, tophints)
            if newANS:
                return newANS
        return None
    elif stuckCol:
        current = stuckCol.pop()
        current_hints = tophints[current]
        binding = {y: oldboard[y][current] for y in range(h) if oldboard[y][current] != 99}
        permutations = expandBindings(h, current_hints, binding)
        #print(permutations, binding, current, "COL")
        board = copy.deepcopy(oldboard)
        for branch in permutations:
            for y in range(h):
                board[y][current] = branch[y]
            newSR = copy.deepcopy(stuckRow)
            newSC = copy.deepcopy(stuckCol)
            newANS = solveStuck_inner(newSR, newSC, board, lefthints, tophints)
            if newANS:
                return newANS
        return None
    else:
        #print(check(oldboard, lefthints, tophints, transpose(oldboard)), oldboard)
        if check(oldboard, lefthints, tophints, transpose(oldboard)):
            return oldboard
        return None


def stuckTestCase():
    board = [[0, 0, 0, 2, 0, 0, 2, 0, 0, 0], [0, 0, 0, 2, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 99, 99, 0, 0, 99, 99, 0, 0], [0, 0, 99, 99, 2, 2, 99, 99, 0, 0]]
    lefthints = [[[1, 2], [1, 2]], [[1, 2], [1, 2]], [], [[1, 2], [1, 2]], [[4,2]]]
    tophints = [[], [], [[1, 2]], [[1, 2], [2, 2]], [[1, 2]], [[1, 2]], [[1, 2], [2, 2]], [[1, 2]], [], []]
    correctboard = [[0, 0, 0, 2, 0, 0, 2, 0, 0, 0], [0, 0, 0, 2, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 2, 2, 2, 2, 0, 0, 0]]
    sr, sc = getStuckRowCol(board)
    #print(sr,sc)
    ans = solveStuck_inner(sr, sc, board, lefthints, tophints)
    print(ans)
    print(f"correct? {ans == correctboard}")


if __name__ == '__main__':
    hint = row_to_hint([2,3,3,0,2,2,2,2,0,0])
    print(hint)
    r = expand(10, hint)
    print(r)
    #print(refine({1:1},r))
    print(collapse(r))
    stuckTestCase()