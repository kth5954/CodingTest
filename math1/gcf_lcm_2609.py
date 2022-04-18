import sys


# gcf: 최대공약수, lcm: 최소공배수
# 두 수의 곱을 최대공약수로 나누면 최소공배수가 된다

a, b = map(int, sys.stdin.readline().split())
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    res = (x * y) // gcd(x, y)
    return res


print(gcd(a, b))
print(lcm(a, b))