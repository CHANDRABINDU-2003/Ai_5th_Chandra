import random, copy, time

GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 is the empty tile

def find_pos(state, value):
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return i, j

def misplaced_tiles(state):
    """Heuristic: number of misplaced tiles"""
    return sum(state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]
               for i in range(3) for j in range(3))

def get_neighbors(state):
    """Generate all valid neighbor states"""
    i, j = find_pos(state, 0)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    neighbors = []
    for di, dj in moves:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append(new_state)
    return neighbors

def hill_climbing(start_state, max_steps=1000):
    current = start_state
    current_h = misplaced_tiles(current)
    
    for step in range(max_steps):
        neighbors = get_neighbors(current)
        next_state = min(neighbors, key=misplaced_tiles)
        next_h = misplaced_tiles(next_state)
        if next_h >= current_h:
            break
        current, current_h = next_state, next_h
    
    return current, current_h, step+1

# -------- INPUT ----------
print("Enter initial 3x3 board configuration (use 0 for empty):")
start_state = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(3)]

t1 = time.time()
final_state, h_value, steps = hill_climbing(start_state)
t2 = time.time()

print("\nFinal State after Hill Climbing:")
for row in final_state:
    print(row)
print(f"Heuristic Value = {h_value}")
print(f"Steps Taken = {steps}")
print(f"⏱ Execution Time: {t2 - t1:.6f}s")
print("🧮 Time Complexity: O(b^d) (branching factor & depth limited)")
print("📦 Space Complexity: O(b)")
