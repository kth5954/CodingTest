import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


def bfs(g, x_init, y_init, k):
    if visited[x_init][y_init] or g[x_init][y_init] < k:
        return False
    queue = deque([[x_init, y_init]])
    visited[x_init][y_init] = 1
    while queue:
        x, y = queue.popleft()
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            if g[nx][ny] >= k and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append([nx, ny])
    return True


max_cnt = 0
for k in range(101):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if bfs(graph, i, j, k):
                cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)
