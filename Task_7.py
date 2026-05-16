# Task 7: Graph Analysis

def analyze_graph(graph):
    # 1. Number of vertices
    num_vertices = len(graph)

    # 2. Number of edges (undirected, so divide by 2)
    num_edges = sum(len(neighbors) for neighbors in graph.values()) // 2

    # 3. Degree of each vertex
    degrees = {vertex: len(neighbors) for vertex, neighbors in graph.items()}

    # 4. Check if graph is connected using BFS
    from collections import deque
    visited = set()
    start = next(iter(graph))  # pick any starting vertex
    queue = deque([start])

    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.add(v)
            for neighbor in graph[v]:
                if neighbor not in visited:
                    queue.append(neighbor)

    is_connected = len(visited) == num_vertices

    # 5. Directed or undirected (based on symmetry of edges)
    is_undirected = all(
        vertex in graph and neighbor in graph and vertex in graph[neighbor]
        for vertex, neighbors in graph.items()
        for neighbor in neighbors
    )

    # Display results
    print("Number of vertices:", num_vertices)
    print("Number of edges:", num_edges)
    print("\nDegree of each vertex:")
    for v, d in degrees.items():
        print(f"{v}: {d}")
    print("\nThe graph is connected." if is_connected else "\nThe graph is not connected.")
    print("The graph is undirected." if is_undirected else "The graph is directed.")

# Define the graph (same as Task 3)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Run analysis
analyze_graph(graph)
