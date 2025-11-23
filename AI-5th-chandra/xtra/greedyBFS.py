import heapq, time

def greedy_best_first_search(graph, start, goal, heuristic):
    pq = [(heuristic[start], [start])]
    visited = set()

    while pq:
        _, path = heapq.heappop(pq)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (heuristic[neighbor], path + [neighbor]))
    return None


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
path = greedy_best_first_search(graph, start, goal, heuristic)
t2 = time.time()

if path:
    print(f"\n✅ Greedy Best-First Path: {' -> '.join(path)}")
else:
    print("\n❌ No path found!")

print(f"⏱ Execution Time: {t2 - t1:.6f} seconds")
print("🧮 Time Complexity: O(E log V)")
print("📦 Space Complexity: O(V)")
print(f"🔍 Nodes Explored: {len(path) if path else 0}")