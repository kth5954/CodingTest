import sys

n = int(sys.stdin.readline())
arr = []
k = [1] * (n + 1)
for i in range(n):
    inp = int(sys.stdin.readline())
    arr.append(inp)

arr.sort()
val = 0
for i in range(n):
    val += abs((i + 1) - arr[i])
print(val)