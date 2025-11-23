def propositional_logic():
    headers=['   p   ','    q   ',' p AND q  ',' p OR q ',' p xor q ',' p => q ',' p <=> q ']
    print("|".join(headers))
    print("_" * (len("|".join(headers))))
    for p in[False, True]:
        for q in [False, True]:
            row=[p,q,p and q, p or q,((((not p) and q)) or ((p and (not q)))), (not p) or q, (p and q) or ((not p) and (not q))]
            row_str="  |  ".join(map(str,row))
            print(row_str)

propositional_logic()