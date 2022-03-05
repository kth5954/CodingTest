import sys

n = int(sys.stdin.readline())
stair = [[0] * 10 for i in range(n + 1)]
stair[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n + 1):
    stair[i][0] = stair[i - 1][1]
    stair[i][9] = stair[i - 1][8]
    for j in range(1, 9):
        stair[i][j] = stair[i - 1][j - 1] + stair[i - 1][j + 1]

print(sum(stair[n]) % 1000000000)

