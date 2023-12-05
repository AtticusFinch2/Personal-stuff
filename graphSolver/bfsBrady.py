from collections import deque

def colorable(nverticies, edges):
    discovered = [i==1 for i in range(nverticies+1)]
    processed = [False]*(nverticies+1)
    parent = [0]*(nverticies+1)
    todo = []
    while todo:
        current = todo.popleft()
        for b in edges[current]:
            if not discovered[b]:
                todo.append(b)
                discovered[b] = True
                parent[b] = current
            processed[current] = True