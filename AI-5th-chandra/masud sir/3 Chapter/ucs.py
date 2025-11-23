def uniform_cost_search(goal, start):
    global graph, cost
    answer = [float('inf')] * len(goal)  # Initialize answer list with infinity
    queue = [(0, start)]  # Priority queue with (cost, node)
    visited = {}  # Dictionary to track visited nodes
    count = 0  # Count of goal nodes reached

    while queue:
        # Sort the queue to get the node with the smallest cost
        queue.sort()
        current_cost, current_node = queue.pop(0)  # Get the node with the smallest cost

        if current_node in goal:
            index = goal.index(current_node)
            if answer[index] == float('inf'):
                count += 1
            if answer[index] > current_cost:
                answer[index] = current_cost
            if count == len(goal):
                return answer

        if current_node not in visited:
            visited[current_node] = True
            for neighbor in graph[current_node]:
                total_cost = current_cost + cost[(current_node, neighbor)]
                queue.append((total_cost, neighbor))

    return answer

# Main function
if __name__ == '__main__':
    # Create the graph
    graph = [[] for _ in range(8)]
    cost = {}

    # Add edges
    graph[0].append(1)
    graph[0].append(3)
    graph[3].append(1)
    graph[3].append(6)
    graph[3].append(4)
    graph[1].append(6)
    graph[4].append(2)
    graph[4].append(5)
    graph[2].append(1)
    graph[5].append(2)
    graph[5].append(6)
    graph[6].append(4)

    # Add the cost
    cost[(0, 1)] = 2
    cost[(0, 3)] = 5
    cost[(1, 6)] = 10
    cost[(3, 1)] = 5
    cost[(3, 6)] = 6
    cost[(3, 4)] = 2
    cost[(2, 1)] = 4
    cost[(4, 2)] = 4
    cost[(4, 5)] = 3
    cost[(5, 2)] = 6
    cost[(5, 6)] = 3
    cost[(6, 4)] = 7

    # Goal states
    goal = [6]  # There can be multiple goal states

    # Get the answer
    answer = uniform_cost_search(goal, 0)

    # Print the answer
    print("Minimum cost from Start to Goal is =", answer[0])
