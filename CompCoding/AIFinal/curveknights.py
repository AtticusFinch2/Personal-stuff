
N, M = map(int, input().split())

inp = input().split()
wants = []
for item in inp:
    wants.append(int(item))

adj = {x:[] for x in range(N)}
for i in range(M):
    u, v, w = map(int, input().split())
    adj[v].append((u,w))

ans = [0 for _ in range(N)]
stack = []
for item in range(len(wants)):
    if wants[item] != 0:
        stack.append((item, wants[item])) # (what we need, how much we need of it)
visiting = set()
while stack:
    (currentIndex, currentWeight) = stack.pop()
    visiting.remove(currentIndex)
    ans[currentIndex] += currentWeight
    for (ingredient, amt) in adj[currentIndex]:
        if ingredient in visiting:
            stack
        visiting.add(ingredient)
        stack.append((ingredient, (amt*currentWeight)))

s = ""
for item in range(N-1):
    s += str(ans[item]) + " "
s += str(ans[N-1])
#print(s)