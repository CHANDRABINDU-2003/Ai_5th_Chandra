import numpy as np
import random

def find_neighbours(state, landscape):
    neighbours = []
    dim = landscape.shape
    if state[0] != 0:
        neighbours.append((state[0] - 1, state[1]))
    if state[0] != dim[0] - 1:
        neighbours.append((state[0] + 1, state[1]))
    if state[1] != 0:
        neighbours.append((state[0], state[1] - 1))
    if state[1] != dim[1] - 1:
        neighbours.append((state[0], state[1] + 1))
    if state[0] != 0 and state[1] != 0:
        neighbours.append((state[0] - 1, state[1] - 1))
    if state[0] != 0 and state[1] != dim[1] - 1:
        neighbours.append((state[0] - 1, state[1] + 1))
    if state[0] != dim[0] - 1 and state[1] != 0:
        neighbours.append((state[0] + 1, state[1] - 1))
    if state[0] != dim[0] - 1 and state[1] != dim[1] - 1:
        neighbours.append((state[0] + 1, state[1] + 1))
    return neighbours

def stochastic_hill_climb(curr_state, landscape):
    neighbours = find_neighbours(curr_state, landscape)
    better_neighbours = [n for n in neighbours if landscape[n[0]][n[1]] > landscape[curr_state[0]][curr_state[1]]]
    if not better_neighbours:
        return False, curr_state
    next_state = random.choice(better_neighbours)
    return True, next_state

def __main__():
    landscape = np.random.randint(1, high=50, size=(10, 10))
    print(landscape)
    start_state = (3, 6)
    current_state = start_state
    count = 1
    ascending = True
    while ascending:
        print("\nStep #", count)
        print("Current state coordinates: ", current_state)
        print("Current state value: ", landscape[current_state[0]][current_state[1]])
        count += 1
        ascending, current_state = stochastic_hill_climb(current_state, landscape)

    print("\nStep #", count)
    print("Optimization objective reached.")
    print("Final state coordinates: ", current_state)
    print("Final state value: ", landscape[current_state[0]][current_state[1]])

__main__()
