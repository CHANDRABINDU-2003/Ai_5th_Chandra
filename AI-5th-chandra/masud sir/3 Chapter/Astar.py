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

def a_star_search(graph, start, goal, heuristic):
    # Priority queue to store (total_cost, current_cost, current_node, path)
    queue = [(heuristic[start], 0, start, [start])]
    heapq.heapify(queue)
    visited = set()
    
    while queue:
        total_cost, current_cost, current_node, path = heapq.heappop(queue)
        
        if current_node in visited:
            continue
        
        if current_node == goal:
            print(f"Path found: {path} with total cost: {current_cost}")
            return path
        
        visited.add(current_node)
        
        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                new_cost = current_cost + cost
                heapq.heappush(queue, (new_cost + heuristic[neighbor], new_cost, neighbor, path + [neighbor]))
                print(f"Exploring node {neighbor} with path: {path + [neighbor]} and total cost: {new_cost + heuristic[neighbor]}")
    
    print("Goal not found")
    return None

# Example usage
start_node = 'A'
goal_node = 'F'
a_star_search(graph, start_node, goal_node, heuristic)

