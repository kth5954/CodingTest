import sys

n = int(sys.stdin.readline())
d = [0] * (n + 1)

for i in range(2, n + 1):
    arr = [d[i - 1]]
    if not i % 3:
        arr.append(d[i // 3])
    if not i % 2:
        arr.append(d[i // 2])
    d[i] = min(arr) + 1

print(d.pop())