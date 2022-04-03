import sys

T = int(sys.stdin.readline())
testCases = []
for i in range(T):
    t = int(sys.stdin.readline())
    testCases.append(t)
MAX = max(testCases)
dp = [0] * (MAX + 1)
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, MAX + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009
for i in testCases:
    print(dp[i] % 1000000009)
