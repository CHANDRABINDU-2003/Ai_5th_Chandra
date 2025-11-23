import heapq, time

def a_star_search(graph, start, goal, heuristic):
    pq = [(heuristic[start], 0, [start])]  # (f = g+h, g, path)
    visited = {}

    while pq:
        f, g, path = heapq.heappop(pq)
        node = path[-1]

        if node == goal:
            return path, g

        if node not in visited or g < visited[node]:
            visited[node] = g
            for neighbor, cost in graph[node]:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(pq, (new_f, new_g, path + [neighbor]))
    return None, float('inf')


# ---------- INPUT ----------
graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))
print("Enter node names:")
nodes = input().split()

# Initialize adjacency list
for node in nodes:
    graph[node] = []

e = int(input("Enter number of weighted edges: "))
print("Enter each edge (u v w):")
for _ in range(e):
    u, v, w = input().split()
    w = int(w)
    graph[u].append((v, w))
    graph[v].append((u, w))

print("Enter heuristic (node h-value):")
for node in nodes:
    heuristic[node] = float(input(f"h({node}) = "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

# ---------- EXECUTION ----------
t1 = time.time()
path, cost = a_star_search(graph, start, goal, heuristic)
t2 = time.time()

if path:
    print(f"\n✅ A* Path: {' -> '.join(path)} | Total Cost = {cost}")
else:
    print("\n❌ No path found!")

print(f"⏱ Execution Time: {t2 - t1:.6f} seconds")
print("🧮 Time Complexity: O(E log V)")
print("📦 Space Complexity: O(V)")
print(f"🔍 Nodes Explored: {len(path) if path else 0}")