import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

acc = [0] * n

for i in range(n):
    for j in range(i + 1):
        acc[i] += arr[j]
print(sum(acc))

# 1 2 3 3 4