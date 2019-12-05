from random import randint

# HT_3 lvl_1 v.1.5

M = [[1, 0, 0, 0],
     [0, 2, 0, 0],
     [0, 0, 3, 0],
     [0, 0, 0, 4]]

# Matrix new

for i in range(len(M)):
    for j in range(len(M[i])):
        c = randint(1, 30)
        M[i][j] = c
print(M)

# Matrix diag

for q in range(len(M)):
    print(str(M[q][q]) + " Diagonal'")

# HT_3 lvl_2 v.1.0

print(max(max(M[z]) for z in range(len(M[i]))))

