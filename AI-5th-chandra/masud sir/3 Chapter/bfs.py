from collections import deque

graph = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'd': ['f'],
    'e': ['h', 'g'],
    'h': ['k'],
    'g': ['i', 'j'],
    'i': ['l'],
    'j': ['l'],
    'c': [],
    'f': [],
    'k': [],
    'l': [],
}

def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    return None

start_node = 'a'
goal_node = 'l'

path = bfs_path(graph, start_node, goal_node)

if path:
    print(f"Path found from '{start_node}' to '{goal_node}': {' -> '.join(path)}")
else:
    print(f"No path found from '{start_node}' to '{goal_node}'.")
