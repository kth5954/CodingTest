import sys

n, k = map(int, sys.stdin.readline().split())
curr = []

for i in range(n):
    curr.append(int(sys.stdin.readline()))

d = [0] * (k + 1)
d[0] = 1

for c in curr:
    for j in range(1, k + 1):
        if j - c >= 0:
            d[j] += d[j - c]

print(d[-1])