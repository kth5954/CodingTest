import sys

n = int(sys.stdin.readline())
d = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if i < j * j:
            break
        if d[i] > d[i - j * j] + 1:
            d[i] = d[i - j * j] + 1

print(d.pop())