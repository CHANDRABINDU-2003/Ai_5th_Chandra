from collections import deque

def ac3(csp):
    # Initialize the queue with all arcs in the CSP
    queue = deque([(Xi, Xj) for Xi in csp['variables'] for Xj in csp['neighbors'][Xi]])

    while queue:
        # Remove the first arc from the queue
        Xi, Xj = queue.popleft()

        # Revise the domain of Xi based on the constraint with Xj
        if revise(csp, Xi, Xj):
            # If the domain of Xi is empty, return False (inconsistency found)
            if not csp['domains'][Xi]:
                return False

            # For each neighbor Xk of Xi (except Xj), add (Xk, Xi) to the queue
            for Xk in csp['neighbors'][Xi] - {Xj}:
                queue.append((Xk, Xi))

    return True

def revise(csp, Xi, Xj):
    revised = False
    domain_Xi = csp['domains'][Xi]
    domain_Xj = csp['domains'][Xj]

    for x in domain_Xi.copy():  # Copy to avoid modifying the list while iterating
        # Check if there is no value y in Dj that satisfies the constraint between Xi and Xj
        if not any((x, y) in csp['constraints'][(Xi, Xj)] for y in domain_Xj):
            domain_Xi.remove(x)  # Remove x from the domain of Xi
            revised = True

    return revised

# Example CSP input structure
csp = {
    'variables': {'X1', 'X2', 'X3'},
    'domains': {
        'X1': {1, 2, 3},
        'X2': {1, 2},
        'X3': {2, 3},
    },
    'neighbors': {
        'X1': {'X2', 'X3'},
        'X2': {'X1', 'X3'},
        'X3': {'X1', 'X2'},
    },
    'constraints': {
        ('X1', 'X2'): {(1, 2), (2, 1), (3, 1)},
        ('X2', 'X1'): {(2, 1), (1, 2), (1, 3)},
        ('X1', 'X3'): {(1, 3), (2, 2), (3, 2)},
        ('X3', 'X1'): {(3, 1), (2, 2), (2, 3)},
        ('X2', 'X3'): {(1, 2), (2, 3)},
        ('X3', 'X2'): {(2, 1), (3, 2)},
    }
}

# Run AC-3 algorithm
result = ac3(csp)
print("AC-3 result:", result)
print("Domains after AC-3:", csp['domains'])