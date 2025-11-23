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
def fitness(board):
    n = len(board)
    max_pairs = n*(n-1)/2
    attacks = heuristic(board)
    return max_pairs - attacks

def select(population):
    return random.choices(population, weights=[fitness(ind) for ind in population], k=2)

def crossover(p1, p2):
    n = len(p1)
    point = random.randint(0, n-1)
    return p1[:point] + p2[point:]

def mutate(board, rate=0.1):
    n = len(board)
    if random.random() < rate:
        board[random.randint(0, n-1)] = random.randint(0, n-1)
    return board

def genetic_nqueen(n, population_size=100, generations=1000):
    population = [random_board(n) for _ in range(population_size)]
    for g in range(generations):
        population = sorted(population, key=heuristic)
        if heuristic(population[0]) == 0:
            return population[0], g
        new_pop = []
        for _ in range(population_size):
            p1, p2 = select(population)
            child = crossover(p1, p2)
            child = mutate(child)
            new_pop.append(child)
        population = new_pop
    return population[0], generations

# ---------- INPUT ----------
n = int(input("Enter N for N-Queens (Genetic Algorithm): "))

t1 = time.time()
solution, gen = genetic_nqueen(n)
t2 = time.time()

print(f"\nBest Solution: {solution}")
print(f"Heuristic Value: {heuristic(solution)}")
print(f"Generations: {gen}")
print(f"⏱ Execution Time: {t2 - t1:.6f}s")
print("🧮 Time Complexity: O(G * P * N)")
print("📦 Space Complexity: O(P * N)")
