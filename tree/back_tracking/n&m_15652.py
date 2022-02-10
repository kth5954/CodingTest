from itertools import *


n, m = map(int, input().split())

arr = [i+1 for i in range(n)]
res = list(combinations_with_replacement(arr, m))
for r in res:
    print(" ".join(map(str, r)))