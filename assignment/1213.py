import numpy as np


def dijkstra(graph, start):
    num_vertices = graph.shape[0]
    distances = [float('inf')] * num_vertices
    found = [0] * num_vertices

    distances[start] = 0
    found[start] = 1

    steps = []
    steps.append((start, list(found), list(distances)))

    for _ in range(num_vertices - 1):
        for i in range(num_vertices):
            if graph[start][i] > 0 and not found[i]:
                distances[i] = min(
                    distances[i], distances[start] + graph[start][i])

        min_distance = float('inf')
        next_vertex = -1
        for i in range(num_vertices):
            if not found[i] and distances[i] < min_distance:
                min_distance = distances[i]
                next_vertex = i

        if next_vertex == -1:
            break

        found[next_vertex] = 1
        start = next_vertex

        steps.append((start, list(found), list(distances)))

    return steps


graph = np.array([
    [0, 50, 45, 10, 0, 0],
    [0, 0, 10, 15, 0, 0],
    [0, 0, 0, 0, 30, 0],
    [20, 0, 0, 0, 15, 0],
    [0, 20, 35, 0, 0, 0],
    [0, 0, 0, 0, 3, 0]
])


steps = dijkstra(graph, 0)

for i, (selected, found, distances) in enumerate(steps):
    print(f"단계 {
          i + 1}: 선택된 정점 = {selected}, Found = {found}, Distances = {distances}")
