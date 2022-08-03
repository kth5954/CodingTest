import sys
from collections import deque


def bfs(graph, v, visited):
    visited[v] = 1
    queue = deque([v])
    while queue:
        x = queue.popleft()
        visited[x] = 1
        for i in range(1, n + 1):
            if graph[x][i] and not visited[i]:
                queue.append(i)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visited = [0] * (n + 1)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

bfs(arr, 1, visited)
print(sum(visited) - 1)

