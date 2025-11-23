from collections import deque
import time
count=0
def bidirectional_search(graph, start, goal):
    global count
    count += 1
    if start == goal:
        return [start]

    front_start = {start: None}
    front_goal = {goal: None}
    queue_start = deque([start])
    queue_goal = deque([goal])

    while queue_start and queue_goal:
        # Forward
        node = queue_start.popleft()
        for neighbor in graph[node]:
            if neighbor not in front_start:
                front_start[neighbor] = node
                queue_start.append(neighbor)
                if neighbor in front_goal:
                    return construct_path(front_start, front_goal, neighbor)

        # Backward
        node = queue_goal.popleft()
        for neighbor in graph[node]:
            if neighbor not in front_goal:
                front_goal[neighbor] = node
                queue_goal.append(neighbor)
                if neighbor in front_start:
                    return construct_path(front_start, front_goal, neighbor)
    return None

def construct_path(front_start, front_goal, meet):
    path1, path2 = [], []
    node = meet
    while node:
        path1.append(node)
        node = front_start[node]
    node = front_goal[meet]
    while node:
        path2.append(node)
        node = front_goal[node]
    return list(reversed(path1)) + path2


# ---------- INPUT ----------
graph = {}
n = int(input("Enter number of nodes: "))
print("Enter node names:")
nodes = input().split()
for node in nodes:
    graph[node] = []

e = int(input("Enter number of edges: "))
print("Enter each edge (u v):")
for _ in range(e):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)

start = input("Enter start node: ")
goal = input("Enter goal node: ")

# ---------- EXECUTION ----------
t1 = time.time()
path = bidirectional_search(graph, start, goal)
t2 = time.time()

if path:
    print(f"\n Bidirectional Path: {' -> '.join(path)}")
else:
    print("\n No path found!")

print(f"⏱ Execution Time: {t2 - t1:.6f} seconds")
print("🧮 Time Complexity: O(b^(d/2))")
print("📦 Space Complexity: O(b^(d/2))")
print(f"🔍 Nodes Explored: {count}")
