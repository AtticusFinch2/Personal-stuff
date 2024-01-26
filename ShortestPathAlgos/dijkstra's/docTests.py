import dijkstraLogic

weights = {(1, 2): 10, (2, 1): 10, (1, 3): 20, (3, 1): 20, (1, 4): 50, (4, 1): 50, (2, 6): 60, (6, 2): 60, (3, 6): 40, (6, 3): 40, (4, 5): 1, (5, 4): 1, (5, 6): 5, (6, 5): 5}

distances, parents = dijkstraLogic.dijkstra(weights, start=1)
print(distances, parents)
assert distances == {1: 0, 2: 10, 3: 20, 4: 50, 5: 51, 6: 56}
assert parents == {1: None, 2: 1, 3: 1, 4: 1, 5: 4, 6: 5}