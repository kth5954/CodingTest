# # X가 주어졌을 때
# # X//5 == 0 -> X//5
# # X//3 == 0 -> X//3
# # X//2 == 0 -> X//2
# # X - 1
# 네 가지 연산중 하나 골라서 실행
# bottom up
import sys

x = int(sys.stdin.readline())

dp = [0] * 30001
for i in range(2, x + 1):
    # 4가지 연산으로 갈 수 있는 dp값을 리스트에 넣어주고 그 다음 최솟값이랑 + 1을 해줌
    pre_dp = []
    if i % 5 == 0:
        pre_dp.append(dp[i//5])
    if i % 3 == 0:
        pre_dp.append(dp[i//3])
    if i % 2 == 0:
        pre_dp.append(dp[i//2])
    pre_dp.append(dp[i - 1])
    dp[i] = min(pre_dp) + 1
print(dp[x])
