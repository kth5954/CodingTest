row, col = 5, 5
matrix = [[] for i in range(row)]  # [[][][][][]]

for i in range(row):
    for j in range(col):
        matrix[i].append((i, j))

print(matrix)