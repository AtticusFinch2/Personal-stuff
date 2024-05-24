

def dist(param1, param2):
    return (param1[0]-param2[0])**2 + (param1[1]-param2[1])**2


n, e, p = map(int, input().split())
nodes = [(0,0) for _ in range(n)]
lengths = []  # (length, fromIndex, toIndex)
for i in range(n):
    x, y = map(float, input().split())
    for nodeindex in range(i):
        if nodeindex < e and i < e:
            lengths.append((0, i, nodeindex))
        else:
            lengths.append((dist((x,y), nodes[nodeindex]), i, nodeindex))
    nodes[i] = (x,y)
lengths = sorted(lengths, key=lambda t: t[0])  # sort lengths, we leave the dist squared
#print(lengths)
parents = [node for node in range(n)]
ranks = [1 for _ in range(n)]


def find(u):
    while u != parents[u]:
        # path compression technique
        parents[u] = parents[parents[u]]
        u = parents[u]
    return u


total_length = 0
for i in range(p):  # get the already placed cables
    u, v = map(int, input().split())
    u-=1
    v-=1
    root_u, root_v = find(u), find(v)
    if root_u == root_v:
        continue
    if ranks[root_u] > ranks[root_v]:
        parents[root_v] = root_u
    elif ranks[root_v] > ranks[root_u]:
        parents[root_u] = root_v
    else:
        parents[root_u] = root_v
        ranks[root_v] += 1

for i in range(len(lengths)):  # union all the distances
    connection = lengths[i]
    u, v = connection[1], connection[2]
    root_u, root_v = find(u), find(v)
    if root_u == root_v:
        continue
    total_length += connection[0]**0.5  # this is the part that gets us our answer
    if ranks[root_u] > ranks[root_v]:
        parents[root_v] = root_u
    elif ranks[root_v] > ranks[root_u]:
        parents[root_u] = root_v
    else:
        parents[root_u] = root_v
        ranks[root_v] += 1
print(format(total_length, '.6f'))

