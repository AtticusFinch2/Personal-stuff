import random, math, copy

adjListEx = {0:{1,7}, 1:{0,2,7}, 2:{1,3,5,8}, 3:{2,4,5}, 4:{3,5}, 5:{2,3,4,6}, 6:{5,7,8}, 7:{0,8,6}, 8:{2,6,7}}
weightsEx = {(0,1):4, (0,7):8, (1,0):4, (1,2):8, (1,7):11, (2,1):8, (2,3):7, (2,5):4, (2,8):2,
             (3,2):7, (3,4):9, (3,5):14, (4,3):9, (4,5):10}
# see https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/


class weightedGraph:
    def __init__(self, edges, weights, adj={}):  # weights: {(Node1, Node2) : weight}
        self.edges = edges
        self.weights = weights
        self.adj = adj
        for edge in edges:
            self.adj[edge[0]] = {}
            self.adj[edge[1]] = {}
        for edge in edges:
            self.adj[edge[0]].add(edge[1])
            self.adj[edge[1]].add(edge[0])
        self.n = len(adj)
    def dijkstra(self, start):
        stack = [(start, 0)]
        visited = {start}
        shortest_dist_to = {(start, 0)}
        while stack:
            (current, distToCurrent) = stack.pop()
            if current not in visited:
                shortest_dist_to.add(current, distToCurrent)
                visited.add(current)
                for neighbor in self.adj[current] not in visited:
                    stack.append((neighbor, distToCurrent+(self.weights[(current, neighbor)])))
        return shortest_dist_to


