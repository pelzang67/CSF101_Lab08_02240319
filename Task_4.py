# Task 4: Depth-First Search (DFS) Traversal

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        # Recursively visit all neighbors
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Perform DFS starting from 'A'
print("DFS Traversal starting from A:")
dfs(graph, 'A')
