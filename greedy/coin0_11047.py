import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
cnt = 0
for i in range(n):
    coins.append(int(sys.stdin.readline()))

for i in range(n - 1, -1, -1):
    if k:
        cnt += k//coins[i]
        k %= coins[i]

print(cnt)