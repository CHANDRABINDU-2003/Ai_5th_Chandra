# A class to represent the map coloring CSP problem
class MapColoring:
    def __init__(self, graph, colors):
        self.graph = graph  # adjacency list representation of the graph (map)
        self.colors = colors  # list of available colors
        self.assignment = {}  # dictionary to hold the color assigned to each region

    # Function to check if it's safe to assign a color to a node
    def is_safe(self, node, color):
        # Check all adjacent nodes
        for neighbor in self.graph[node]:
            if neighbor in self.assignment and self.assignment[neighbor] == color:
                return False  # The color is already assigned to a neighbor
        return True

    # Backtracking function to solve the map coloring problem
    def solve(self, nodes):
        # If all nodes are assigned a color, we're done
        if len(self.assignment) == len(nodes):
            return True

        # Try each node that hasn't been assigned a color
        for node in nodes:
            if node not in self.assignment:
                # Try each color
                for color in self.colors:
                    if self.is_safe(node, color):
                        self.assignment[node] = color

                        # Recurse to assign colors to the next node
                        if self.solve(nodes):
                            return True

                        # If the color assignment didn't work, backtrack
                        del self.assignment[node]

        # If no solution is found
        return False

    # Function to get the result (solution) of the map coloring
    def get_coloring(self):
        nodes = list(self.graph.keys())
        if self.solve(nodes):
            return self.assignment
        else:
            return None


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

# Create the map coloring instance
map_coloring = MapColoring(graph, colors)

# Get the solution
solution = map_coloring.get_coloring()

if solution:
    print("Solution found: ")
    for node, color in solution.items():
        print(f"Region {node} is colored {color}")
else:
    print("No solution exists")
