import sys

n = int(sys.stdin.readline())
tr = []
for i in range(n):
    tr.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, n):
    tr[i][0], tr[i][-1] = tr[i - 1][0] + tr[i][0], tr[i - 1][-1] + tr[i][-1]
    for k in range(1, len(tr[i]) - 1):
        tr[i][k] = max(tr[i - 1][k - 1], tr[i - 1][k]) + tr[i][k]


print(max(tr[-1]))