import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    queue = deque([v])
    visited[v] = 1
    cnt = 0
    while queue:
        x = queue.popleft()
        for k in graph[x]:
            if not visited[k]:
                visited[k] = 1
                queue.append(k)
                cnt += 1
    return cnt


print(bfs(1))


