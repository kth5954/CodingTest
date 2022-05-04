import sys
from math import gcd

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    inp = int(sys.stdin.readline())
    arr.append(inp)

diff = []
for i in range(1, len(arr)):
    diff.append(arr[i] - arr[i - 1])
gcd_diff = gcd(*diff)
del diff
cnt = 0
for i in range(1, len(arr)):
    cnt += ((arr[i] - arr[i - 1])//gcd_diff) - 1
print(cnt)