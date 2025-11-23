import random, time

def random_board(n):
    return [random.randint(0, n-1) for _ in range(n)]  # row position of queen in each column

def heuristic(board):
    """Number of attacking pairs"""
    n = len(board)
    attacks = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                attacks += 1
    return attacks

def get_neighbors(board):
    n = len(board)
    neighbors = []
    for col in range(n):
        for row in range(n):
            if row != board[col]:
                new_board = board.copy()
                new_board[col] = row
                neighbors.append(new_board)
    return neighbors

def hill_climbing_nqueen(n, max_steps=1000):
    current = random_board(n)
    current_h = heuristic(current)
    for step in range(max_steps):
        if current_h == 0:
            return current, step
        neighbors = get_neighbors(current)
        next_state = min(neighbors, key=heuristic)
        next_h = heuristic(next_state)
        if next_h >= current_h:
            break
        current, current_h = next_state, next_h
    return current, step

# ---------- INPUT ----------
n = int(input("Enter N for N-Queens: "))

t1 = time.time()
solution, steps = hill_climbing_nqueen(n)
t2 = time.time()

print(f"\nFinal Board (Column: Row): {solution}")
print(f"Heuristic Value: {heuristic(solution)}")
print(f"Steps Taken: {steps}")
print(f"⏱ Execution Time: {t2 - t1:.6f}s")
print("🧮 Time Complexity: O(N^2)")
print("📦 Space Complexity: O(N)")
