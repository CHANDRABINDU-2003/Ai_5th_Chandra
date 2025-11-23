import random


class NQueens:
    def __init__(self, n, initial_state, goal_state):
        self.n = n
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.current_state = initial_state
        self.steps = []

    def print_board(self, state):
        for row in state:
            print(" ".join(str(cell) for cell in row))
        print()

    def is_goal_state(self, state):
        return state == self.goal_state

    def heuristic(self, state):
        # Calculate the number of pairs of queens that are attacking each other
        conflicts = 0
        for row in range(self.n):
            for col in range(self.n):
                if state[row][col] == 1:
                    # Check for other queens in the same row, column, and diagonals
                    for i in range(row + 1, self.n):
                        if state[i][col] == 1:  # Column conflict
                            conflicts += 1
                        if col + (i - row) < self.n and state[i][col + (i - row)] == 1:  # Right diagonal conflict
                            conflicts += 1
                        if col - (i - row) >= 0 and state[i][col - (i - row)] == 1:  # Left diagonal conflict
                            conflicts += 1
        return conflicts

    def get_best_successor(self, state):
        best_state = state
        best_heuristic = self.heuristic(state)

        for row in range(self.n):
            for col in range(self.n):
                if state[row][col] == 1:
                    # Try moving this queen to each column in the same row
                    for new_col in range(self.n):
                        if new_col != col:
                            new_state = [list(row) for row in state]
                            new_state[row][col] = 0
                            new_state[row][new_col] = 1
                            new_heuristic = self.heuristic(new_state)
                            if new_heuristic < best_heuristic:
                                best_state = new_state
                                best_heuristic = new_heuristic
                                self.steps.append((row, col, new_col))  # Log the move
        return best_state

    def hill_climbing(self):
        print("Initial State:")
        self.print_board(self.current_state)

        while not self.is_goal_state(self.current_state):
            next_state = self.get_best_successor(self.current_state)
            if self.heuristic(next_state) >= self.heuristic(self.current_state):
                # No improvement found; we're stuck in a local minimum
                break
            self.current_state = next_state
            print("Current State with heuristic =", self.heuristic(self.current_state))
            self.print_board(self.current_state)

        if self.is_goal_state(self.current_state):
            print("Goal State reached!")
            self.print_board(self.current_state)
            return True
        else:
            print("Stuck in local minimum, unable to reach goal state.")
            return False


# Example Usage
n = 4
initial_state = [
    [1, 1, 0, 0],  # Row 0
    [0, 1, 0, 1],  # Row 1
    [1, 0, 0, 0],  # Row 2
    [0, 0, 1, 0]  # Row 3
]

goal_state = [
    [1, 0, 0, 0],  # Row 0
    [0, 0, 1, 0],  # Row 1
    [0, 0, 0, 1],  # Row 2
    [0, 1, 0, 0]  # Row 3
]

n_queens = NQueens(n, initial_state, goal_state)
n_queens.hill_climbing()
