import copy
import math
from collections import defaultdict
import heapq
import sys


def bubble_down(heap, loc):
    end = len(heap)
    start_loc = loc
    new = heap[loc]
    child_loc = 2 * loc + 1  # left child
    while child_loc < end:
        right = child_loc + 1 #right child
        if right < end and not heap[child_loc] < heap[right]:
            child_loc = right
        heap[loc] = heap[child_loc]
        # we blindly move smaller child up until we get to leaf
        loc = child_loc
        child_loc = 2 * loc + 1  # new left child
    # now, the heap is sorted except for the new item and the final leaf node
    #    (loc is now the location of the leaf)
    # we just put new item at the leaf node and bubble up, since it's faster
    heap[loc] = new
    bubble_up(heap, start_loc, loc)


def bubble_up(heap, start_bubble_pos, loc):
    newitem = heap[loc]
    while loc > start_bubble_pos:
        parentLoc = (loc - 1) >> 1
        #print(heap)
        parent = heap[parentLoc]
        #print(newitem, parent)
        if newitem < parent:
            heap[loc] = parent
            loc = parentLoc
            continue
        break
    heap[loc] = newitem


def heappop(heap):
    last = heap.pop()
    # put the last value at the front and then re-sort
    if heap:
        min_val = heap[0]
        heap[0] = last
        bubble_down(heap, 0)
        return min_val
    return last


def heappush(heap, value):
    heap.append(value)  # increase list size.
    bubble_up(heap, 0, len(heap)-1)



def dijkstra_faster(start, weights, adj):
    heap = [(0, start)]  # (dist, node)
    shortest_dist_to = defaultdict(lambda: math.inf)  # distance then parent for each node
    shortest_dist_to[start] = 0
    visited = set()
    while heap:
        (distToCurrent, current) = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        #print(adj[current])
        for neighbor in adj[current]:
            if neighbor not in shortest_dist_to or shortest_dist_to[neighbor] > shortest_dist_to[current]+weights[(current, neighbor)]:
                shortest_dist_to[neighbor] = shortest_dist_to[current]+weights[(current, neighbor)]
                heapq.heappush(heap, (distToCurrent+weights[(current, neighbor)], neighbor))
    return shortest_dist_to



lines = sys.stdin.readlines()
line1 = lines[0]
xs = line1.strip().split()
n, m = int(xs[0]), int(xs[1])
weights = {}
adj = defaultdict(lambda: [])
c = 1
while c <= m:
    start, end, cost = map(int, lines[c].strip().split())
    adj[start].append(end)
    if (start, end) in weights:
        cost = min(cost, weights[(start, end)])
    weights[(start, end)] = cost
    c += 1
dist = dijkstra_faster(1, weights, adj)
strOut = ""
for i in range(1, n + 1):
    strOut += str(dist[i]) + " "
print(strOut)


