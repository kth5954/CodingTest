import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
miro = []
for i in range(N):
    miro.append(list(map(int, sys.stdin.readline().rstrip())))


# 너비 우선 탐색
def bfs(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N - 1][M - 1]


print(bfs(miro, 0, 0))



