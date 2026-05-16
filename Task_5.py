# Task 5: Compare BFS and DFS Traversal

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return order

def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    if start not in visited:
        order.append(start)
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited, order)
    return order

# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Run BFS and DFS
bfs_result = bfs(graph, 'A')
dfs_result = dfs(graph, 'A')

# Display results
print("BFS Traversal starting from A:", " ".join(bfs_result))
print("DFS Traversal starting from A:", " ".join(dfs_result))

# Comparison Table
print("\nComparison Table:")
print("| Algorithm | Data Structure Used | Traversal Order | Suitable For |")
print("|-----------|---------------------|-----------------|--------------|")
print(f"| BFS       | Queue               | {' '.join(bfs_result)} | Shortest path in unweighted graph |")
print(f"| DFS       | Stack / Recursion   | {' '.join(dfs_result)} | Exploring deep paths |")
