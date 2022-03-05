import sys

n = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))

d = [0] * (n + 1)
d[0], d[1] = 1, 1
for i in range(2, n + 1):
    for j in range(1, i):
        if arr[i] > arr[j]:
            d[i] = max(d[j] + 1, d[i])
print(max(d))
