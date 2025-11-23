def implies(p, q):
    return not p or q

# p - score 100, q - earns A
def print_truth_table():
    headers = ["p", "q", "p => q"]


    score = input("p:" )
    earns = input("q: ")

    # Print table header
    print(" | ".join(headers))
    print("-" * 15)

    # Generate and print truth table
    for p in [score]:
        for q in [earns]:
            result = implies(p, q)
            row = [str(p), str(q), str(result)]
            print("|".join(row))

# Print the truth table
print_truth_table()