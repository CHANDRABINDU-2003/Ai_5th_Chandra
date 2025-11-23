def iterative_deepening_dfs(graph, start, goal):
    def dls(node, depth, limit):
        if depth > limit:
            return False
        if node == goal:
            return True
        for neighbor in graph[node]:
            if dls(neighbor, depth + 1, limit):
                return True
        return False

    depth = 0
    while True:
        print(f"Iteration (Depth Limit): {depth}")
        if dls(start, 0, depth):
            print(f"Goal found at depth {depth}")
            return True
        depth += 1

# Main function
if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    start_node = 'A'
    goal_node = 'F'

    found = iterative_deepening_dfs(graph, start_node, goal_node)
    if found:
        print(f"Goal node '{goal_node}' found successfully.")
    else:
        print(f"Goal node '{goal_node}' not found.")
