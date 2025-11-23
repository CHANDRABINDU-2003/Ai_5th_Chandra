import truthtable as ttg

equations= [" A == B "," not A or B"," A ^ B"," A or B"," A and B"]
table=ttg.Table(['A','B'],equations)
print(table)