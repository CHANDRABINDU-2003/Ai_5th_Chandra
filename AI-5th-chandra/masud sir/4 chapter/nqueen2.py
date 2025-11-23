import numpy as np
import random


initial_state = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0]
])

goal_state = np.array([
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0]
])


def calculate_conflicts(board):
    conflicts = 0
    n = board.shape[0]
    positions = np.argwhere(board == 1)

    for i, (x1, y1) in enumerate(positions):
        for x2, y2 in positions[i+1:]:
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                conflicts += 1
    return conflicts


def random_initial_state():
    board = np.zeros((8, 8), dtype=int)
    for row in range(8):
        col = random.randint(0, 7)
        board[row, col] = 1
    return board


def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()


def hill_climbing_with_random_restart(initial_state, max_restarts=100):
    for restart in range(max_restarts):
        current_state = initial_state if restart == 0 else random_initial_state()
        current_conflicts = calculate_conflicts(current_state)
        steps = [current_state.copy()]
        print(f"Starting Restart {restart + 1}")

        while current_conflicts > 0:
            best_move = None
            lowest_conflicts = current_conflicts

            # Explore each queen's position in each row
            for row in range(8):
                for col in range(8):
                    if current_state[row, col] == 1:
                        continue

                    # Move queen to new position
                    temp_state = current_state.copy()
                    temp_state[row] = 0
                    temp_state[row, col] = 1

                    # Calculate conflicts in the new state
                    new_conflicts = calculate_conflicts(temp_state)
                    if new_conflicts < lowest_conflicts:
                        best_move = (row, col)
                        lowest_conflicts = new_conflicts

            # If a better move is found, make it
            if best_move:
                row, col = best_move
                current_state[row] = 0
                current_state[row, col] = 1
                current_conflicts = lowest_conflicts
                steps.append(current_state.copy())

                # Print the new state
                print(f"Step {len(steps) - 1}:")
                print_board(current_state)
            else:
                break  # No improvement possible, exit the loop

        if current_conflicts == 0:
            print(f"Solution found after {restart + 1} restart(s)!")
            return steps, True

    return steps, False  # Return the last steps if solution not found

# Solve the 8-Queens problem from initial state with random restarts
steps, success = hill_climbing_with_random_restart(initial_state)
print(goal_state)
# Display solution steps
if success:
    print("Solution found!")
else:
    print("Failed to reach goal state.")