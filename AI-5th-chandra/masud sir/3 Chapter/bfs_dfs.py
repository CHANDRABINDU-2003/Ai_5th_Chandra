import time
from collections import deque

# Updated Graph Representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B', 'F'],
    'E': ['B', 'G', 'H'],
    'F': ['D'],
    'G': ['E', 'I', 'J'],
    'H': ['E', 'K'],
    'I': ['G', 'L'],
    'J': ['G', 'L'],
    'K': ['H'],
    'L': ['I', 'J']
}


# Breadth-First Search with time measurement
def bfs(graph, start):
    start_time = time.time()  # Start timer
    visited = set()
    queue = deque([start])
    traversal_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    end_time = time.time()  # End timer
    print("BFS Traversal Order:", traversal_order)
    print(f"BFS Time: {end_time - start_time:.100f} seconds")
    return traversal_order


# Depth-First Search with time measurement
def dfs(graph, start):
    start_time = time.time()  # Start timer
    visited = set()
    stack = [start]
    traversal_order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            stack.extend(reversed(graph[node]))  # Reverse to maintain order

    end_time = time.time()  # End timer
    print("DFS Traversal Order:", traversal_order)
    print(f"DFS Time: {end_time - start_time:.100f} seconds")
    return traversal_order


# Testing BFS and DFS
bfs(graph, 'A')
dfs(graph, 'A')