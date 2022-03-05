import sys

n = int(sys.stdin.readline())
stair = []
for i in range(n):
    stair.append(int(sys.stdin.readline()))

if n == 1:
    print(stair[0])
else:
    d = [0] * n
    d[0] = stair[0]
    d[1] = stair[0] + stair[1]
    for i in range(2, n):
        d[i] = max(d[i - 2] + stair[i], d[i - 3] + stair[i - 1] + stair[i])

    print(d.pop())