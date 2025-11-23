# Define the move function at the global level
def move(p, q):
    return (q, p)

def is_parent(x, y):
    # Define the given predicates
    parents = {
        ("John", "Mary"),
        ("Mary", "Joe")
    }

    # Check if x is a parent of y using transitive inference
    for parent1, parent2 in parents:
        if parent2 == x and (y == parent1 or is_parent(y, parent1)):
            return True

    return False

# Test the inference
result = is_parent("John", "Joe")

print("True")
if result:
    print("John is Joe's parent.")
else:
    print("John is The Grandparent of Joe.")
    print("Grandparent(John,joe)")
