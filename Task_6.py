# Task 6: Shortest Path Using BFS

from collections import deque

def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])  # store paths instead of just nodes

    while queue:
        path = queue.popleft()
        vertex = path[-1]

        if vertex == goal:
            return path

        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Find shortest path from A to F
shortest_path = bfs_shortest_path(graph, 'A', 'F')

# Display result
if shortest_path:
    print("Shortest path from A to F:")
    print(" -> ".join(shortest_path))
else:
    print("No path found from A to F")
