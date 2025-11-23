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

def dfs_path(graph, start, goal, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    visited.add(start)
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, path + [neighbor], visited)
            if new_path:
                return new_path
    return None

start_node = 'a'
goal_node = 'l'

path = dfs_path(graph, start_node, goal_node)

if path:
    print(f"Path found from '{start_node}' to '{goal_node}': {' -> '.join(path)}")
else:
    print(f"No path found from '{start_node}' to '{goal_node}'.")
