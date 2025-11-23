import time
from collections import deque

# Graph represented as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2],
}


# BFS algorithm
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


# DFS algorithm
def dfs(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)

            # Add neighbors to the stack
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order


# Function to measure the running time of an algorithm
def measure_time(algorithm, graph, start):
    start_time = time.time()
    result = algorithm(graph, start)
    end_time = time.time()

    elapsed_time = end_time - start_time
    return result, elapsed_time


# Test BFS and DFS
start_node = 0
bfs_result, bfs_time = measure_time(bfs, graph, start_node)
dfs_result, dfs_time = measure_time(dfs, graph, start_node)

# Output results and their running times
print(f"BFS Result: {bfs_result}")
print(f"BFS Running Time: {bfs_time:.6f} seconds")

print(f"DFS Result: {dfs_result}")
print(f"DFS Running Time: {dfs_time:.6f} seconds")
