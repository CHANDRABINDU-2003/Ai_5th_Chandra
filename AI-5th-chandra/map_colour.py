# Define the map as a graph using an adjacency list representation
# Example: Four regions: A, B, C, D with adjacencies
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}


# Function to check if the current coloring is valid
def is_valid(assignment, graph, node, color):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


# Backtracking function to solve the map coloring problem
def map_coloring(graph, colors, assignment, nodes):
    # If all nodes are assigned a color, return True (solution found)
    if len(assignment) == len(nodes):
        return True

    # Select the next node to color
    node = next(node for node in nodes if node not in assignment)

    # Try every color for this node
    for color in colors:
        # Check if the color assignment is valid
        if is_valid(assignment, graph, node, color):
            assignment[node] = color

            # Recur to assign colors to the next node
            if map_coloring(graph, colors, assignment, nodes):
                return True

            # Backtrack if no valid coloring is found
            del assignment[node]

    return False


# Function to solve the Map Coloring problem
def solve_map_coloring(graph, num_colors):
    nodes = list(graph.keys())  # List of nodes (regions)
    colors = [f'Color{i + 1}' for i in range(num_colors)]  # List of available colors
    assignment = {}  # To store the color assigned to each node

    # Start backtracking to find a valid coloring
    if map_coloring(graph, colors, assignment, nodes):
        return assignment
    else:
        return None


# Example usage
num_colors = 3  # Number of colors available
solution = solve_map_coloring(graph, num_colors)

if solution:
    print("Solution found:", solution)
else:
    print("No solution exists with the given number of colors.")
