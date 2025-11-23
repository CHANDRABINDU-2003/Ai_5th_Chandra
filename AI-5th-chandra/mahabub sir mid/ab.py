# Define known relationships
parents = set()
parents.add(("John", "Mary"))  # John is Mary's parent
parents.add(("Mary", "Joe"))   # Mary is Joe's parent

# Define the Parent predicate
def Parent(x, y):
    return (x, y) in parents

# Define the Grandparent rule
def Grandparent(x, z):
    # A grandparent relationship exists if x is the parent of some y, and y is the parent of z
    for y in [p[1] for p in parents if p[0] == x]:  # All children y of x
        if Parent(y, z):  # Check if y is the parent of z
            return True
    return False

# Define the Ancestor rule using recursion
def Ancestor(x, z):
    # Direct ancestor (parent)
    if Parent(x, z):
        return True
    # Recursive ancestor (parent of an ancestor)
    for y in [p[1] for p in parents if p[0] == x]:  # All children y of x
        if Ancestor(y, z):
            return True
    return False

# Test the logic
print("Is John the parent of Mary?", Parent("John", "Mary"))
print("Is Mary the parent of Joe?", Parent("Mary", "Joe"))
print("Is John the grandparent of Joe?", Grandparent("John", "Joe"))
print("Is John an ancestor of Joe?", Ancestor("John", "Joe"))
