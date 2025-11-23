def depth_limited_search(graph, start, goal, limit):
    def dls(node, depth):
        if depth > limit:
            return False
        if node == goal:
            return True
        for neighbor in graph[node]:
            if dls(neighbor, depth + 1):
                return True
        return False

    return dls(start, 0)

# Main function
if __name__ == '__main__':
    # Create the graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # Define start, goal, and depth limit
    start_node = 'A'
    goal_node = 'F'
    depth_limit = 1


    # Perform Depth-Limited Search
    found = depth_limited_search(graph, start_node, goal_node, depth_limit)
    if found:
        print(f"Goal node '{goal_node}' found within depth limit of {depth_limit}.")
    else:
        print(f"Goal node '{goal_node}' not found within depth limit of {depth_limit}.")
