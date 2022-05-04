import sys

n = int(sys.stdin.readline())
length = 4 * n - 3
arr = [[' ' for i in range(length)] for j in range(length)]

def dot19(n, k):
    if n == 1:
        arr[k][k] = '*'
        return 0
    cur_len = 4 * n - 3
    for i in range(k, k + cur_len):
        arr[i][k] = '*'
        arr[k][i] = '*'
        arr[i][k + cur_len - 1] = '*'
        arr[k + cur_len - 1][i] = '*'

    return dot19(n - 1, k + 2)


dot19(n, 0)
for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], end="")
    print("")