import copy
import random
from collections import defaultdict
import math
import numpy as np
MAX_INT = 2**30
correct = []

def alphabeta_eval(edges, values, root_node, maximizingPlayerInit, bounds:[int]):
    countF = 0
    def minimax(node, depth, maximax, minimin, maximizingPlayer):
        nonlocal countF, values, edges
        if len(edges[node]) == 0 or depth<=0:
            countF+=1
            v = values[node]
            return v
        value = MAX_INT if not maximizingPlayer else -MAX_INT
        for child in edges[node]:
            x = minimax(child, depth-1, maximax, minimin, not maximizingPlayer)
            if maximizingPlayer:
                value = max(value, x)
                maximax = max(maximax, x)
            else:
                value = min(value, x)
                minimin = min(minimin, x)
            if minimin <= maximax:
                break
        values[node] = value
        return value
    root_val = minimax(root_node, 10, bounds[0], bounds[1], maximizingPlayerInit)
    return countF

edges = {0:[1, 2], 1:[3, 4], 2:[5, 6], 3:[], 4:[], 5:[], 6:[]}
values = [0,0,0,12,-7,-17,-15]
count = alphabeta_eval(edges, values, 0, True, [-math.inf, math.inf])
print(f"count == {count}\nvalues == {values}")

