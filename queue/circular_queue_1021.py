import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
val = deque(list(map(int, sys.stdin.readline().split())))
cq = deque([i + 1 for i in range(n)])  # 1 2 3 4 5 6 7 8 9 10
cnt = 0
for v in val:
    while True:
        if cq.index(v) == 0:
            cq.popleft()
            break
        elif cq.index(v) <= len(cq) - cq.index(v):
            cq.append(cq.popleft())
            cnt += 1
        else:
            cq.appendleft(cq.pop())
            cnt += 1
print(cnt)