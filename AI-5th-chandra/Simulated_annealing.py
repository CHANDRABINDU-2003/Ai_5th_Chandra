import random
import math


def calculate_conflicts(state):
    """
    Calculates the number of conflicts in the current state.
    A conflict occurs if two queens are in the same row, column, or diagonal.
    """
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts


def generate_neighbor(state):
    """
    Generates a neighbor by randomly moving one queen to a different row in its column.
    """
    n = len(state)
    new_state = state[:]
    col = random.randint(0, n - 1)
    new_row = random.choice([i for i in range(n) if i != new_state[col]])
    new_state[col] = new_row
    return new_state


def simulated_annealing(initial_state, max_steps=10000, initial_temp=100, cooling_rate=0.99):
    """
    Solves the N-Queens problem using simulated annealing.
    - initial_state: The initial state of the board (a list where index represents column and value represents row)
    - max_steps: Maximum number of iterations before the algorithm stops
    - initial_temp: Starting temperature for simulated annealing
    - cooling_rate: Rate at which temperature decreases in each step
    """
    current_state = initial_state
    current_conflicts = calculate_conflicts(current_state)
    temperature = initial_temp

    for step in range(max_steps):
        if current_conflicts == 0:  # Goal state reached
            return current_state, step

        # Generate a neighbor state
        neighbor = generate_neighbor(current_state)
        neighbor_conflicts = calculate_conflicts(neighbor)

        # Calculate change in conflicts
        delta = neighbor_conflicts - current_conflicts

        # Decide to move to the neighbor based on the probability
        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / temperature):
            current_state = neighbor
            current_conflicts = neighbor_conflicts

        # Decrease temperature
        temperature *= cooling_rate

    return current_state, max_steps  # Return the last state if goal is not reached


# Define the problem parameters
n = 8  # Number of queens
initial_state = [0, 2, 4, 6, 1, 3, 5, 7]  # Define a specific starting state
final_state, steps = simulated_annealing(initial_state)

print("Final State:", final_state)
print("Conflicts in Final State:", calculate_conflicts(final_state))
print("Steps Taken:", steps)
