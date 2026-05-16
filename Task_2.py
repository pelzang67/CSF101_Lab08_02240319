# Task 2: Add Vertex and Edge

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Ensure both vertices exist before adding the edge
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

# Create graph
g = Graph()

# Sample Operations
# Add vertices: A, B, C, D
for v in ['A', 'B', 'C', 'D']:
    g.add_vertex(v)

# Add edges: A-B, A-C, B-D
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')

# Display graph
print("Graph Representation:")
g.display()
