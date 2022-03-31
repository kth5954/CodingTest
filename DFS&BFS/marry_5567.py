import sys
from collections import deque, defaultdict

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = defaultdict(list)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    cnt = 0
    visited = [0] * (n + 1)
    queue = deque([[1, 0]])
    visited[1] = 1
    while queue:
        x, dist = queue.popleft()
        if dist <= 2:
            cnt += 1
        for v in graph[x]:
            if not visited[v]:
                queue.append([v, dist + 1])
                visited[v] = 1
    return cnt - 1


print(bfs())