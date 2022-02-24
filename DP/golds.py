import sys
t = int(sys.stdin.readline())
for q in range(t):
    n, m = map(int, sys.stdin.readline().split())
    inp = list(map(int, sys.stdin.readline().split()))
    table = [[0 for r in range(n)] for c in range(m)]
    k = 0
    for r in range(n):
        for c in range(m):
            table[c][r] = inp[k]
            k += 1

    d = table
    for i in range(1, m):
        for j in range(n):
            if j == 0:
                mid, lower = d[i - 1][j], d[i - 1][j + 1]
                d[i][j] = max(mid, lower) + d[i][j]

            elif j == n - 1:
                upper, mid = d[i - 1][j - 1], d[i - 1][j]
                d[i][j] = max(upper, mid) + d[i][j]

            else:
                upper, mid, lower = d[i - 1][j - 1], d[i - 1][j], d[i - 1][j + 1]
                d[i][j] = max(upper, mid, lower) + d[i][j]
    print(max(d[m - 1]))