import sys

def gcf(x, y):
    while y:
        x, y = y, x % y

    return x

def lcm(x, y):
    return x * y // gcf(x, y)


n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))




