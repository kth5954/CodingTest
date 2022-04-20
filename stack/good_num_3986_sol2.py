import sys
from collections import deque


n = int(sys.stdin.readline())
arr = []
cnt = 0
for i in range(n):
    inp = sys.stdin.readline().rstrip()
    while inp:
        if 'AA' in inp or 'BB' in inp:
            inp = inp.replace('AA', '')
            inp = inp.replace('BB', '')
        else:
            break
    if not inp:
        cnt += 1


print(cnt)