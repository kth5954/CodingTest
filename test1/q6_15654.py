import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
ans = permutations(arr, m)

for i in ans:
    print(' '.join(list(map(str, i))))
