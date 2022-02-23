# 효율적인 화폐구성
import sys

n, m = map(int, sys.stdin.readline().split())
c = []
for i in range(n):
    c.append(int(sys.stdin.readline()))

d = [10001] * (m + 1)
d[0] = 0
for i in range(n):
    for j in range(c[i], m + 1):
        if d[j - c[i]] != 10001:
            d[j] = min(d[j], d[j - c[i]] + 1)
            print("j: %d,  d[%d]: %d" % (j, j, d[j]))

print(d)



