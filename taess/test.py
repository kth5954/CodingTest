list = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]

row, col = 3, 4
table = [[0 for r in range(row)] for c in range(col)]

k = 0
for i in range(3):
    for j in range(4):
        table[j][i] = list[k]
        k += 1
print(table)