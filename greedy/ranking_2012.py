import sys
from itertools import permutations

n = int(sys.stdin.readline())
arr = []
ans = 0
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
for i in range(n):
    ans += abs(arr[i] - (i + 1))
print(ans)