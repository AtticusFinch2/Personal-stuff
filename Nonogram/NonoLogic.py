

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


if __name__ == '__main__':
  hint = row_to_hint([0,0,1,1,0,1,2,2,1,0])
  print(checkRowSolved([0,0,1,1,0,1,2,2,1,0], hint))
  print(transpose([[1 for i in range(10)] for i in range(5)]))