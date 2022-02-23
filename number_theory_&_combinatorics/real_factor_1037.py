import sys

n = int(sys.stdin.readline())
factor_of_n = list(map(int, sys.stdin.readline().split()))

print(max(factor_of_n) * min(factor_of_n))
