# Luis Garcia
# CSC 2720 Lab 12
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Apr 7, 2024

class Graph:
    def __init__(self, V):
        self.V = V  # number of vertices
        self.adj = {}  # adjacent lists
        # Initialize adjacency lists for all vertices
        for i in range(V):
            self.adj[i] = []

    def add_edge(self, v, w):
        # Ensure v is in the dictionary
        if v not in self.adj:
            self.adj[v] = []
        # Add w to the adjacency list of v
        self.adj[v].append(w)


def dfs_recursive(graph, v, visited, traversal):
    # Mark the current vertex as visited
    visited[v] = True
    # Append the current vertex to the traversal
    traversal.append(v)
    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph.adj[v]:
        if not visited[neighbor]:
            dfs_recursive(graph, neighbor, visited, traversal)


def dfs_traversal_recursive(graph):
    # Initialize visited array
    visited = [False] * graph.V
    traversal = []  # to store the DFS traversal

    # Call the recursive helper function to perform DFS traversal
    dfs_recursive(graph, 0, visited, traversal)

    return traversal


# Example usage:
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 3)
g.add_edge(3, 5)

# Perform DFS traversal starting from vertex 0
dfs_order = dfs_traversal_recursive(g)
print("DFS Traversal (Recursive):", dfs_order)

# Test cases
assert dfs_order == [0, 1, 3, 5, 2, 4], "Test case 1 failed"  

# Test case 2: Graph with only one vertex
g2 = Graph(1)
dfs_order_2 = dfs_traversal_recursive(g2)
print("DFS Traversal (Recursive) - Test case 2:", dfs_order_2)
assert dfs_order_2 == [0], "Test case 2 failed"  