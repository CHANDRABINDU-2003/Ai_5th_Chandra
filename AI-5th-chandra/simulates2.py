import random
import math


class NQueensSimulatedAnnealing:
    def __init__(self, n, initial_state, goal_state):
        self.n = n  # Number of queens
        self.state = initial_state  # Initial state with potentially multiple queens per row
        self.goal_state = goal_state  # Goal state

    def get_conflicts(self, state):
        """Calculate the number of conflicts in the given state."""
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def get_random_neighbor(self):
        """Generate a random neighbor by moving a queen to a different row."""
        neighbor = self.state[:]
        col = random.randint(0, self.n - 1)
        new_row = random.randint(0, self.n - 1)
        neighbor[col] = new_row
        return neighbor

    def simulated_annealing(self, initial_temp, cooling_rate):
        """Perform the simulated annealing algorithm."""
        temperature = initial_temp
        current_state = self.state
        current_conflicts = self.get_conflicts(current_state)

        while temperature > 0.01:
            if current_state == self.goal_state:
                print("Reached the goal state!")
                return current_state

            # Generate a neighbor and calculate its conflicts
            neighbor = self.get_random_neighbor()
            neighbor_conflicts = self.get_conflicts(neighbor)

            # Calculate energy difference
            delta_conflicts = neighbor_conflicts - current_conflicts

            # Decide to move to neighbor based on probability
            if delta_conflicts < 0 or random.uniform(0, 1) < math.exp(-delta_conflicts / temperature):
                current_state = neighbor
                current_conflicts = neighbor_conflicts

            # Cool down
            temperature *= cooling_rate

        print("Did not reach the exact goal state but found a solution close to it.")
        return current_state


# Example usage:
n = 8  # Number of queens
initial_state = [0, 1, 2, 3, 4, 5, 6, 7]  # Initial state (can have more than one queen in a row)
goal_state = [0, 1, 2, 3, 5, 5, 6, 7]  # Goal state we want to reach

solver = NQueensSimulatedAnnealing(n, initial_state, goal_state)
solution = solver.simulated_annealing(initial_temp=100, cooling_rate=0.99)

print("Solution:", solution)
