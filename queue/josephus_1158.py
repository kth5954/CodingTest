import sys
from collections import deque

n, k =map(int, sys.stdin.readline().split())
queue = deque(i + 1 for i in range(n))
res = []
i = 0
while queue:
    if i == k - 1:
        res.append(queue.popleft())
        i = 0
        continue
    queue.append(queue.popleft())
    i += 1
print("<", end="")
for i in res:
    if i == res[-1]:
        print("%d>" % i)
        continue
    print(i, end=", ")
