import truthtable as ttg

equation = "(A and B) or (not B and C)"
table = ttg.Table(['A', 'B', 'C'], [equation])

print(table)
