import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    p = [1] * (n + 1)
    if 1 <= n <= 3:
        print(1)
    elif 4 <= n <= 5:
        print(2)
    else:
        p[4], p[5] = 2, 2
        for i in range(6, n + 1):
            p[i] = p[i - 1] + p[i - 5]
        print(p.pop())
