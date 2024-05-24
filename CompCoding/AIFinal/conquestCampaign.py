a, b, c = map(int, input().split())
arr = [[0 for x in range(b)] for i in range(a)]
#print(arr)
for i in range(c):
    r, c = map(int, input().split())
    arr[r - 1][c-1] = True
ans = 1

while sum([sum(arr[x]) for x in range(a)]) != a * b:
    ans+=1
    temp = set()
    for r in range(a):
        for c in range(b):
            if arr[r][c]:
                if (r - 1) in range(a):
                    temp.add((r-1, c))
                if (r + 1) in range(a):
                    temp.add((r+1, c))
                if (c - 1) in range(b):
                    temp.add((r, c -1))
                if (c + 1) in range(b):
                    temp.add((r, c +1))
    for x in temp:
        arr[x[0]][x[1]] = True


print(ans)