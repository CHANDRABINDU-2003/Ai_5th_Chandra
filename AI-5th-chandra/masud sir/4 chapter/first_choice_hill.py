import numpy as np

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

def first_choice_hill_climb(curr_state, landscape):
    neighbours = find_neighbours(curr_state, landscape)
    for neighbour in neighbours:
        if landscape[neighbour[0]][neighbour[1]] > landscape[curr_state[0]][curr_state[1]]:
            return True, neighbour
    return False, curr_state

def __main__():
    landscape = np.random.randint(1, high=50, size=(10, 10))
    print("Landscape:\n", landscape)
    global_max_value = np.max(landscape)
    global_max_coords = list(zip(*np.where(landscape == global_max_value)))

    start_state = (3, 6)
    current_state = start_state
    count = 1
    ascending = True
    while ascending:
        print("\nStep #", count)
        print("Current state coordinates:", current_state)
        print("Current state value:", landscape[current_state[0]][current_state[1]])
        count += 1
        ascending, current_state = first_choice_hill_climb(current_state, landscape)

    print("\nStep #", count)
    print("Optimization objective reached.")
    print("Final state coordinates:", current_state)
    print("Final state value:", landscape[current_state[0]][current_state[1]])
    
    if landscape[current_state[0]][current_state[1]] == global_max_value:
        print("This is the GLOBAL MAXIMUM!")
    else:
        print("This is a LOCAL MAXIMUM.")
    
    print("Global maximum value in the landscape:", global_max_value)
    print("Coordinates of global maximum:", global_max_coords)

__main__()
