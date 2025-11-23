from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return True

    # Initialize the frontiers for both directions
    front_start = deque([start])
    front_goal = deque([goal])

    # Initialize the visited sets for both directions
    visited_start = {start}
    visited_goal = {goal}

    while front_start and front_goal:
        # Expand from the start side
        if front_start:
            node = front_start.popleft()
            for neighbor in graph[node]:
                if neighbor in visited_goal:
                    return True
                if neighbor not in visited_start:
                    visited_start.add(neighbor)
                    front_start.append(neighbor)

        # Expand from the goal side
        if front_goal:
            node = front_goal.popleft()
            for neighbor in graph[node]:
                if neighbor in visited_start:
                    return True
                if neighbor not in visited_goal:
                    visited_goal.add(neighbor)
                    front_goal.append(neighbor)

    return False

# Main function
if __name__ == '__main__':
    # Create the graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # Define start and goal nodes
    start_node = 'A'
    goal_node = 'F'

    # Perform Bidirectional Search
    found = bidirectional_search(graph, start_node, goal_node)
    if found:
        print(f"Path found between '{start_node}' and '{goal_node}'.")
    else:
        print(f"No path found between '{start_node}' and '{goal_node}'.")
