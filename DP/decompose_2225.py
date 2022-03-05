import sys

n, k = map(int, sys.stdin.readline().split())

d = [[1 for i in range(n + 1)] for j in range(k + 1)]

for i in range(2, k + 1):
    d[i][0], d[i][1] = 0, i

for i in range(2, k + 1):
    for j in range(2, n + 1):
        d[i][j] = d[i - 1][j] + d[i][j - 1]

print(d[k].pop() % 1000000000)