import time
count=0
def dls(graph, start, goal, limit, visited=None, path=None):
    global count
    count += 1  
    if visited is None:
        visited = set()
    if path is None:
        path = []
    path.append(start)
    visited.add(start)

    if start == goal:
        return path
    if limit <= 0:
        return None

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dls(graph, neighbor, goal, limit - 1, visited.copy(), path.copy())
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
limit = int(input("Enter depth limit: "))

# ---------- EXECUTION ----------
t1 = time.time()
path = dls(graph, start, goal, limit)
t2 = time.time()

if path:
    print(f"\n✅ DLS Path: {' -> '.join(path)}")
else:
    print("\n❌ No path found within depth limit!")

print(f"⏱ Execution Time: {t2 - t1:.6f} seconds")
print("🧮 Time Complexity: O(b^l)")
print("📦 Space Complexity: O(l)")
print(f"🔍 Nodes Explored: {count}")
