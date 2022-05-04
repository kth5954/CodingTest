import sys

def star(n, k, t):
    print(k, t)
    if n == 0:
        return 0
    for i in range(k, 2**n):
        arr[k][i] = '*'  # 0 0, 0 1, 0 2,  ... 0 7
        arr[i][k] = '*'  # 0 0, 1 0, 2 0,  ... 7 0
        arr[i][2**n - i - 1] = '*'  # 0 7, 1 6, ... 7 0
        arr[2**n//2 + k][i//2] = '*'
        arr[i//2][2**n//2 + k] = '*'  # 0 4, 1 4, 2 4, 3 4, 4 4
        arr[i//2][(2**n - i - 1)//2] = '*'
    star(n - 1, k, t + 2**n//2)
    star(n - 1, k + 2**n//2, t)
    star(n - 1, k + 2**n//2, t + 2**n//2)


n = int(sys.stdin.readline())
arr = [[' ' for j in range(2**n)] for i in range(2**n)]
star(n, 0, 0)

if n:
    for i in arr:
        print(i)