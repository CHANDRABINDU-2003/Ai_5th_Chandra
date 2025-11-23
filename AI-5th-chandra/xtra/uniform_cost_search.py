import heapq, time

def ucs(graph, start, goal):
    pq = [(0, [start])]
    visited = {}

    while pq:
        cost, path = heapq.heappop(pq)
        node = path[-1]

        if node == goal:
            return path, cost

        if node not in visited or cost < visited[node]:
            visited[node] = cost
            for neighbor, weight in graph[node]:
                heapq.heappush(pq, (cost + weight, path + [neighbor]))
    return None, float('inf')


# ---------- INPUT ----------
graph = {}
n = int(input("Enter number of nodes: "))
print("Enter node names:")
nodes = input().split()
for node in nodes:
    graph[node] = []

e = int(input("Enter number of weighted edges: "))
print("Enter each edge (u v w):")
for _ in range(e):
    u, v, w = input().split()
    w = int(w)
    graph[u].append((v, w))
    graph[v].append((u, w))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

# ---------- EXECUTION ----------
t1 = time.time()
path, cost = ucs(graph, start, goal)
t2 = time.time()

if path:
    print(f"\n✅ UCS Path: {' -> '.join(path)} | Cost = {cost}")
else:
    print("\n❌ No path found!")

print(f"⏱ Execution Time: {t2 - t1:.6f} seconds")
print("🧮 Time Complexity: O(E log V)")
print("📦 Space Complexity: O(V)")
print(f"🔍 Nodes Explored: {len(path) if path else 0}")