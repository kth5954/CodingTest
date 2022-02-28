# 가장 긴 증가하는 부분 수열(LIS)
# -> 가장 긴 감소하는 부분 수열로 응용하여 풀 수 있음
import sys

n = int(sys.stdin.readline())
inp = list(map(int, sys.stdin.readline().split()))
d = [1] * (len(inp))

for i in range(1, n):
    for j in range(i):
        if d[i] > d[j]:
            d[i] = max(d[i], d[j] + 1)


print(n - max(d))