from collections import deque
import time
count=0
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        global count
        count += 1
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None


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
path = bfs(graph, start, goal)
t2 = time.time()

if path:
    print(f"\n✅ BFS Path: {' -> '.join(path)}")
else:
    print("\n❌ No path found!")

print(f"⏱ Execution Time: {t2 - t1:.6f} seconds")
print("🧮 Time Complexity: O(V + E)")
print("📦 Space Complexity: O(V)")
print(f"🔍 Nodes Explored: {count}")
