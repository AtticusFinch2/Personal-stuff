import random, math, copy
from queue import PriorityQueue

adjListEx = {0:{1,7}, 1:{0,2,7}, 2:{1,3,5,8}, 3:{2,4,5}, 4:{3,5}, 5:{2,3,4,6}, 6:{5,7,8}, 7:{0,1,8,6}, 8:{2,6,7}}
weightsEx = {(0,1):4, (0,7):8, (1,0):4, (1,2):8, (1,7):11, (2,1):8, (2,3):7,
             (2,5):4, (2,8):2, (3,2):7, (3,4):9, (3,5):14, (4,3):9, (4,5):10,
             (5,2):4, (5,3):14, (5,4):10, (5,6):2, (6,5):2, (6,7):1, (6,8):6,
             (7,0):8, (7,1):11, (7,6):1, (7,8):7, (8,2):2, (8,6):6, (8,7):7}
# see https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/ for the graph i'm refrencing
# I DID NOT USE geeksforgeeks FOR THE CODE, ONLY FOR THE GRAPH


class weightedGraph:
    def __init__(self, weights, edges={}, adj={}):  # weights: {(Node1, Node2) : weight}
        self.edges = edges
        self.weights = weights
        self.adj = adj
        for edge in weights:
            self.adj[edge[0]] = set()
            self.adj[edge[1]] = set()
        for edge in weights:
            self.adj[edge[0]].add(edge[1])
            self.adj[edge[1]].add(edge[0])
        self.n = len(adj)
    def dijkstra(self, start):
        stack = PriorityQueue()
        stack.put((0, start, [start]))  # (dist, node, path)
        shortest_dist_to = {node: (math.inf, []) for node in range(self.n)}  # distance then path for each node
        shortest_dist_to[start] = (0, [start])
        while not stack.empty():
            (distToCurrent, current, path_to_current) = stack.get()
            if distToCurrent <= shortest_dist_to[current][0]:
                # if it's a slower path, just ignore it. This is the optimization of dijkstra's
                shortest_dist_to[current] = (distToCurrent, path_to_current)
                for neighbor in self.adj[current]:
                    d_to_neighbor = distToCurrent+(self.weights[(current, neighbor)])
                    # distance to neighbor is just distance to current and the weight of the edge between them
                    path_to_neighbor = path_to_current + [neighbor]
                    stack.put((d_to_neighbor, neighbor, path_to_neighbor))
        return shortest_dist_to
    def dijkstra_end(self, start, end):
        stack = PriorityQueue()
        stack.put((0, start, [start]))  # (dist, node, path)
        shortest_dist_to = {node: (math.inf, []) for node in range(self.n)}  # distance then path for each node
        shortest_dist_to[start] = (0, [start])
        while not stack.empty():
            (distToCurrent, current, path_to_current) = stack.get()
            if distToCurrent <= shortest_dist_to[current][0]:
                # if it's a slower path, just ignore it. This is the optimization of dijkstra's
                shortest_dist_to[current] = (distToCurrent, path_to_current)
                if current == end:
                    break
                for neighbor in self.adj[current]:
                    d_to_neighbor = distToCurrent+(self.weights[(current, neighbor)])
                    # distance to neighbor is just distance to current and the weight of the edge between them
                    path_to_neighbor = path_to_current + [neighbor]
                    stack.put((d_to_neighbor, neighbor, path_to_neighbor))
        return shortest_dist_to[end]

    def a_star(self, start, end: (float, float)):
        def potential(node: (float, float)):
            return math.sqrt((node[0]-end[0])**2 + (node[1]-end[1])**2)
        # now we reformat:
        for edge in self.weights:
            self.new_weights[edge] = self.weights[edge] + potential(edge[0]) - potential(edge[1])
        return self.dijkstra_end(start, end)

g = weightedGraph(weightsEx)
print(g.dijkstra_end(0,4))
