from collections import deque
import sys

def bfs(v, his):
    queue = deque([(v, his)])
    while queue:
        x, his = queue.popleft()
        for i in [x + 1, x * 2, x * 3]:
            if i == n:
                return d[x] + 1, his + [i]
            elif i < n and d[i] == 0:
                queue.append((i, his + [i]))
                d[i] = d[x] + 1


n = int(sys.stdin.readline())
if n == 1:
    print(0)
    print(1)
else:
    d = [0] * (n + 1)
    cnt, his = bfs(1, [1])
    print(cnt)
    print(*his[::-1])

