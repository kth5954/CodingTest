import sys

def sol(k):
    if k == 1:
        return 1
    if k == 2:
        return 2
    if k == 3:
        return 4
    else:
        return sol(k - 1) + sol(k - 2) + sol(k - 3)


n = int(sys.stdin.readline())
for i in range(n):
    print(sol(int(sys.stdin.readline())))


