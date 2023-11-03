import random
from collections import deque
from collections import defaultdict
import pytest
import copy


def dfsOne(edges, start=1):
    stk = [start]
    visited = {start}
    now = 0
    timeIn = {start: 1}
    timeOut = {}
    path = []
    GETOUT = False
    while stk or path:
        if stk:
            current = stk.pop()
            now += 1
            timeIn[current] = now
            visited.add(current)
            isOutRun = False
        else:  # when stack empty and parent not, this is the TimeOut run
            current = path.pop()
            isOutRun = True
        weProcess = True
        temp = -1
        for edge in edges[current]:
            if edge not in visited:
                weProcess = False
                temp = edge
                break
        if weProcess:  # when we process current
            now += 1
            timeOut[current] = now
        else:
            stk.append(temp)
            path.append(current)
    return visited


def dfsAll(edges):  # O(V+E)
    sumVertVisited = 0
    nvert = len(edges)
    start = 1
    visited = set()
    while sumVertVisited < nvert:
        if start not in visited:
            visitedTemp = dfsOne(edges, start)
            for node in visitedTemp:
                visited.add(node)
                sumVertVisited += 1
        start += 1


def dfsPosn(edges, start=(0, 0)):
    stk = [start]
    visited = {start}
    now = 0
    timeIn = {start: 1}
    timeOut = {}
    path = []
    tree = {node: set() for node in edges}
    while stk or path:
        if stk:
            current = stk.pop()
            now += 1
            timeIn[current] = now
            visited.add(current)
            isOutRun = False
        else:  # when stack empty and parent not, this is the TimeOut run
            current = path.pop()
            isOutRun = True
        weProcess = True
        temp = -1
        for edge in edges[current]:
            if edge not in visited:
                weProcess = False
                temp = edge
                tree[temp].add(current)
                tree[current].add(temp)
                break
        if weProcess:  # when we process current
            now += 1
            timeOut[current] = now
        else:
            stk.append(temp)
            path.append(current)
    return tree


def dfsPosnRand(edges, start=(0, 0)):
    stk = [start]
    visited = {start}
    now = 0
    timeIn = {start: 1}
    timeOut = {}
    path = []
    tree = {node: set() for node in edges}
    while stk or path:
        if stk:
            current = stk.pop()
            now += 1
            timeIn[current] = now
            visited.add(current)
            isOutRun = False
        else:  # when stack empty and parent not, this is the TimeOut run
            current = path.pop()
            isOutRun = True
        weProcess = True
        temp = -1
        ##### RANDOMIZATION #####
        randEdges = list(edges[current])
        random.shuffle(randEdges)
        #########################
        for edge in randEdges:
            if edge not in visited:
                weProcess = False
                temp = edge
                tree[temp].add(current)
                tree[current].add(temp)
                break
        if weProcess:  # when we process current
            now += 1
            timeOut[current] = now
        else:
            stk.append(temp)
            path.append(current)
    return tree
