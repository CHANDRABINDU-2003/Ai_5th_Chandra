import numpy as np
import copy
import random

# Define goal state for 3x3 puzzle
goal_state = np.array([[1,2,3],
                       [4,5,6],
                       [7,8,0]])

def heuristic(state):
    """Number of misplaced tiles"""
    return np.sum(state != goal_state) - 1 if state[2,2] == 0 else np.sum(state != goal_state)

def find_neighbours(state):
    """Return all possible states after moving blank (0)"""
    neighbours = []
    blank_pos = tuple(np.argwhere(state == 0)[0])
    x, y = blank_pos
    moves = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x, y], new_state[nx, ny] = new_state[nx, ny], new_state[x, y]
            neighbours.append(new_state)
    return neighbours

def hill_climb(state):
    """Perform one hill climbing step"""
    neighbours = find_neighbours(state)
    current_h = heuristic(state)
    best_state = state
    for neighbour in neighbours:
        h = heuristic(neighbour)
        if h < current_h:  # minimize misplaced tiles
            current_h = h
            best_state = neighbour
    if np.array_equal(best_state, state):
        return False, state  # no improvement
    return True, best_state

def __main__():
    # Random initial puzzle (scrambled)
    puzzle = goal_state.copy()
    np.random.shuffle(puzzle.flat)
    print("Initial Puzzle:\n", puzzle)

    current_state = puzzle
    steps = 0
    while True:
        improved, current_state = hill_climb(current_state)
        steps += 1
        print(f"\nStep #{steps}:\n{current_state}")
        if not improved or heuristic(current_state) == 0:
            break

    print("\nReached final state:")
    print(current_state)
    if heuristic(current_state) == 0:
        print("Goal state reached!")
    else:
        print("Local maximum (stuck).")

__main__()
