import sys

n = int(sys.stdin.readline())
stair = [0]
for i in range(n):
    stair.append(int(sys.stdin.readline()))
if n == 1:
    print(stair[1])
else:
    d = [0] * (n + 1)
    d[1] = stair[1]
    d[2] = stair[1] + stair[2]

    for i in range(3, n + 1):
        d[i] = max(d[i - 3] + stair[i - 1] + stair[i], d[i - 2] + stair[i])
    print(d)