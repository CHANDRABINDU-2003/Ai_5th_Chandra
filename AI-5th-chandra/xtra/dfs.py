import time
count = 0
def dfs(graph, start, goal, path=None, visited=None):
    global count
    count += 1
    if path is None:
        path = []
    if visited is None:
        visited = set()
    path.append(start)
    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, path.copy(), visited)
            if new_path:
                return new_path
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
path = dfs(graph, start, goal)
t2 = time.time()

if path:
    print(f"\n✅ DFS Path: {' -> '.join(path)}")
else:
    print("\n❌ No path found!")

print(f"⏱ Execution Time: {t2 - t1:.6f} seconds")
print("🧮 Time Complexity: O(V + E)")
print("📦 Space Complexity: O(V)")
print(f"🔍 Nodes Explored: {count}")
