import sys

n = int(sys.stdin.readline())

dp = [0] * (n + 1)
dp[0] = 0
for i in range(2, n + 1):
    pre_ord = []
    if i % 3 == 0:
        pre_ord.append(dp[i // 3])
    if i % 2 == 0:
        pre_ord.append(dp[i // 2])
    pre_ord.append(dp[i - 1])
    dp[i] = min(pre_ord) + 1

print(dp[-1])
