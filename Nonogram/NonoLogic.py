import copy

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
    return expandinner(rowLength, hintj)
def expandinner(rowLength, hintj, i=None, row=None):
    hint = copy.deepcopy(hintj)
    row = [99 for _ in range(rowLength)] if row is None else copy.deepcopy(row)
    i = 0 if i is None else i
    #print(row, hint, i)
    if i < rowLength:
        if len(hint)<=0:  # the rest of the row has to be 0
            row[i] = 0
            return expandinner(rowLength, hint, i=i+1, row=row)
        else:
            row[i] = 0
            zeroBranch = expandinner(rowLength, hint, i=i+1, row=row)  # branch if current box is 0
            if hint[0][0] <= rowLength-i:
                for i2 in range(hint[0][0]):  # if we have a hint, make all boxes in the range of the hint its value
                    index = i + i2
                    row[index] = hint[0][1]
                if rowLength - index >= 2 and len(hint) >= 2:  # if we have space and out next hint is the same type,
                    if hint[1][1] == hint[0][1]:
                        index += 1
                        row[index] = 0  # put white space
                hint.pop(0)  # we have used the firstmost hint
                valueBranch = expandinner(rowLength, hint, i=index+1, row=row)  # branch if current box is topmost hint
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
        s = 0
        for j in range(len(possibilities)):
            s += possibilities[j][i]
        if s == current * len(possibilities):
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
        bindings_left.append(collapse(refine(binding, expand(w, hints[y]))))
    return bindings_left


def getAllRequiredTop(h, w, oldboard, hints):
    bindings_top = []
    for x in range(w):
        binding = {y: oldboard[y][x] for y in range(h) if oldboard[y][x] != 99}
        bindings_top.append(collapse(refine(binding, expand(h, hints[x]))))
    return bindings_top



if __name__ == '__main__':
    hint = row_to_hint([0,1,1,1,0])
    print(hint)
    r = expand(5, hint)
    print(r)
    print(refine({1:1},r))
    print(collapse(r))
