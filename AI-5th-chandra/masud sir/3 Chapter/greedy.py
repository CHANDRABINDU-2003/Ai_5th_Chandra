graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2), ('E', 4)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
heuristic = {
    'A': 5,
    'B': 2,
    'C': 4,
    'D': 6,
    'E': 3,
    'F': 0
}
import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    # Priority queue to store (heuristic, node) tuples
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))
    
    # Set to keep track of visited nodes
    visited = set()
    
    while priority_queue:
        # Get the node with the lowest heuristic value
        current_heuristic, current_node = heapq.heappop(priority_queue)
        
        # If we reach the goal, return the path
        if current_node == goal:
            print(f"Goal {goal} found!")
            return
        
        # Mark the current node as visited
        visited.add(current_node)
        
        # Explore neighbors
        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
                print(f"Exploring node {neighbor} with heuristic {heuristic[neighbor]}")
    
    print("Goal not found!")

# Example usage
start_node = 'A'
goal_node = 'F'
greedy_best_first_search(graph, start_node, goal_node, heuristic)
