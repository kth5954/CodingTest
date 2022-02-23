import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))

# 점화식(Recurrence Relation)
# A(i) = max(Ai-1, k(1) + A(i-2))

dp = [0] * n
dp[0] = k[0]
dp[1] = max(dp[0], k[1])
for i in range(2, n):
    dp[i] = max(dp[i - 1], k[i] + dp[i - 2])



