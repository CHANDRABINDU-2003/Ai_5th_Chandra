import time
from collections import deque


# BFS Algorithm Implementation
def bfs(graph, start):
    # Keep track of visited nodes to avoid revisiting
    visited = set()
    # Queue for BFS
    queue = deque([start])
    # List to store the traversal order
    traversal_order = []

    # Mark the starting node as visited
    visited.add(start)

    while queue:
        # Dequeue a node from the queue
        node = queue.popleft()
        # Add the node to the traversal order
        traversal_order.append(node)

        # Get all adjacent nodes (neighbors) of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                # If the neighbor is not visited, mark it visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Record the start time
start_time = time.time()

# Perform BFS starting from node 'A'
traversal = bfs(graph, 'A')

# Record the end time
end_time = time.time()

# Calculate the running time
execution_time = end_time - start_time

# Output the results
print("BFS Traversal Order:", traversal)
print("Execution Time: {:.6f} seconds".format(execution_time))
