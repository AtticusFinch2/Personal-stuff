import copy
import random
from collections import defaultdict

import numpy as np
MAX_INT = 2**30
branching = 3
initDepth = 5
edgeList = []



def move(node, branch):
    return 1
def static_value(node):
    return (random.randrange(-50, 50))
def isTerminal(node):
    return False
def minimax(node, depth, alpha, beta, maxing, t):
    if isTerminal(node) or depth>=initDepth:
        v = static_value(node)
        return v
    children = [move(node, branch) for branch in range(branching)]
    value = MAX_INT if not maxing else -MAX_INT
    k=0
    for child in children:
        edgeList.append(((depth+1, k), (depth, t)))
        x = minimax(child, depth+1, alpha, beta, not maxing, k)
        k+=1
        if maxing:
            value = max(value, x)
            alpha = max(value, x)
        else:
            value = min(value, x)
            beta = min(value, x)
        if beta <= alpha:
            break
    return value
root_value = minimax(1, 0, -MAX_INT, MAX_INT, True, 0)

