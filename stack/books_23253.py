import sys
from collections import deque
readline = sys.stdin.readline

ordered = "Yes"
n, m = map(int, readline().split())
packages = deque()
for i in range(m):
    k = int(readline())
    nums = list(map(int, readline().split()))
    if sorted(nums) != nums:
        ordered = "No"
        break

print(ordered)

